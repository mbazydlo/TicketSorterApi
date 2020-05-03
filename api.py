from flask import Flask, jsonify, request
from sorter import Sorter

app = Flask(__name__)

@app.route('/tickets', methods=['POST'])
def sendTickets():
    ticket_unsorted = request.get_json()

    
if __name__ == '__main__':
    app.run(debug=True)