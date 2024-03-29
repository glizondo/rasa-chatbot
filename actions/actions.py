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
        elif genre == "Sci-fi":
            dispatcher.utter_message(text="Got it. Booking a flight from O'Hare Airport.")
        else:
            dispatcher.utter_message(
                text="Sorry, I don't have that city and its airports in my database.")

        return []