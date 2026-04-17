VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"

def is_login_authorized(username, password):
    """Memvalidasi kredensial pengguna dengan prinsip Guard Clauses."""
    
    if username != VALID_USERNAME:
        return False, "User not found."

    if password != VALID_PASSWORD:
        return False, "Incorrect password."

    return True, "Login successful!"

def main():
    user_input = "admin"
    pass_input = "password123"
    
    is_success, message = is_login_authorized(user_input, pass_input)
    print(message)

if __name__ == "__main__":
    main()