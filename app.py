from flask import Flask, render_template, request
from flask import Flask, jsonify,request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)
bot = ChatBot("Flutter")
trainer = ListTrainer(bot)

file =  open("static/file.text", "r")
conversation = file.read()

trainer.train(conversation)

# @app.route("/")
# def home():
#     return render_template("index.html")

@app.route("/", methods = ['GET','POST'])
def get_bot_response():
    if request.method == 'GET':
        userText = request.args.get('msg')
        print("working", userText)
        res = str(bot.get_response(userText))
        return jsonify({"response" : res})
    elif request.method == 'POST':
        print("POST")

if __name__ == "__main__":
    app.run()


# app = Flask(__name__)

# @app.route("/bot", methods=["POST"])
# def response():
#     query = dict(request.form)['query']
#     res = query + " " + time.ctime()
#     return jsonify({"response" : res})
    
# if __name__=="__main__":
#     app.run()