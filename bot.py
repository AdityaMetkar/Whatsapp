from flask import Flask, jsonify,request
from flask_cors import CORS
from chatterbot import ChatBot



app = Flask(__name__)
cors = CORS(app)



class compile:
    def __init__(self):
        # print("cunstructor")
        self.chatbot = ChatBot(
        'Training Example',
        preprocessors=['chatterbot.preprocessors.clean_whitespace'],
        logic_adapters=[
            'chatterbot.logic.MathematicalEvaluation','MyTimeLogic.MyTimeLogicAdapter',
            'chatterbot.logic.BestMatch',
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': 'I am sorry, but I do not understand.',
                'maximum_similarity_threshold': 0.6
            }]
        )


    def predict(self,q):
        self.ans=""
        # print("func",q)
        ans=self.chatbot.get_response(q)

        if(ans.confidence==0):
            ans='I am sorry, but I do not understand.'
    
        return ans

        

@app.route("/receiver",methods=["POST","GET"])
def postME():
      
    data = request.json

    try:
        bot.ans=bot.predict(data)
    except:
        print("server exception")

    # print("server",data,bot.ans)
    return jsonify(str(bot.ans))

    

bot=compile()

app.run(debug=True)


