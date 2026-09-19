from google import genai
from google.genai import types
from googleapi import API_KEY
from browser_search import get_weather, get_books_info, get_country
import json

func_map = {
    "get_weather": get_weather, 
    "get_books_info": get_books_info, 
    "get_country": get_country
}

def gen_response(query):

    client = genai.Client(api_key=API_KEY)

    chat = client.chats.create(
        model="gemini-3.5-flash-lite", 
        config=types.GenerateContentConfig(
            tools=[get_books_info, get_weather, get_country], 
            system_instruction="Your are a smart agent. you have tools to get weather, country detials, books info, and using ge weather you can get details about specific area city",
            automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True)
        )
  )

    res = chat.send_message(query)

    if not res.function_calls:
        return res.text

    else:

        for fc in res.function_calls:
            func_name = fc.name
            func_args = fc.args

            func_real_name = func_map.get(func_name)
            func_result = func_real_name(**func_args)

            final_res = chat.send_message(
                types.Part.from_function_response(
                    name=func_name, 
                    response={"results": func_result}
                )
            )

        return final_res.text
print(gen_response("can you give me brief info about pakistan"))
