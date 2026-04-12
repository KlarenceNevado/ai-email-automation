def classify_email(email):
    """
    Simulated AI classification logic. 
    This is structured to be AI-ready and can be easily swapped 
    for a real LLM API (OpenAI/Claude) in the future.
    """
    # Combine subject and body for context-aware classification
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
    if category == "Order Inquiry":
        return "sales_team"
    elif category == "Complaint":
        return "support_team"
    elif category == "Support Request":
        return "tech_team"
    else:
        return "general"