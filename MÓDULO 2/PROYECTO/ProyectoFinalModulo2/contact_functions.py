contacts = []

def add_contact(name, phone, email):
    contacts.append({"name": name, "phone": phone, "email": email})

def find_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return None

def update_contact(name, phone, email):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            if phone:
                contact["phone"] = phone
            if email:
                contact["email"] = email
            return True
    return False

def delete_contact(name):
    for i, contact in enumerate(contacts):
        if contact["name"].lower() == name.lower():
            del contacts[i]
            return True
    return False
