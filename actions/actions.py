# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List

import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


# Checks if the answer is cough or fever, otherwise recommends to go to the hospital
class ActionProvideAdvice(Action):

    def name(self) -> Text:
        return "action_provide_advice"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        symptom = tracker.get_slot('symptom')

        if symptom == "cough":
            dispatcher.utter_message(template="utter_recommend_medicine")
        elif symptom == "fever":
            dispatcher.utter_message(template="utter_recommend_doctor")
        else:
            dispatcher.utter_message(
                text="Mmh... I don't know that one. It is probably better for you to go to the hospital!")

        return []


class ActionProvideWeatherForecast(Action):

    def name(self) -> Text:
        return "action_provide_weather_forecast"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city = tracker.get_slot('city')
        api_key = "9de2c0d3a8ba2ab4dcfcc7cee516a701"
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")

        if response.status_code == 200:
            data = response.json()
            temperature = data["main"]["temp"] - 275
            weather = data["weather"][0]["description"]
            dispatcher.utter_message(text=f"The current temperature in {city} is {temperature:.2f}°C. You can expect {weather}")
        else:
            dispatcher.utter_message(text=f"Couldn't retrieve the weather for {city}. Please try again.")

        return []

