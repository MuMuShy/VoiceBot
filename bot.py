from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


class ChatBotClass():

    def init(self):
        self.bot = ChatBot('sara')
        trainer = ChatterBotCorpusTrainer(self.bot)
        trainer.train("./test.yml")
        #trainer.train("chatterbot.corpus.chinese.greetings")
        #trainer.train("chatterbot.corpus.chinese.conversations")


    def hellowGreed(self):
        print( self.bot.get_response("測試"))


    def getResponse(self,text):

        print(":BotCore:"+text)
        result = self.bot.get_response(text)
        print("result:"+str(result))
        return str(result)