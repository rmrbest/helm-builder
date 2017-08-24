from flask import Flask, request, jsonify

from src.services import QueueService

app = Flask(__name__)

@app.route('/api/build', methods=['POST'])
def build():
    queueService = QueueService
    queueService.produce()
    return (jsonify({'username': 'OK'}), 201)


if __name__ == '__main__':
    app.run(debug=True)


