import openai

openai.api_key = ""#Relacionar su Apikey personal

conversation = ""#Este permanece vacío

i = 1
while (i != 0):
    question =  input("Persona:")
    conversation += "\nPersona: " +  question + "\nAI:"
    response = openai.Completion.create(
        engine="davinci",
        prompt=conversation,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n", " Persona:", " AI:"]
    )

    answer = response.choices[0].text.strip()
    conversation += answer
    print("AI: "+ answer + "\n")