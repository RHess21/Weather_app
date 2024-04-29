import re

def zipSanitize(zip):
    zipPattern = re.compile(r'^\d{5}$')
    if zipPattern.match(zip):
        return True
    else:
        return False
    
    
import json

def validate_json(json_data):
    try:
        json.dumps(json_data)
    except ValueError as err:
        return False
    return True