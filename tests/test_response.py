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

        self.assertEqual('Wrong tickets', response.json['response'])