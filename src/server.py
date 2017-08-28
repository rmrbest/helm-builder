import os
from flask import Flask, request, jsonify
from src.services.QueueService import QueueService
from src.services.provider.RabbitMQStrategy import RabbitMQStrategy

app = Flask(__name__)
config = os.path.join(app.root_path, 'config/production.cfg')
app.config.from_pyfile(config)
service = QueueService(RabbitMQStrategy())


@app.route('/api/build', methods=['GET'])
def build():
    result = service.produce()
    return (jsonify(result.success,result.returnValues), 201)

if __name__ == '__main__':
    app.run(debug=True)

