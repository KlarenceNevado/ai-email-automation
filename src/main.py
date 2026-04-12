import json
import os
import logging
from datetime import datetime
from parser import parse_emails
from classifier import classify_email, route_email, detect_priority, generate_auto_reply

# Configure Logging for System Observability
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class EmailAutomationEngine:
    """
    A professional-grade automation engine that processes, 
    classifies, and triages incoming emails.
    """
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.processed_data = []
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

    def run_pipeline(self):
        """Executes the full automation lifecycle."""
        logging.info("Initializing Email Automation Pipeline v2.0...")
        
        # 1. Parsing
        emails = parse_emails(self.input_file)
        if not emails:
            logging.warning("No emails found to process. Exiting.")
            return

        # 2. Triage & Enrichment
        for email in emails:
            category = classify_email(email)
            team = route_email(category)
            priority = detect_priority(email)
            reply = generate_auto_reply(category, priority)

            enriched_data = {
                "id": email.get("id"),
                "subject": email["subject"],
                "category": category,
                "priority": priority,
                "assigned_to": team,
                "auto_reply_draft": reply,
                "processed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "status": "COMPLETED"
            }

            self.processed_data.append(enriched_data)
            logging.info(f"Processed: '{email['subject']}' -> {team} ({priority})")

        # 3. Persistence
        self._save_results()
        
        # 4. Action Simulation
        self._simulate_actions()

    def _save_results(self):
        """Saves processed emails incrementally to JSON."""
        with open(self.output_file, "w") as file:
            json.dump(self.processed_data, file, indent=4)
        logging.info(f"System results saved to: {self.output_file}")

    def _simulate_actions(self):
        """Simulates final system actions like response sending."""
        print("\n" + "="*50)
        print("STARTING: EXECUTING FINAL AUTOMATION ACTIONS")
        print("="*50)
        
        for email in self.processed_data:
            print(f"[{email['priority']}] Sending triage update for '{email['subject']}'")
            print(f"Draft: {email['auto_reply_draft']}\n")
        
        print("="*50)
        print("SUCCESS: Automation Cycle Complete.")

if __name__ == "__main__":
    engine = EmailAutomationEngine(
        input_file="data/emails.txt",
        output_file="data/processed_emails.json"
    )
    engine.run_pipeline()