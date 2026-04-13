import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from main import classify_email, route_email, detect_priority, generate_auto_reply
from logger import log_info, log_error

# Load environment configuration
load_dotenv()
API_KEY = os.getenv("API_KEY")

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    """Friendly welcome page for recruiters."""
    return jsonify({
        "status": "online",
        "message": "AI Email Automation Engine API is live!",
        "version": "2.0 Pro",
        "author": "Klarence Nevado",
        "usage": "Send a POST request to /process-email with a JSON body and x-api-key header."
    })

@app.route("/process-email", methods=["POST"])
def process_email():
    """
    Secured Webhook endpoint to process incoming emails in real-time.
    Requires 'x-api-key' header for authentication.
    """
    # 1. Security Check
    client_key = request.headers.get("x-api-key")
    if client_key != API_KEY:
        log_error("Unauthorized access attempt detected.")
        return jsonify({"error": "Unauthorized"}), 401

    # 2. Data Extraction
    data = request.json
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    subject = data.get("subject", "No Subject")
    body = data.get("body", "")

    # 3. Execution (Pro-Grade Triage Logic)
    email_obj = {"subject": subject, "body": body}
    
    category = classify_email(email_obj)
    team = route_email(category)
    priority = detect_priority(email_obj)
    reply = generate_auto_reply(category, priority)

    result = {
        "subject": subject,
        "category": category,
        "priority": priority,
        "assigned_to": team,
        "auto_reply_draft": reply,
        "status": "COMPLETED"
    }

    # 4. Observability (Logging)
    log_info(f"PROCESSED: {subject} -> {team} ({priority})")

    return jsonify(result)

if __name__ == "__main__":
    log_info("Starting Production-Grade Email Automation API...")
    # Bind to 0.0.0.0 and use dynamic PORT for cloud deployment (Render/Heroku)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
