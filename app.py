from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>🚀 Project 2 Deployed Successfully</h1>
    <p>CI/CD is working perfectly!</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
