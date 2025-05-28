def validate_email(email):
    import re
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def validate_phone(phone):
    return phone.isdigit() and len(phone) in [10, 11]

def validate_required_fields(data, required_fields):
    for field in required_fields:
        if field not in data or not data[field]:
            return False
    return True

def validate_client_data(data):
    required_fields = ['nom', 'prenom', 'email', 'telephone', 'adresse', 'statut', 'IFU', 'RCCM']
    if not validate_required_fields(data, required_fields):
        return False
    if not validate_email(data['email']):
        return False
    if not validate_phone(data['telephone']):
        return False
    return True