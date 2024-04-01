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
            dispatcher.utter_message(
                text=f"The current temperature in {city} is {temperature:.2f}°C. You can expect {weather}")
        else:
            dispatcher.utter_message(text=f"Couldn't retrieve the weather for {city}. Please try again.")

        return []


class ActionRecomendBook(Action):

    def name(self) -> Text:
        return "action_recomend_book"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        genre = tracker.get_slot('genre')

        if genre == "Fantasy":
            dispatcher.utter_message(text="You might like The Dark Tower by Stephen King")
        elif genre == "Sci-fi":
            dispatcher.utter_message(text="You might like Dune by Frank Herbert")
        else:
            dispatcher.utter_message(
                text="Sorry, I can't think of any books at the moment.")

        return []


class ActionBookFlight(Action):

    def name(self) -> Text:
        return "action_book_flight"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city = tracker.get_slot('city')

        if city == "Grand Rapids":
            dispatcher.utter_message(text="Got it. Booking a flight from GRR Airport.")
        elif city == "Chicago":
            dispatcher.utter_message(text="Got it. Booking a flight from O'Hare Airport.")
        else:
            dispatcher.utter_message(
                text="Sorry, I don't have that city and its airports in my database.")

        return []


class ActionOfferHelp(Action):

    def name(self) -> Text:
        return "action_provide_solution"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        issue = tracker.get_slot('issue')

        if issue == "Monitor":
            dispatcher.utter_message(text="Try unplugging and replugging the monitor cables")
        else:
            dispatcher.utter_message(
                text="Sorry, I don't know how to fix that issue.")

        return []


class ActionCreatePattern(Action):

    def name(self) -> Text:
        return "action_pattern"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        pattern = tracker.get_slot('pattern')

        dispatcher.utter_message(text=f"{pattern}{pattern}")

        return []


class ActionRequestSandwich(Action):

    def name(self) -> Text:
        return "action_provide_sandwich"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        sandwich = tracker.get_slot('sandwich')

        if sandwich == "turkey":
            dispatcher.utter_message(text="A slice of Turkey, cheese, and mayonnaise on white bread")
        else:
            dispatcher.utter_message(
                text="Sorry, I don't know that type of sandwich")

        return []
