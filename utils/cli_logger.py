import sys
import logging


class StreamToLogger:
    """
    Fake stream object that redirects writes to a logger.
    """

    def __init__(self, logger, level):
        self.logger = logger
        self.level = level
        self.line_buffer = ""

    def write(self, message):
        message = message.strip()
        if message:
            self.logger.log(self.level, message)

    def flush(self):
        pass


class CLILogger:

    def __init__(self, logger_adapter):
        """
        logger_adapter = Logger().get_logger("CLI")
        """
        self.logger = logger_adapter

    def start_capture(self):
        """
        Redirect stdout and stderr to logger
        """
        sys.stdout = StreamToLogger(self.logger, logging.INFO)
        sys.stderr = StreamToLogger(self.logger, logging.ERROR)

    def stop_capture(self):
        """
        Restore original streams if needed
        """
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__