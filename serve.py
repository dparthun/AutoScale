from flask import Flask, request, jsonify
import socket
import subprocess

app = Flask(__name__)

# Route to handle POST requests
@app.route('/', methods=['POST'])
def handle_post():
    # Launch the stress_cpu.py script in a separate process
    subprocess.Popen(["python3", "stress_cpu.py"])
    return jsonify(success=True), 200

# Route to handle GET requests
@app.route('/', methods=['GET'])
def handle_get():
    # Get the private IP address of the EC2 instance
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
