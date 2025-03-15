from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook_handler():
    if request.method == 'POST':
        data = request.get_json()
        print("Received data:", data)
        return jsonify({'status': 'success'}), 200
    else:
        return 'Method not allowed', 405

if __name__ == '__main__':
    app.run(debug=True, port=5000)