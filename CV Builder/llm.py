from google import genai
from googleapi import API_KEY

def gen_html(info, photo_path=None):

    client = genai.Client(api_key=API_KEY)

    custom_config = {
        "system_instruction": """
                        You are a professional CV maker. the user will pass its info 
                        the job he is applying for. the role. i mean the info. analyze the 
                        info and generate a html that python xhtml2pdf can hanlde and 
                        make a beautifull and professinal CV. Also if he pass its image add that to pdf as well 
                        using the same html that xhtml2pdf can handle,
                            """
    }   

    print("Started Writing HTML.......")
    interactions = client.interactions.create(
        model="gemini-3.5-flash-lite", 
        input=f"photo path: \n{photo_path}\nInfo about user\n{info}\nNow write a html which xhtml2pdf can use. return only the html", 
        generation_config=custom_config
    )

    return interactions.output_text