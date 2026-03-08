"""
Flask Web Application for Quotes Recommendation Chatbot
Serves the chatbot web interface and communicates with the Rasa server.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """Serve the chatbot web interface."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
