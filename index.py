from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    return jsonify({"reply": f"You said: {message}"})

# Vercel looks for "app"
if __name__ == "__main__":
    app.run()
