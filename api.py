from flask import Flask, jsonify, request
from sorter import Sorter

app = Flask(__name__)

@app.route('/tickets', methods=['POST'])
def sendTickets():
    ticket_unsorted = request.get_json()
    path = Sorter(ticket_unsorted).printNiceTickets()

    if path:
        return jsonify(path)
    else:
        return jsonify({'response': 'No tickets or tickets with no connection'})
    
if __name__ == '__main__':
    app.run(debug=True)