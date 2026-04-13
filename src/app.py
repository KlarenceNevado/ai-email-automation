from flask import Flask, request, jsonify
from main import classify_email, route_email, detect_priority, generate_auto_reply

app = Flask(__name__)

@app.route("/process-email", methods=["POST"])
def process_email():
    """
    Webhook endpoint to process incoming emails in real-time.
    Expects JSON: {"subject": "...", "body": "..."}
    """
    data = request.json
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    subject = data.get("subject", "No Subject")
    body = data.get("body", "")

    # Create the internal email object required by the classifier
    email_obj = {
        "subject": subject,
        "body": body
    }

    # Execute Pro-Grade Triage Logic
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

    # Log action to console for observability
    print(f"[API] Processed: '{subject}' -> {team} ({priority})")

    return jsonify(result)

if __name__ == "__main__":
    # Running in debug mode for development as requested
    app.run(host="127.0.0.1", port=5000, debug=True)
