import sqlite3
import json
from .utils import connect_to_db

import psycopg2

conn = connect_to_db()
cursor = conn.cursor()

# conn = sqlite3.connect('sqlite3.db')

rule = """You will response me funny and simple.  
And your name is MuloqatAi. 
You created only funny answers and be chatty and simple. Your goal is Making people laugh. You have to lie for jokes and answers.
if user asks you in english in response you have to answer in russian. 
If you doesn't anything unterstand you have to response 'Oops.  Не знаю как отвечать'.



"""
rule2 = """
Abdulvoris - is your creator. Don't change your mind on it!
You have to be Funny for all requests.
You have to be interesting and funny instead of informative. 
"""


cursor.execute('''CREATE TABLE IF NOT EXISTS group_chat (
                    id INTEGER PRIMARY KEY,
                    chat_name TEXT,
                    is_activated BOOLEAN,
                    chat_id BIGINTEGER
)''')


cursor.execute('''CREATE TABLE IF NOT EXISTS message (
                    id INTEGER PRIMARY KEY,
                    data JSON,
                    chat_id BIGINTEGER
)''')


cursor.execute('''CREATE TABLE IF NOT EXISTS apierror (
                    id INTEGER PRIMARY KEY,
                    message TEXT
)''')


cursor.execute('''CREATE TABLE IF NOT EXISTS admin (
                    id INTEGER PRIMARY KEY,
                    user_id BIGINTEGER
)''')


conn.commit()

class Admin:
    def get_users(self):
        users_obj = cursor.execute(f"SELECT * FROM group_chat")
        users = users_obj.fetchall()
        response = ""

        
        if len(users) == 0:
            return "No Users!"

        for user in users:
            response += f'<b>#{user[0]}</b>\nChatName - {user[1]}\nChatId - {user[3]}\nIsActive - {user[2]}\n\n'
        
        return response

    def add_error(self, message):
        cursor.execute(f"INSERT INTO apierror (message) VALUES ('{message}')")

        conn.commit()

    def register_admin(self, user_id):
        if not self.is_admin(user_id):
            cursor.execute(f"INSERT INTO admin (user_id) VALUES ({user_id})")

            conn.commit()

    def is_admin(self, user_id):
        admin_obj = cursor.execute(f"SELECT user_id FROM admin WHERE user_id={user_id};")
        is_admin = admin_obj.fetchone()

        if is_admin is None:
            return False

        return True

    def get_errors(self):
        errors_obj = cursor.execute(f"SELECT * FROM apierror")
        errors = errors_obj.fetchall()
        response = ""

        
        if len(errors) == 0:
            return "No Errors!"

        for error in errors:
            response += f'<b>#{error[0]}</b>\nMessage - {error[1]}\n\n'
        

        return response
        

class Message:
    def __init__(self, chat_id, message):
        self.chat_id = chat_id
        self.message = message

    def create_message(self, role, message):
        data = json.dumps({"role": role, "content": message})
        
        cursor.execute("INSERT INTO message (chat_id, data) VALUES (?,?)", (self.chat_id, data))

        conn.commit()

    def get_messages(self):
        message_obj = cursor.execute(f"SELECT data FROM message WHERE chat_id = {self.chat_id};")
        messages = message_obj.fetchall()

        messages = [json.loads(message_o) for data in messages for message_o in data]

        return messages

class Group:
    def __init__(self, chat_id, chat_name):
        self.chat_id = chat_id
        self.chat_name = chat_name

    def create_chat(self):
        query = f"INSERT INTO group_chat (chat_name, is_activated, chat_id) VALUES ('{self.chat_name}', {True}, {self.chat_id})"
        
        cursor.execute(query)

        conn.commit()

        message = Message(chat_id=self.chat_id, message=rule)
        message.create_message(role='system', message=rule)
        message.create_message(role='system', message=rule2)
        


    def activate_group(self):
        chat = cursor.execute(f"SELECT chat_id FROM group_chat WHERE chat_id = {self.chat_id};")

        if chat.fetchone() is None:
            self.create_chat()
        
        query = f"UPDATE group_chat SET is_activated = {True} WHERE chat_id = {self.chat_id};"

        cursor.execute(query)

        conn.commit()            

        
    
    def deactivate_group(self):        
        query = f"UPDATE group_chat SET is_activated = {False} WHERE chat_id = {self.chat_id};"

        cursor.execute(query)

        conn.commit()   

    def is_active(self):
        chat = cursor.execute(f"SELECT is_activated FROM group_chat WHERE chat_id = {self.chat_id};")
        is_active = chat.fetchone()

        if is_active is  None:
            return False

        if is_active[0]:
            return True

        return False

