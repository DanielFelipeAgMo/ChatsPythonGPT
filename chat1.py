import openai
import prompt_toolkit

# Configura tu clave de API de OpenAI
openai.api_key = ""

# Define una función que envía una solicitud a la API de OpenAI y devuelve la respuesta
def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci", prompt=prompt, max_tokens=50
    )
    return response.choices[0].text

# Ejecuta el chatbot
while True:
    user_input = prompt_toolkit.prompt("> ")
    response = generate_response(user_input)
    print(response.strip())
