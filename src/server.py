from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/build', methods=['POST'])
def build():
    
    return (jsonify({'username': 'OK'}), 201)


if __name__ == '__main__':
    app.run(debug=True)


