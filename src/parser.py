import os
import logging

def parse_emails(file_path):
    """
    Parses raw email text into a list of structured dictionaries.
    Includes error handling for missing files or malformed data.
    """
    if not os.path.exists(file_path):
        logging.error(f"Input file not found: {file_path}")
        return []

    try:
        with open(file_path, "r") as file:
            content = file.read()

        if not content.strip():
            logging.warning(f"File {file_path} is empty.")
            return []

        emails = content.split("---")
        parsed = []

        for index, raw_email in enumerate(emails):
            if "Subject:" in raw_email:
                lines = raw_email.strip().split("\n")
                subject = lines[0].replace("Subject:", "").strip()
                body = " ".join(lines[1:]).strip()

                parsed.append({
                    "id": index + 1,
                    "subject": subject,
                    "body": body
                })
        
        return parsed

    except Exception as e:
        logging.error(f"Error parsing emails: {str(e)}")
        return []