import logging
import openai

logging.basicConfig(level=logging.DEBUG)
# Init openAI API
openai.api_key = [API_KEY]
# init de GPT
def get_init ():
    type_chatbot = '''"salut gpt je vais te donner des example de prompt pour stable diffision pour que tu m'aide a améliorer et traduire en anglais mes prompt que je vais te donner par la suite  voici les prompt d'examlpe : A robot working on a computer, learning,
                art by Gediminas Pranckevicius and
                Alexander Jansson, books on background,  A very very cute cat wearing sunglasses,
                kawaii, smiling, in the style of Artgerm,
                Gerald Brom, Atey Ghailan and Mike
                Mignola, pastel colors, studio lighting, plain
                background, comic cover art, trending on
                Artstation, sharp, focus, cell shading, wearing
                a sweater and a scarf, centered.An old mechanical factory on a raft, lots of
                cogs, cables and gears. Concept art,
                trending on artstation, style deponia, very
                detailed, intricate, realistic, 4k, octane
                render, fine details,A robot trying to land on the moon, art by
                Alexander Jansson and Gediminas
                Pranckevicius, cartoon lunar rover lander.A concept art of neo-tokyo in the rain, art by wlop, poster, lot of
                details, intricate and ray tracing."'''
    messages=[
        {"role": "system", "content": type_chatbot}]
    chatbot(messages)  
     
print("Bonjour, Écriver vos prompt pour stable diffision pour que je les améliore. OU appuyer sur Ctrl+C pour quitter!")

#Création de la conversation avec GPT
def chatbot (messages):
    while True:
        user_input = input("User: ")
        messages.append({"role": "user","content": user_input}) 
        reponse = openai.ChatCompletion.create(
            model= [MODEL_GPT],
            messages = messages
        ).choices[0].message
        
        messages.append(reponse)
        print("GPT:",reponse.content)

get_init()