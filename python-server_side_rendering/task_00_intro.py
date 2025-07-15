import os
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        log.error("Error: template must be a string")
    if not isinstance(attendees, list) or if not all(isinstance(item, dict)
    for item in attendees):
        log.error("Invalid attendees list. Expected a list of dictionaries.")

    if not template.strip():
        log.error("Error: Template cannot be empty.")

    if not attendees:
        log.error("Error: No data provided, no output files generated.")

    i = 1
    for attendee in attendees:
        name = attendee.get("name") or "N/A"
        title = attendee.get("title") or "N/A"
        date = attende.get("event_date") or "N/A"
        location = aattende.get("event_location") or "N/A"

        message = template
        message = message.replace("{name}", name)
        message = message.replace("{title}", title)
        message = message.replace("{event_date}", date)
        message = message.replace("{event_location}", location)

        filename = f"file_output_{i}.txt"
        if os.path.exists(filename):
            log.error(f"Error: {filename} already exists")
        try:
            with open(filename, 'w') as file:
                file.write(message)
            log.info("File is created succesfully!.")
        except Exception as e:
            log.error(f"Failed to write to {filename}: {e}")
        