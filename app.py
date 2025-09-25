
import os
from flask import Flask, jsonify
from datetime import datetime
import time

app = Flask(__name__)

# Configuration
PORT = int(os.environ.get('PORT', {{ values.port }}))
start_time = time.time()

@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome to {{ values.repoName }}',
        'description': '{{ values.description }}',
        'version': '1.0.0',
        'timestamp': datetime.now().isoformat()
    })


@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'uptime': time.time() - start_time
    }), 200

@app.route('/ready')
def ready():
    # Add any readiness checks here (database connections, external services, etc.)
    return jsonify({
        'status': 'ready',
        'timestamp': datetime.now().isoformat()
    }), 200


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'error': 'Route not found',
        'timestamp': datetime.now().isoformat()
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'error': 'Internal server error',
        'timestamp': datetime.now().isoformat()
    }), 500

if __name__ == '__main__':
    print(f"{{ values.repoName }} is starting on port {PORT}")
    print(f"Health check: http://localhost:{PORT}/health")
    
    print(f"Readiness check: http://localhost:{PORT}/ready")
    
    
    app.run(
        host='0.0.0.0',
        port=PORT,
        debug=os.environ.get('FLASK_ENV') == 'development'
    )

