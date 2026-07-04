import logging

logging.basicConfig(
    filename="organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


def log_move(old_name, new_name):
    logging.info(f"Moved {old_name} -> {new_name}")