from flask import Flask, request, jsonify
from src.services.QueueService import QueueService
from src.services.provider.RabbitMQStrategy import RabbitMQStrategy

app = Flask(__name__)
service = QueueService(RabbitMQStrategy())

@app.route('/api/build', methods=['POST'])
def build():
    return (jsonify({'username': 'OK'}), 201)


if __name__ == '__main__':
    app.run(debug=True)


