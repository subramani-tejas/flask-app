from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def home():
    return '<h3> Scaler DevOps Bootcamp - Day 1 </h3>'


# run the app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
