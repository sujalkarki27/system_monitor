from flask import Flask, jsonify, render_template
import psutil

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/system', methods=['GET'])
def get_system_stats():
    return jsonify({
        "cpu": psutil.cpu_percent(interval=1),
        "ram": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent
    })

if __name__ == '__main__':
    app.run(debug=True)
