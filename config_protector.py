import json
from cryptography.fernet import Fernet

# Функція для шифрування даних користувачів
def hide_config_data(key):
    with open("config.json", "r") as config_json:
        config_data = json.load(config_json)

    cipher = Fernet(key)
# Ітерація по списку користувачів за допомогою  об'єкта
    for user in config_data["users"]:
        encrypted_login = cipher.encrypt(user["login"].encode())
        encrypted_password = cipher.encrypt(user["password"].encode())
        user["login"] = encrypted_login.decode()
        user["password"] = encrypted_password.decode()

    with open("protected_config.json", "w") as protected_config_json:
        json.dump(config_data, protected_config_json, indent=2)

# Функція для дешифрування даних користувачів
def show_config_data(key):
    with open("protected_config.json", "r") as protected_config_json:
        protected_config_data = json.load(protected_config_json)

    cipher = Fernet(key)
# Ітерація по списку користувачів за допомогою об'єкта для дешифрування
    for user in protected_config_data["users"]:
        decrypted_login = cipher.decrypt(user["login"].encode())
        decrypted_password = cipher.decrypt(user["password"].encode())
        user["login"] = decrypted_login.decode()
        user["password"] = decrypted_password.decode()

    with open("unprotected_config.json", "w") as unprotected_config_json:
        json.dump(protected_config_data, unprotected_config_json, indent=2)

# import json
# from cryptography.fernet import Fernet
#
# # Функція для шифрування даних користувачів
# def hide_config_data(key):
#     with open("config.json", "r") as config_json:
#         config_data = json.load(config_json)
#
#     cipher = Fernet(key)
#
#     # Ітерація по списку користувачів за допомогою індексів
#     for i in range(len(config_data["users"])):
#         encrypted_login = cipher.encrypt(config_data["users"][i]["login"].encode())
#         encrypted_password = cipher.encrypt(config_data["users"][i]["password"].encode())
#         config_data["users"][i]["login"] = encrypted_login.decode()
#         config_data["users"][i]["password"] = encrypted_password.decode()
#
#     with open("protected_config.json", "w") as protected_config_json:
#         json.dump(config_data, protected_config_json, indent=2)
#
# # Функція для дешифрування даних користувачів
# def show_config_data(key):
#     with open("protected_config.json", "r") as protected_config_json:
#         protected_config_data = json.load(protected_config_json)
#
#     cipher = Fernet(key)
#
#     # Ітерація по списку користувачів за допомогою індексів для дешифрування
#     for i in range(len(protected_config_data["users"])):
#         decrypted_login = cipher.decrypt(protected_config_data["users"][i]["login"].encode())
#         decrypted_password = cipher.decrypt(protected_config_data["users"][i]["password"].encode())
#         protected_config_data["users"][i]["login"] = decrypted_login.decode()
#         protected_config_data["users"][i]["password"] = decrypted_password.decode()
#
#     with open("unprotected_config.json", "w") as unprotected_config_json:
#         json.dump(protected_config_data, unprotected_config_json, indent=2)
