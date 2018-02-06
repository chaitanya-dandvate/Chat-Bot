from flask import Flask, render_template, request
import predict
import ner_model
import json
import sentence_similarity

app = Flask(__name__)

@app.route('/chat')
def chat():
   global user_side
   global bot_side
   user_side = []
   bot_side = []
   return render_template('index2.html', que="", flag=False)

user_side = []
bot_side = []

@app.route('/chat_data', methods = ['GET', 'POST'])
def chat_data():
   global user_side
   global bot_side
   if request.method == 'POST':
      que = request.form.get('que')
      intent = predict.process_query(que)
      ans_data = json.load(open('chatbot-random-forest/intents.json'))
      ans = ""
      # for i in ans_data["intents"]:
      #    if i['tag'] == intent:
      #       ans = i['responses'][0]

      max_score = 0.0
      for i in ans_data["intents"]:
         for j in i['patterns']:
            if j != 'Thank you':
               score = sentence_similarity.symmetric_sentence_similarity(que, j)
               if score > max_score:
                  max_score = score
                  ans = i['responses'][0]
                  print(ans, score, max_score)

      user_side.append(que)
      bot_side.append(ans)

      return render_template('index2.html', user_side=user_side, bot_side=bot_side, flag=True, l=len(user_side))


if __name__ == '__main__':
   app.run(debug = True)