# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction


class ValidateFormAction(FormValidationAction):

    def name(self) -> Text:
        return "validate_details_form"

    # def run(self, dispatcher: CollectingDispatcher,
    #         tracker: Tracker,
    #         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
    #             dispatcher.utter_message(text="Hello World!")

    #             return []

    def validate_username( self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    )-> Dict[Text, Any]:
        # username = tracker.get_slot("username")
        if username is not None:
            # dispatcher.utter_message(response="utter_ask_username")
            print("Gitcha")
            return {"username": value}
            
        else:
            dispatcher.utter_message(response="utter_wrong_username")
            return {"username": value}
         

    
    def validate_mobilenumber( self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    )-> Dict[Text, Any]:
        # mobilenumber = tracker.get_slot("mobilenumber")
        if mobilenumber is not None:
            # returned_slots = {"mobilenumber": value}
            # dispatcher.utter_message(response="utter_ask_mobilenumber")
            print("hello")
            return{"mobilenumber": value}
            
        else:
            # returned_slots = {REQUESTED_SLOT: mobilenumber}
            dispatcher.utter_message(response="utter_wrong_mobilenumber")
            return {"mobilenumber": value}
 

    def validate_address( self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    )-> Dict[Text, Any]:
        address = tracker.get_slot("address")
        if address is not None:
            dispatcher.utter_message(response="utter_ask_address")
            # returned_slots = {"mobilenumber": value}
            return{"address": value}
        else:
            dispatcher.utter_message(response="utter_wrong_address")
            return {"address":  value}

    def validate_pincode( self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    )-> Dict[Text, Any]:                                        
        pincode = tracker.get_slot("pincode")
        if pincode is not None:
            # returned_slots = {"mobilenumber": value}
            
            dispatcher.utter_message(response="utter_ask_pincode")
            return{"pincode": value}
        else:
            dispatcher.utter_message(response="utter_wrong_pincode")
            return{"pincode": value}

    

    