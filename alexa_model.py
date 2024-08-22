# Instruction Set - 1 (Status Failed)

# I'm creating this project in seperate virtual environment
# How??
# Open VS Code
# Navigate to the folder and open it 
# Open new terminal
# Create an environment: python -m venv venv
# Activate that environment: venv\Scripts\activate
# Now go ahead and install all necessary libraries and requirements



# Instruction Set  - 2 (Status Passed)

# Create a Project Directory
# Navigate to it using Anaconda Prompt
# Create a conda environment of the suitable python version
# Install required libraries using pip/conda
# Type to open spyder simply - spyder




#Importing Libraries


# pywhatkit is a Python library that offers various automation utilities,
# including sending WhatsApp messages at scheduled times, performing Google searches,
# playing YouTube videos, converting text into handwriting-style images,
# and retrieving Wikipedia summaries. 
import speech_recognition as sr 



# For Weather part
import requests
import json


#For text to speech 
import pyttsx3 


#For knowing the time and date
import datetime


#For retrieving info about a person from wiki
import wikipedia


# Other libs to import in time
# PyAudio

# PyWhatKit
# pywhatkit is a Python library that offers various automation utilities,
# including sending WhatsApp messages at scheduled times, performing Google searches,
# playing YouTube videos, converting text into handwriting-style images,
# and retrieving Wikipedia summaries. 
import pywhatkit

# PyJokes
import pyjokes


import sys


listner = sr.Recognizer()



engine = pyttsx3.init()

#Setting female voice of Alexa
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)

def engine_talk(text):
    engine.say(text)
    engine.runAndWait()

# engine.say("I am your bot")
# engine.say("How can i help you?")
# engine.runAndWait()


#We use OpenWeatherApp
def weather(city):
    # Enter your API key here 
    api_key = "8f4237930762f9a882f9311284d9ebaf"
    
    # base_url variable to store url 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Give city name 
    city_name = city
    
    # complete_url variable to store 
    # complete url address 
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
    
    # get method of requests module 
    # return response object 
    response = requests.get(complete_url) 
    
    # json method of response object  
    # convert json format data into 
    # python format data 
    x = response.json() 
    
    # Now x contains list of nested dictionaries 
    # Check the value of "cod" key is equal to 
    # "404", means city is found otherwise, 
    # city is not found 
    if x["cod"] != "404": 
    
        # store the value of "main" 
        # key in variable y 
        y = x["main"] 
    
        # store the value corresponding 
        # to the "temp" key of y 
        current_temperature = y["temp"] 
    
        # store the value corresponding 
        # to the "pressure" key of y 
        #current_pressure = y["pressure"] 
    
        # store the value corresponding 
        # to the "humidity" key of y 
        #current_humidiy = y["humidity"] 
    
        # store the value of "weather" 
        # key in variable z 
        #z = x["weather"] 
    
        # store the value corresponding  
        # to the "description" key at  
        # the 0th index of z 
        #weather_description = z[0]["description"]
        temp_in_celcius = current_temperature - 273.15
        return str(int(temp_in_celcius))
    
        # print following values 
        '''print(" Temperature (in kelvin unit) = " +
                        str(current_temperature) + 
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity (in percentage) = " +
                        str(current_humidiy) +
            "\n description = " +
                        str(weather_description)) 
    else: 
        print(" City Not Found ")
        '''


def user_commands():
    try:
        with sr.Microphone() as source:
            print("Start Speaking!!")
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                # print(command)
    except Exception as e:
        print(f"An error occurred: {e}")  # Print the specific error
        pass
    return command

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return int(celsius)


def run_alexa():
    command = user_commands()
    
    # If I want to play some music from Youtube
    if 'play' in command:
        song = command.replace('play', '')
        print('Playing' + command)
        engine_talk('Playing'+song)
        pywhatkit.playonyt(song)
    
    
    elif 'time' in command:
        # 24Hour format
        # time = datetime.datetime.now().strftime('%H:%M:%S')
        # AM or PM
        time = datetime.datetime.now().strftime('%I:%M:%p')
        engine_talk('The current time is' + time)
        
    elif 'who is' in command:
        name = command.replace('who is', '')
        info = wikipedia.summary(name, 1)
        print(info)
        engine_talk(info)
        
    elif 'joke' in command:
        joke = pyjokes.get_joke(language='en')
        print(joke)
        engine_talk(joke)
    elif 'weather' in command:
        engine_talk('Lemme know the city for which you are asking')
        city = user_commands()
        weather_api = weather(city)
        engine_talk(weather_api + 'degree celcius')  
    elif 'stop' in command:
        sys.exit()
    else:
        engine_talk('I could not hear you properly')


while True:
    run_alexa()













































































