from flask import Flask, request, jsonify
import redis

app = Flask(__name__)
db = redis.Redis(host='redis', port=6379)

@app.route('/api/create', methods=['POST'])
def create():
    data = request.get_json()

    if data is None or 'key' not in data or 'value' not in data:
        return jsonify({'error': 'invalid data'}), 400

    key = data['key']
    value = data['value']

    db.set(key, value)

    return jsonify({'success': True})

@app.route('/api/get', methods=['GET'])
def get():
    key = request.args.get('key')

    if key is None:
        return jsonify({'error': 'empty key'}), 400

    value = db.get(key)

    if value is None:
        return jsonify({'error': 'key not found'}), 404

    return jsonify({'key': key, 'value': value.decode()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
