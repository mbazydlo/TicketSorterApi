import unittest
from api import app
import json

class ResponseTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    # Testing is response 200
    def test_successful_response(self):
        tickets = json.dumps(
                            [{   
                                "id" : 1,
                                "start" : "Warszawa",
                                "finish": "Krakow",
                                "transport_number" : "T2464",
                                "mean_of_transport" : "train",
                                "seat_assigment" : "A34"
                            }]
                            )


        response = self.app.post('/tickets', headers={"Content-Type": "application/json"}, data=tickets)

        self.assertEqual(200, response.status_code)

    # Case of tickets with no connection.
    def test_ticket_without_connect(self):
        tickets = json.dumps(
                            [
                            {   
                                "id" : 1,
                                "start" : "Warszawa",
                                "finish": "Krakow",
                                "transport_number" : "T2464",
                                "mean_of_transport" : "train",
                                "seat_assigment" : "A34"
                            },
                            {   
                                "id" : 2,
                                "start" : "Poznan",
                                "finish": "Gdansk",
                                "transport_number" : "T2464",
                                "mean_of_transport" : "bus",
                                "seat_assigment" : "T24"
                            }
                            ]
                            )
    
        response = self.app.post('/tickets', headers={"Content-Type": "application/json"}, data=tickets)

        self.assertEqual('No tickets or tickets with no connection', response.json['response'])

    # Case of proper list - correct data.
    def test_correct_data(self):
        tickets = json.dumps([
                            { 
                             "id" : 1,
                                "start" : "Warszawa",
                                "finish": "Krakow",
                                "transport_number" : "123",
                                "mean_of_transport" : "train",
                                "seat_assigment" : "A34"
                            },
                            {   
                                "id" : 2,
                                "start" : "Gdansk",
                                "finish": "Poznan",
                                "transport_number" : "T2464",
                                "mean_of_transport" : "flight",
                                "seat_assigment" : "13C",
                                "baggage" : "345",
                                "gate" : "Z5"
                            },
                            {   
                                "id" : 3,
                                "start" : "Krakow",
                                "finish": "Gdansk",
                                "transport_number" : "T24",
                                "mean_of_transport" : "bus"
                            },
                            {
                                "id" : 4,
                                "start" : "Poznan",
                                "finish": "Berlin",
                                "transport_number" : "Z5730",
                                "mean_of_transport" : "flight",
                                "seat_assigment" : "25E",
                                "gate" : "Z5"
                            }])

        expected = [
                    "1. Take train 123 from Warszawa to Krakow. Sit in A34",
                    "2. Take bus T24 from Krakow to Gdansk. No seat assigned",
                    "3. From Gdansk, take flight T2464 to Poznan. Gate Z5. Seat 13C. Baggage drop at ticket counter 345.",
                    "4. From Poznan, take flight Z5730 to Berlin. Gate Z5. Seat 25E. Baggage will we automatically transferred from your last leg.",
                    "5. You have arrived at your final destination."
                    ]

        response = self.app.post('/tickets', headers={"Content-Type": "application/json"}, data=tickets)
        self.assertEqual(expected, response.json)

    # Case of empty list - no tickets.
    def test_empty_list_of_tickets(self):
        tickets = json.dumps([])
        response = self.app.post('/tickets', headers={"Content-Type": "application/json"}, data=tickets)

        self.assertEqual('No tickets or tickets with no connection', response.json['response'])