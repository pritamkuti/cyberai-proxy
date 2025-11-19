from flask import Flask, render_template, request, jsonify
from google import genai
from datetime import datetime

app = Flask(__name__)

GENIE_API_KEY = "AIzaSyB12M3tR7J9R9HoHKB9SHwbEJHf2I4pM10"
client = genai.Client(api_key=GENIE_API_KEY)

def ask_gemini(question):
    """Call Gemini API via genai with cybersecurity expertise emphasis"""
    prompt = f"""
You are a cybersecurity expert AI assistant. Answer all questions in a short and concise manner.

Question: {question}
"""
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        print("Gemini API error:", e)
        return "Sorry, I cannot process your request now."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question", "").strip()
    timestamp = datetime.now().strftime("%H:%M")

    if not question:
        return jsonify({"answer": "Please type a question.", "time": timestamp})

    answer = ask_gemini(question)
    return jsonify({"answer": answer, "time": timestamp})

if __name__ == "__main__":
    app.run(debug=True)