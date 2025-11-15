from flask import Flask
import config

app = Flask(__name__)

@app.route("/")
def home():
    return f"Hello from Flask demo. API_TOKEN={config.API_TOKEN}"

if __name__ == "__main__":
    app.run(port=5000)
