from flask import Flask, jsonify, request
import json
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data#recibo la data
    print("Incoming request with the following body", request_body)
    decoded_object = json.loads(request_body)#convertimos la data a formato que python lo pueda trabajar(en un diccionario)
    print(decoded_object)
    todos.append(decoded_object)#como un push añado la nueva data
    return jsonify(todos),200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    print('antes de remove',todos)
    todos.pop(position)
    print('despues de remove',todos)
    return 'something'



# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)