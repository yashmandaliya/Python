# Creating a function
def login():  
    username = input("Enter username: ")  
    password = input("Enter password: ")  
  
    # Assuming we have a list of valid usernames and passwords  
    valid_users = ["user1", "user2", "user3"]  
    valid_passwords = ["pass1", "pass2", "pass3"]  
  
    if username in valid_users and password == valid_passwords[valid_users.index(username)]:  
        print("Login successful!")  
        # Add code to redirect to main application or perform other actions here  
    else:  
        print("Invalid username or password.")  
        # Add code to handle incorrect login attempts here  
  
login()
