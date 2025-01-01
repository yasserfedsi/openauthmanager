import json
from bcrypt import hashpw, gensalt, checkpw

# Constants
ALLOWED_DOMAINS = ["@gmail.com"] # You can add more domains here!
DEFAULT_CONTENT = {"users": []}
FILE_NAME = "users.json"

# Load and Save Users
def load_users():
    try:
        with open(FILE_NAME, "r") as file:
            content = file.read().strip()
            if content:
                data = json.loads(content)
                return data.get("users", [])
            default_content()
            return DEFAULT_CONTENT["users"]
    except FileNotFoundError:
        print(f"File not found: {FILE_NAME}")
        default_content()
        return DEFAULT_CONTENT["users"]
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from {FILE_NAME}: {e}")
        default_content()
        return DEFAULT_CONTENT["users"]

def save_users():
    try:
        with open(FILE_NAME, "w") as file:
            json.dump({"users": users}, file)
            print(f"Users successfully saved to {FILE_NAME}.")
    except IOError as e:
        print(f"Error saving {FILE_NAME}: {e}")

# Password Handling
def hash_password(password):
    return hashpw(password.encode(), gensalt()).decode()

def verify_password(password, hashed_password):
    return checkpw(password.encode(), hashed_password.encode())

# Helpers
def validate_email(email):
    return any(email.endswith(domain) for domain in ALLOWED_DOMAINS)

def get_valid_email():
    email = input("Enter your email address: ").strip()
    if not validate_email(email):
        print("Error: email must end with allowed domains.")
        return None
    return email

def get_valid_password():
    password = input("Enter your password: ").strip()
    confirm_password = input("Confirm your password: ").strip()
    if password != confirm_password:
        print("Error: Passwords do not match.")
        return None
    if len(password) < 5:
        print("Error: Password must be at least 5 characters.")
        return None
    return hash_password(password)

def default_content():
    with open(FILE_NAME, "w") as file:
        json.dump(DEFAULT_CONTENT, file)
        print(f"{FILE_NAME} created with default content: {DEFAULT_CONTENT}")

# Global Variables
users = load_users()

# Core Functions
def add_user():
    user_email = get_valid_email()
    if not user_email:
        return
    user_password = get_valid_password()
    if not user_password:
        return

    if any(user["email"] == user_email for user in users):
        print("Error: email already exists.")
        return

    user = {
        "email": user_email,
        "password": user_password,
        "personalInformation": {}
    }
    users.append(user)
    save_users()
    print(f"User with email: {user_email}, added successfully")

def search_users():
    search_email = get_valid_email()
    if not search_email:
        return

    for user in users:
        if user["email"] == search_email:
            print(f"User found: {user}")
            return

    print("No user found with that email.")

def modify_user():
    current_email = get_valid_email()
    if not current_email:
        return
    new_email = get_valid_email()
    if not new_email:
        return
    new_password = get_valid_password()
    if not new_password:
        return

    for user in users:
        if user["email"] == current_email:
            user["email"] = new_email
            user["password"] = new_password
            save_users()
            print(f"User updated successfully to: {user}")
            return

    print("Error: No user found with the specified current email.")

def display_users(authenticated=False):
    if not users:
        print("No users to display.")
        return
    for user in users:
        print(user if authenticated else {key: user[key] for key in ["email"]})

def delete_user():
    search_email = get_valid_email()
    if not search_email:
        return

    for user in users:
        if user["email"] == search_email:
            users.remove(user)
            save_users()
            print(f"User with email {search_email} deleted successfully.")
            return

    print("Error: No user found with that email.")

# Authentication Functions
def auth_user():
    user_email_auth = get_valid_email()
    if not user_email_auth:
        return
    user_password_auth = input("Enter your password: ").strip()

    for user in users:
        if user["email"] == user_email_auth and verify_password(user_password_auth, user["password"]):
            print(f"Authentication successful! Welcome @{user['personalInformation'].get('Full name', 'User')}.")
            return

    print("Error: Incorrect email or password.")

def modify_password_auth():
    user_email_auth = get_valid_email()
    if not user_email_auth:
        return
    current_password_auth = input("Enter your current password: ").strip()

    for user in users:
        if user["email"] == user_email_auth and verify_password(current_password_auth, user["password"]):
            new_password_auth = get_valid_password()
            if not new_password_auth:
                return
            user["password"] = new_password_auth
            save_users()
            print("Password changed successfully!")
            return

    print("Error: Authentication failed. email or password is incorrect.")

def modify_email_auth():
    current_email_auth = get_valid_email()
    if not current_email_auth:
        return
    user = next((u for u in users if u["email"] == current_email_auth), None)

    if not user:
        print("Error: email address not found.")
        return

    new_email_auth = get_valid_email()
    if not new_email_auth:
        return

    user["email"] = new_email_auth
    save_users()
    print("Email updated successfully!")

def add_personal_info():
    user_email_auth = get_valid_email()
    if not user_email_auth:
        return

    user = next((u for u in users if u["email"] == user_email_auth), None)
    if not user:
        print("Error: User not found.")
        return

    user["personalInformation"] = {
        "Full name": input("Enter your full name: ").strip(),
        "Phone number": input("Enter your phone number: ").strip(),
        "City": input("Enter your city (Wilaya): ").strip()
    }
    save_users()
    print("Personal information added successfully!")

# Main Loop
def authentication_system():
    while True:
        print("\nAuthentication System")
        print("1. Authenticate User")
        print("2. Modify User Password")
        print("3. Modify User Email")
        print("4. Add Personal Info")
        print("5. Display Users")
        print("6. Logout")

        auth_choice = input("Enter your choice: ").strip()

        if auth_choice == "1":
            auth_user()
        elif auth_choice == "2":
            modify_password_auth()
        elif auth_choice == "3":
            modify_email_auth()
        elif auth_choice == "4":
            add_personal_info()
        elif auth_choice == "5":
            display_users(authenticated=True)
        elif auth_choice == "6":
            print("Logging out!")
            break
        else:
            print("Invalid choice. Please try again.")

# Main Program Loop
while True:
    print("\nWelcome to OpenAuthManager")
    print("Please choose an option: ")
    print("1. Add User")
    print("2. Search User")
    print("3. Modify User")
    print("4. Delete User")
    print("5. Display Users")
    print("6. Switch to Authentication System")
    print("7. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_user()
    elif choice == "2":
        search_users()
    elif choice == "3":
        modify_user()
    elif choice == "4":
        delete_user()
    elif choice == "5":
        display_users()
    elif choice == "6":
        authentication_system()
    elif choice == "7":
        print("Thank you for using OpenAuthManager!")
        break
    else:
        print("Invalid choice. Please try again.")
