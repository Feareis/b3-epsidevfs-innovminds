import requests
from datetime import datetime

def get_date():
    return datetime.now().strftime("%A %d %B %Y")

def get_weather(city):
    try:
        api_key = "37b2afbfa70f43ffb75175846241511"  # Remplacez par votre clé API
        url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=1"
        response = requests.get(url)
        data = response.json()
        forecast = data['forecast']['forecastday'][0]['day']
        return f"Météo à {city} demain : {forecast['condition']['text']}, température de {forecast['mintemp_c']}°C à {forecast['maxtemp_c']}°C."
    except Exception as e:
        return f"Impossible de récupérer la météo : {e}"

def answer_question(q):
    question = q.lower()
    if "date" in question:
        return f"Aujourd'hui, nous sommes le {get_date()}."
    elif "météo" in question and "grenoble" in question:
        return get_weather("Grenoble")
    else:
        return "Pour les questions locales, je suis en apprentissage. Merci de poser une question générale ou de me renseigner avec des données spécifiques."

# Exemple d'utilisation
while True:
    question = input("Posez une question : ")
    print(answer_question(question))
