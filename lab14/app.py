from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

items = {}

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/items', methods = ["POST"])
def create_item():
    data = request.get_json()
    item_id = str(len(items)+1)
    items[item_id] = data
    return jsonify({"id" : item_id, "item" : data}), 201
@app.route('/items', methods = ["GET"])
def get_items():
    return jsonify(items)
@app.route('/items/<item_id>', methods = ['GET', 'PUT', 'DELETE'])
def handle_item(item_id):
    item = items.get(item_id)
    if request.method == 'GET':
        if not item:
            return jsonify({'Error' : 'Item not found'}), 404

        return jsonify(item)
    elif request.method == 'PUT':
        if not item:
            return render_template('error.html', message = "NOT FOUND"), 404
        data = request.get_json()
        if not data: 
            return jsonify({'error' : 'Invalid input'})
        items[item_id] = data
        return render_template('update.html', item_id = item_id, item = data)

    elif request.method == "DELETE":
        deleted_item = items.pop(item_id)
        return render_template('delete.html', item_id = item_id,
        deleted_item = deleted_item)
    

if __name__ == "__main__":
    app.run(debug=True)