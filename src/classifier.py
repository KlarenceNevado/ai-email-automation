def classify_email(email):
    """
    Simulated AI classification logic. 
    Matches subject and body to categories.
    """
    text = (email["subject"] + " " + email["body"]).lower()

    if "order" in text:
        return "Order Inquiry"
    elif "damaged" in text or "unacceptable" in text:
        return "Complaint"
    elif "help" in text or "reset" in text:
        return "Support Request"
    else:
        return "General Inquiry"

def route_email(category):
    """Routes category to internal department identifiers."""
    mapping = {
        "Order Inquiry": "sales_team",
        "Complaint": "support_team",
        "Support Request": "tech_team",
        "General Inquiry": "general"
    }
    return mapping.get(category, "general")

def detect_priority(email):
    """
    Analyzes urgency based on professional keywords.
    Returns: High, Medium, or Low.
    """
    text = (email["subject"] + " " + email["body"]).lower()
    high_urgency = ["urgent", "asap", "emergency", "broken", "critical"]
    medium_urgency = ["soon", "status", "cancel", "delay"]

    if any(word in text for word in high_urgency):
        return "High"
    elif any(word in text for word in medium_urgency):
        return "Medium"
    else:
        return "Low"

def generate_auto_reply(category, priority):
    """Generates a professional auto-reply template based on triage results."""
    replies = {
        "Order Inquiry": "we've received your order inquiry. Our sales team is reviewing the details.",
        "Complaint": "we are sorry to hear about your experience. A support specialist has been assigned to resolve this.",
        "Support Request": "your technical request has been logged. Our engineers are investigating.",
        "General Inquiry": "thank you for reaching out. We will get back to you soon."
    }
    
    base_reply = f"Hello, {replies.get(category)}"
    if priority == "High":
        base_reply += " Since this is marked as High priority, we are fast-tracking your request."
    
    return base_reply