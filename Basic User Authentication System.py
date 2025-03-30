# Dictionary to store user credentials

user_credentials = {}

# Function to register a new user
def register_user():
    username = input("Enter a new username: ")

    # Check if the username already exists
    if username in user_credentials:
        print("Username already exists! Try a different username.")
    else:
        password = input("Enter a new password: ")
        user_credentials[username] = password
        print("Registration successful!")

# Function to log in an existing user
def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username exists and the password matches
    if username in user_credentials and user_credentials[username] == password:
        print("Login successful! Welcome back.")
    else:
        print("Invalid username or password. Please try again.")

# Main menu
def authentication_system():
    while True:
        print("\n*** Basic Authentication System ***")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

# Run the authentication system
authentication_system()