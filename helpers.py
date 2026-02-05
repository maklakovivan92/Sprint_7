import random
import string

# Генерация рандомной строки
def generate_random_string(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))


# Генерация payload с: логин, пароль, имя 
def generate_payload_login_password_firstname():
    payload = {
    "login": generate_random_string(10),
    "password": generate_random_string(10),
    "firstName": generate_random_string(10)
    }
    return payload


# Генерация payload с: логин, пароль
def generate_payload_login_password():
    payload = {
    "login": generate_random_string(10),
    "password": generate_random_string(10)
    }
    return payload

# Генерация payload с: пароль, имя 
def generate_payload_password_firstname():
    payload = {
    "password": generate_random_string(10),
    "firstName": generate_random_string(10)
    }
    return payload

# Генерация payload с: логин, имя 
def generate_payload_login_firstname():
    payload = {
    "login": generate_random_string(10),
    "firstName": generate_random_string(10)
    }
    return payload

# payload для тестов
def build_courier_payload(login, password, first_name):
    return {"login": login, "password": password, "firstName": first_name}
