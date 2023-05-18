import os
import openai
from dotenv import load_dotenv
from db.manager import Admin

import sys

load_dotenv()  # take environment variables from .env.

openai.api_key = os.environ.get("API_KEY")


def answer_ai(messages, chat_id):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        return response['choices'][0]['message']['content']

    except openai.OpenAIError as e:
        admin = Admin()
        admin.add_error(message=e)
        admin.delete_limited_messages(chat_id=chat_id)
        
        return "Я  отключился от ИИ из-за большого количества запросов 🤒. Пожалуйста, отправьте запрос позже."


    except Exception as e:
        # Handle other exceptions

        admin = Admin()
        admin.add_error(message=e)

        return "Что-то пошло не так. Пожалуйста, отправьте запрос позже"

