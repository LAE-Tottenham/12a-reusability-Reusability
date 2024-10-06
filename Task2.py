import requests
from pyfiglet import Figlet
import os, time

# Help! I'm trying to make this cool bot but my code is too messy :( Please help me organise it into reusable components.

# Define your reusable functions here:
#guess_gender, postcode_information,weather,get_cat_fact,message,weird_weather_bot
# Make sure each function only does ONE thing!!!!!!!!!!!

def guess_gender(name):
    gender_resp = requests.get(f"https://api.genderize.io/?name={name}").json()
    gender = gender_resp["gender"]
    prob_percent = gender_resp["probability"] * 100
    return [gender, prob_percent]

###########################################

def postcode_information(postcode):
    postcode_resp = requests.get(f"https://api.postcodes.io/postcodes/{postcode_raw}").json()
    result = postcode_resp['result']
    return result['admin_ward'], result['longtitude'], result['latitude']

def weather(latitude,longtitude):
    weather_resp = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=4d30afa58f6f935d861edecad3639cda").json()
    kelvin = weather_resp["main"]["temp"]
    degrees = int(kelvin - 273.15)
    main_weather = weather_resp["weather"][0]["main"]
    second_weather = weather_resp["weather"][0]["description"]
    return degrees, main_weather, second_weather

def  get_cat_fact():
    joke_resp = requests.get("https://catfact.ninja/fact").json()
    return joke_resp['fact']

def message():
    f = Figlet(font="slant")
    print(f.renderText("HEY!"))

    print("Welcome to the weird weather bot :)")
    print("-----------------------------------\n")

def weird_weather_bot():
    message()
    name = input("May I take your first name please? ")
    gender, prob_percent = guess_gender(name)
    print(f"\nHmmm, I'm {prob_percent}% sure you are a {gender}.")
    gender_correct = input("Am I right? :) (Y/n)")
    if gender_correct.lower() in ["", "yes", "y", "ye"]:
        print("Wooooooh! Computer 1, Human 0.")
    else:
        print("Ahhhh, sorry! :(")
    
    postcode_raw = input("/nso, what's your postcode? ")
    area,longtitude,latitude = postcode_information(postcode_raw)
    print(f"Nice! so you live in {area}.\n")
    print("Let me just check the weather there today...\n")

    for i in range(3):
        time.sleep(1)
        print("...")
    def yes_no():
        answer = input("\nWould you like a cat fact while you wait? ").strip().lower()
        if answer in ['yes', 'no']:
            return answer
        else:
            print("Please enter yes or no ")

    
    print("Doesn't matter what you think, I'm going to give you one anyway :)")
    time.sleep(3)
    joke=get_cat_fact()
    print("\n###########################")
    print("CAT FACT:")
    print(f"\n{joke}\n")
    print("So interesting isn't it!")
    print("###########################")

    print("\nWaiting 5 seconds for you to read the fact...")
    time.sleep(5)
    print("\nNow, back to getting the weather...")

    for i in range(3):
        time.sleep(1)
        print("...")

    degrees, main_weather, second_weather = weather(latitude,longtitude)
    print(f"\nThe weather in {area}:\n")
    print(str(weather_degrees) + "℃")
    print(f"{main_weather_desc} - {second_weather_desc}")
    print("\nThank you! Bye.")

    if name == "main":
        main()



# After you have written the reusable functions, answer the following:
# Questions:
# 1. What are the preconditions for your code not to break?
#The user's answer to whether they want a cat fact or not should only be yes or no

# 2. Validate the user's input based on your preconditions.
#def yes_no():
        #answer = input("\nWould you like a cat fact while you wait? ").strip().lower()
        #if answer in ['yes', 'no']:
        #   return answer
        #else:
        #  print("Please enter yes or no ")

# 3. Why was it useful to use reusable components in this case? Please mention at least 2 reasons and don't forget to contextualise.
# It was useful to use reusable components as it was easier to understand the code as the functions, guess_gender, postcode_information,weather,get_cat_fact,message,weird_weather_bot all do different things
#Also, I was able to use the functions i created multiple times


# Further Tasks:
# 1. Put your functions in seperate appropriate files and import them in.
# 2. Make sure all of your functions (except the main one) only do ONE thing or process.
# 3. Add your own twist to the code.

# Extension:
# Add the following apis as reusable components and use them in your code:
# https://www.exchangerate-api.com/docs/overview
