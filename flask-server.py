from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/api/data', methods=['GET'])

def get_data():
    data = {'message': 'This is JSON data from the API'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
    
