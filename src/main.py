from parser import parse_emails
from classifier import classify_email, route_email
import json
import os

# Ensure data directory exists
os.makedirs("data", exist_ok=True)

emails = parse_emails("data/emails.txt")
processed_emails = []

for email in emails:
    # Get classification and routing
    category = classify_email(email)
    team = route_email(category)

    email_data = {
        "subject": email["subject"],
        "body": email["body"],
        "category": category,
        "assigned_to": team
    }

    processed_emails.append(email_data)
    print(f"[ROUTED] {email['subject']} -> {team}")

# Save the structured output
output_path = "data/processed_emails.json"
with open(output_path, "w") as file:
    json.dump(processed_emails, file, indent=4)

def simulate_action(email):
    print(f"Sending '{email['subject']}' to {email['assigned_to']}...\n")

# Execute final system actions
print("\n--- Executing System Actions ---")
for email in processed_emails:
    simulate_action(email)

print(f"Success! Data saved to {output_path}")