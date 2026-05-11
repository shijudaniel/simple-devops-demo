from flask import Flask


app = Flask(__name__)

@app.route("/")
def home():
    return "Hello... DevOps Demo App Running!"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
    #app.run(host="0.0.0.0", port=5000) #not secure binds to ALL networks, Docker
