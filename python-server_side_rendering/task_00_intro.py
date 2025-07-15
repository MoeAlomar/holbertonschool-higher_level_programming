import os
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        logging.error("Error: template must be a string")
        return

    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        logging.error("Invalid attendees list. Expected a list of dictionaries.")
        return

    if not template.strip():
        logging.error("Error: Template cannot be empty.")
        return

    if not attendees:
        logging.error("Error: No data provided, no output files generated.")
        return

    i = 1
    for attendee in attendees:
        name = attendee.get("name") or "N/A"
        title = attendee.get("event_title") or "N/A"
        date = attendee.get("event_date") or "N/A"
        location = attendee.get("event_location") or "N/A"

        message = template
        message = message.replace("{name}", name)
        message = message.replace("{event_title}", title)
        message = message.replace("{event_date}", date)
        message = message.replace("{event_location}", location)

        filename = f"output_{i}.txt"
        if os.path.exists(filename):
            logging.error(f"Error: {filename} already exists")
            i += 1
            continue

        try:
            with open(filename, 'w') as file:
                file.write(message)
            logging.info("File is created succesfully!.")
        except Exception as e:
            logging.error(f"Failed to write to {filename}: {e}")

        i += 1
