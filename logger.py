import datetime

def log_message(message, level="INFO"):
    # Feature C: Logging functionality
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"[{timestamp}] {level}: {message}"

def log_error(message):
    return log_message(message, "ERROR")

def log_warning(message):
    return log_message(message, "WARNING")