import logging
import json

# ---------------- Basic structured logging setup ----------------
class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "funcName": record.funcName,
            "time": self.formatTime(record, self.datefmt)
        }
        if hasattr(record, "extra"):
            log_record.update(record.extra)
        return json.dumps(log_record)

# Create logger
logger = logging.getLogger("my_app")
logger.setLevel(logging.DEBUG)  # Capture all levels

# Create console handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Assign JSON formatter
formatter = JsonFormatter()
ch.setFormatter(formatter)

logger.addHandler(ch)

# ---------------- Example usage ----------------
logger.debug("This is a debug message", extra={"extra": {"user_id": 123}})
logger.info("User logged in", extra={"extra": {"user_id": 123, "ip": "192.168.0.1"}})
logger.warning("Disk space low", extra={"extra": {"disk": "/dev/sda1"}})
logger.error("Error processing request", extra={"extra": {"request_id": "abc123"}})
logger.critical("System down!", extra={"extra": {"server": "server-01"}})
