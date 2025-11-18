from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "AIzaSyB12M3tR7J9R9HoHKB9SHwbEJHf2I4pM10"  # Replace with your actual API key
MODEL = "gemini-2.5-flash"

@app.route('/proxy', methods=['POST'])
def proxy():
    # Get the incoming request data (the user message)
    user_input = request.get_json()

    # Google API URL
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

    # Make a POST request to Google API with the user input
    response = requests.post(url, json=user_input)

    # If the response is OK, return it to InfinityFree
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Error contacting Google API."}), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=10000)
