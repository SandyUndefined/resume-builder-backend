# from flask import Flask, render_template, request
# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
# from chatterbot.trainers import ListTrainer

# app = Flask(__name__)
# bot = ChatBot("Sunanda's Resume ChatBot")
# trainer = ListTrainer(bot)

# file =  open("static/file.text", "r")
# conversation = file.read()

# trainer.train(conversation)

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/")
# def get_bot_response():
#     userText = request.args.get('msg')
#     print("working")
#     return str(bot.get_response(userText))

# if __name__ == "__main__":
#     app.run()

from flask import Flask, jsonify,request
import time

app = Flask(__name__)

@app.route("/bot", methods=["POST"])
def response():
    query = dict(request.form)['query']
    res = query + " " + time.ctime()
    return jsonify({"response" : res})
    
if __name__=="__main__":
    app.run()