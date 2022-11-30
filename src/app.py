from flask import Flask, jsonify, request, json
app = Flask(__name__)

todos =[
    {"label": "tomar aguita", "done": False},
    {"label": "tomas otra vez", "done": False},
    {"label": "tomas otra vez otra vez", "done": False}
]
@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_todos= json.loads(request_body)
    todos.append(decoded_todos)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    print("Incoming request with the following body", position)
    return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)