# TRIP SORTER


Content of challenge:

TRIP SORTER

You are given a stack of boarding cards for various transportations that will take you from
point A to point B via several stops on the way. All of the boarding cards are out of order and
you don't know where your journey starts, nor where it ends. Each boarding card contains
information about seat assignment, and means of transportation (such as flight number, bus
number, etc).
Write an API that lets you sort this kind of list and present back a description of how to
complete your journey.
For instance, the API should be able to take an unordered set of boarding cards, provided in
a format defined by you, and produce this list:

1. Take train 78A from Madrid to Barcelona. Sit in seat 45B.
2. Take the airport bus from Barcelona to Girona Airport. No seat assignment.
3. From Girona Airport, take flight SK455 to Stockholm. Gate 45B, seat 3A.
Baggage drop at ticket counter 344.
4. From Stockholm, take flight SK22 to New York JFK. Gate 22, seat 7B.
Baggage will we automatically transferred from your last leg.
5. You have arrived at your final destination.

The list should be defined in a format that's compatible with the input format.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
See deployment for notes on how to deploy the project on a live system.

### Prerequisites

**Without Docker:**

Get into flask project folder:

```
cd .../ecumene_test/flask
```

Create virtual venv based on requirements.txt file:


*On Linux:*
```
python3 -m venv venv
```

*On Windows:*
```
py -m venv env
```



Activate venv:

*On Linux:*
```
source /venv/bin/activate
```

*On Windows:*
```
.\env\Scripts\activate
```



Install libraries (inside virtual enviroment):

```
pip install -r requirements.txt
```


**With Docker:**

Create virtual enviroment from 'Without Docker' step.

If you don't already have a Docker you can get it from:
[Docker Docs](https://docs.docker.com/) - Official website of Docker.

Install uWSGI (inside virtual enviroment):
```
pip install flask uwsgi
```

### Runnning App
**Without Docker:**

# Run app (inside virtual enviroment)
```
python api.py
```

**With Docker:**

Build docker-compose (inside main folder 'ecumene_test/')
```
docker-compose build
```

Run docker-compose:
```
docker-compose up
```

### Running tests

To run tests get into 'ecumene_test/flask/' and give a command:
```
python -m unittest -v tests\test_response.py
```






