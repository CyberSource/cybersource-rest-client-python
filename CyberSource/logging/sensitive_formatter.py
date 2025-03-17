import logging
import json
import re


class SensitiveFormatter(logging.Formatter):
    sensitive_fields = [
        "securityCode",
        "cardNumber",
        "number",
        "expirationMonth",
        "expirationYear",
        "routingNumber",
        "email",
        "firstName",
        "lastName",
        "phoneNumber",
        "type",
        "token",
        "signature",
        "keyid"
    ]

    """Formatter that removes sensitive information in urls."""
    @staticmethod
    def is_json_string(message):
        try:
            json.loads(message)
            return True
        except ValueError:
            return False

    @staticmethod
    def _filter(s):
        if SensitiveFormatter.is_json_string(s):
            json_msg = json.loads(s)

            if isinstance(json_msg, dict):
                for prop in json_msg:
                    is_field_sensitive = prop in SensitiveFormatter.sensitive_fields
                    if is_field_sensitive:
                        if json_msg[prop] is not None:
                            if isinstance(json_msg[prop], str) and len(json_msg[prop]) > 0:
                                json_msg[prop] = 'X' * len(json_msg[prop])
                            else:
                                json_msg[prop] = json.loads(SensitiveFormatter._filter(json.dumps(json_msg[prop])))
                    else:
                        json_msg[prop] = json.loads(SensitiveFormatter._filter(json.dumps(json_msg[prop])))

            return json.dumps(json_msg)

        elif "Signature:" in s:
            splits = s.split("     ")
            start_split = splits[0]
            splits = splits[1].split(",")
            split_keyid = splits[0].split("=")
            split_signature = splits[-1].split("=")
            new_log_message = start_split + "     " + split_keyid[0] + "=\"XXXXX\", " + splits[1] + ", " + splits[2] + ", " + split_signature[0] + "\"XXXXX\""
            return new_log_message
        
        elif "Digest:" in s:
            splits = s.split("=", 1)
            new_log_message = splits[0] + "=XXXXX"
            return new_log_message
        
        elif "Authorization Bearer:" in s:
            splits = s.split("     ")
            new_log_message = splits[0] + "     XXXXX"
            return new_log_message
        else:
            return s

    def format(self, record):
        new_message = self._filter(record.msg)
        new_record = logging.LogRecord(record.name, record.levelno, record.pathname, record.lineno, new_message, record.args, record.exc_info)
        return logging.Formatter.format(self, new_record)