def parse_emails(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    emails = content.split("---")
    parsed = []

    for email in emails:
        if "Subject:" in email:
            lines = email.strip().split("\n")
            subject = lines[0].replace("Subject:", "").strip()
            body = " ".join(lines[1:]).strip()

            parsed.append({
                "subject": subject,
                "body": body
            })

    return parsed