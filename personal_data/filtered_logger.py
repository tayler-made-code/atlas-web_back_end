#!/usr/bin/env python3

""" use a function to return a log message obfuscated """

import re
from typing import List
import logging

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ init """
        super(RedactingFormatter, self).__init__(
            "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: "
            "%(message)s")
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ format """
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ returns the log message obfuscated """
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message


def get_logger() -> logging.Logger:
    """ get_logger takes no arguments and returns a logging.Logger object """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(handler)
    return logger
