import re

def detect_value_type(cell_text):
    if re.match(r"\d{1,2}/\d{1,2}/\d{2,4}", cell_text):
        return "date"
    elif re.match(r"\d+(\.\d+)?%", cell_text):
        return "percentage"
    elif re.match(r"\d+(\.\d+)?", cell_text):
        return "numeric"
    elif re.search(r"\b(yes|no|true|false)\b", cell_text.lower()):
        return "boolean"
    else:
        return "text"
