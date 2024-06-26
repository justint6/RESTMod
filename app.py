from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_swagger_ui import get_swaggerui_blueprint
import json
import os

app = Flask(__name__)
api = Api(app)

# Define a sample resource
class HelloWorld(Resource):
    def get(self):
        return jsonify({'message': 'Hello, World!'})

class DeviceValue:
  def __init__(self, address, value):
    self.value = value
    self.address = address


# Add the resource to the API
api.add_resource(HelloWorld, '/hello')


# Configure Swagger UI
SWAGGER_URL = '/swagger'
API_URL = './swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Sample API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/swagger.json')
def swagger():
    with open('swagger.json', 'r') as f:
        return jsonify(json.load(f))

incomes = [
    { 'description': 'salary', 'amount': 5000 }
]

@app.route('/incomes')
def get_incomes():
    return jsonify(incomes)

@app.route('/incomes', methods=['POST'])
def add_income():
    postdata = request.get_json()
    incomes.append(postdata)
    device1 = DeviceValue(postdata['description'], postdata['amount'])
    print(device1.value)
    print(device1.address)
    returnvalue = device1.value;
    return str(returnvalue) + ' ' + str(device1.address), 200

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port, host='0.0.0.0')
