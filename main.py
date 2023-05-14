import os
import openai
from dotenv import load_dotenv
from db.manager import Admin

load_dotenv()  # take environment variables from .env.

openai.api_key = os.environ.get("API_KEY")


def answer_ai(messages):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        return response['choices'][0]['message']['content']

    except openai.OpenAIError as e:
        
        admin = Admin()
        admin.add_error(message=e)

        return 'Кажется я времмено отключился от ИИ 🤒. Пожалуйста, отправьте запрос позже.'

    except Exception as e:
        # Handle other exceptions
        return 'Что то пошло не так. Пожалуйста, отправьте запрос позже'

