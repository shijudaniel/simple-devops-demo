from flask import Flask


app = Flask(__name__)

@app.route("/")
def home():
    return "HELLO .._.. DevOps Demo App Running! AGAIN ...-5-..."


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
    # app.run(host="0.0.0.0", port=5000) #not secure binds to ALL networks
