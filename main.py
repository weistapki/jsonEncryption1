import json
import config_protector

config_protector.hide_config_data(b'5tlOpu2Bvib0m_yllgmzfhYVmonJNUR7bKCcdNh827Y=')
config_protector.show_config_data(b'5tlOpu2Bvib0m_yllgmzfhYVmonJNUR7bKCcdNh827Y=')

with open("config.json", "r") as config_json:
    config_string = config_json.read()

parsed_config = json.loads(config_string)


def check_password(password, users):
    for user in users:
        if password == user["password"]:
            return user["login"]
    return "Intruder"


def login_user(config):
    max_attempts = config["attempts"]
    users = config["users"]

    attempts = 0

    while attempts < max_attempts:
        password = input("Enter your password, please: ")
        username = check_password(password, users)

        if username != "Intruder":
            print(f"Welcome, {username}! It's nice to see you again")
            return
        else:
            attempts += 1
            remaining_attempts = max_attempts - attempts
            if remaining_attempts > 0:
                print(f"Sorry, password is invalid. {remaining_attempts} attempt(s) left.\nTry again!")
            else:
                print("Sorry, I don't know you")

login_user(parsed_config)

