from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>🔥 Auto Deployment V3 🔥</h1>
    <p>Now CI/CD is perfectly working!</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
