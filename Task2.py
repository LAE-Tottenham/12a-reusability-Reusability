import requests
from pyfiglet import Figlet
import os, time

# Help! I'm trying to make this cool bot but my code is too messy :( Please help me organise it into reusable components.

# Define your reusable functions here:
def print_header():
  f = Figlet(font="slant")
  print(f.renderText("HEY!"))
  print("Welcome to the weird weather bot :)")
  print("-----------------------------------\n")


def get_user_name():
    return input("May I take your first name please? ")


def guess_gender(name): 
    gender_resp = requests.get(f"https://api.genderize.io/?name={name}").json()
    gender = gender_resp["gender"]
    prob_percent = gender_resp["probability"] * 100
    return [gender, prob_percent]


def get_user_postcode():
  return input("\nSo, what's your postcode? ")

def get_location_details(postcode):
    postcode_resp = requests.get(f"https://api.postcodes.io/postcodes/{postcode}").json()
    return {
        'area': postcode_resp['result']['admin_ward'],
        'longitude': postcode_resp['result']['longitude'],
        'latitude': postcode_resp['result']['latitude']
        }
 
def print_location(location_details):
   print(f"Nice! so you live in {location_details['area']}.\n")

def get_weather_data(latitude, longitude):
    weather_resp = requests.get(
      f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=4d30afa58f6f935d861edecad3639cda"
  ).json()
    return weather_resp

def format_weather_data(weather_data):
  weather_kelvin = weather_data["main"]["temp"]
  weather_degrees = int(weather_kelvin - 273.15)
  main_weather_desc = weather_data["weather"][0]["main"]
  second_weather_desc = weather_data["weather"][0]["description"]
  return {
    'temperature': str(weather_degrees) + "℃",
    'description': f"{main_weather_desc} - {second_weather_desc}"
  }

def print_weather(weather_details, area):
  print(f"\nThe weather in {area}:\n")
  print(weather_details['temperature'])
  print(weather_details['description'])

def get_cat_fact():
  joke_resp = requests.get("https://catfact.ninja/fact").json()
  return joke_resp['fact']

def print_cat_fact(cat_fact):
  print("\n###########################")
  print("CAT FACT:")
  print(f"\n{cat_fact}\n")
  print("So interesting isn't it!")
  print("###########################")

  
 
# Make sure each function only does ONE thing!!!!!!!!!!!

###########################################

def weird_weather_bot():
  print_header()
  name = get_user_name()
  gender_result = guess_gender(name)
  gender = gender_result[0]
  prob_percent = gender_result[1]
  print(f"\nHmmm, I'm {prob_percent}% sure you are a {gender}.")
  gender_correct = input("Am I right? :) (Y/n)")
  if gender_correct.lower() in ["", "yes", "y", "ye"]:
    print("Wooooooh! Computer 1, Human 0.")
  else:
    print("Ahhhh, sorry! :(")
  postcode = get_user_postcode()
  location_details = get_location_details(postcode)
  print_location(location_details)
  print("Let me just check the weather there today...\n")
  for i in range(3):
    time.sleep(1)
    print("...")
  input("\nWould you like a cat fact while you wait? ")
  print("Doesn't matter what you think, I'm going to give you one anyway :)")
  time.sleep(3)
  cat_fact = get_cat_fact()
  print_cat_fact(cat_fact)
  print("\nWaiting 5 seconds for you to read the fact...")
  time.sleep(5)
  print("\nNow, back to getting the weather...")
  for i in range(3):
    time.sleep(1)
    print("...")
  weather_data = get_weather_data(location_details['latitude'], location_details['longitude'])
  weather_details = format_weather_data(weather_data)
  print_weather(weather_details, location_details['area'])
  print("\nThank you! Bye.")

weird_weather_bot()


# After you have written the reusable functions, answer the following:

# Questions:

# 1. What are the preconditions for your code not to break?

# The user's input must be a valid name and postcode


# 2. Validate the user's input based on your preconditions.

# By using the functions get_user_name and get_suer_postcode, the inputs can be checked to see if the are valid.
# A while loop could be used


# 3. Why was it useful to use reusable components in this case? Please mention at least 2 reasons and don't forget to contextualise.

#The code is more compact and easier to read.
# Each function has a specific purpose, making the code easier to understand and maintain.




# Further Tasks:
# 1. Put your functions in seperate appropriate files and import them in.
# 2. Make sure all of your functions (except the main one) only do ONE thing or process.
# 3. Add your own twist to the code.

# Extension:
# Add the following apis as reusable components and use them in your code:
# https://www.exchangerate-api.com/docs/overview
