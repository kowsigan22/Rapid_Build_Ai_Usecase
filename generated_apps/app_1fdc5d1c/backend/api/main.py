from flask import Flask, jsonify, request
app = Flask(__name__)
@app.route('/items', methods=['GET'])
def get_items():
    return {'items': []}
@app.route('/items', methods=['POST'])
def post_item():
    data = request.get_json()
    with open('backend/db/items.json', 'a') as f:
        json.dump(data, f)
    return jsonify({'item': data})
if __name__ == '__main__':
    app.run(port=8000)
