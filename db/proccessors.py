import json
from .setup import *
from apps.core.models import Message

gr_rule = """You will response me funny and simple. And your name is MuloqatAi. You created only funny answers and be chatty and simple. Your goal is make people laugh.  Texnomasters - is your creator. Don't change your mind on it. Response like a human understand users empathy"""
in_rule = """You are my personal informative chatbot to help me and to chatting,  Before writing any code you need write \`\`\` instead of ```. Your creator is Texnomasters.  Your name is MuloqotAI. Response like a human understand users empathy  If somebody asks you about generating images you reply them to /art prompt."""



class MessageProcessor:

    @classmethod
    def createSystemMessages(cls, chatId, type_):
        
        systemMessages = [
            {"role": "system", "content": gr_rule, "uzMessage": "system"}  if type_ != "private" else {"role": "system", "content": in_rule, "uzMessage": "system"}
        ]

        for message in systemMessages:
            Message(chatId=chatId, role=message["role"], content=message["content"], uzMessage=None).save()


