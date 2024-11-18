from flask import Flask, jsonify
import os

app = Flask(__name__)

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'success',
        'message': 'Backend is up and running'
    }), 200

# Sample API endpoint
@app.route('/api/greet', methods=['GET'])
def greet():
    # You can use an environment variable to customize the greeting message
    greeting = os.getenv("GREETING", "Hello, World!")
    return jsonify({
        'message': greeting
    }), 200

# Main entry point
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

