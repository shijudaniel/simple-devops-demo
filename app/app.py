from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    user_input = request.args.get("input")
    eval(user_input)
    return "Unsafe Code"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)