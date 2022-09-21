from flask import Flask, request, json

app = Flask(__name__)

food = {"1": "apple", "2": "banana", "3": "cheery", "4": "pineapple"}


@app.route('/data', methods=['GET', 'POST'])
def api():
    if request.method == 'GET':
        return food
    if request.method == 'POST':
        data = request.json
        food.update(data)
        return 'data got inserted'


@app.route("/data/<id>", methods=['PUT'])
def update(id):
    data = request.form['item']
    food[str(id)] = data
    return 'data updated'


@app.route("/data/<id>", methods=["DELETE"])
def delete_Operation(id):
    food.pop(str(id))
    return 'data deleted'


if __name__ == '__main__':
    app.run(debug=True)
