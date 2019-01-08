from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

task=[
    { "request" : "1",
      "temperature" : "20",
      "humidity" : "23",
      "distance" : "200m",
      "obstacle" : "false"
        }]
@app.route('/', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': task})

@app.route('/move', methods=['POST'])
def create_task():
    print(request.is_json)
    content = request.get_json()
    print("request is "+content['request']+" and angle is  "+content['angle'])
    return "data received"


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
