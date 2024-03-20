
from user import User

def create_user():
    print("Let's create a new user.")
    username = input("Enter username: ")
    email = input("Enter email: ")
    return User(username, email)

def main():
    print("Welcome to User Management System!")

    user = create_user()
    print(f"User created successfully: {user}")

    # Upload profile picture
    profile_picture = input("Enter profile picture filename: ")
    user.upload_profile_picture(profile_picture)
    print(f"Profile picture uploaded: {user.profile_picture}")

    # Follow user
    choice = input("Do you want to follow another user? (yes/no): ")
    if choice.lower() == "yes":
        follow_username = input("Enter username of the user you want to follow: ")
        user_to_follow = User(follow_username, "dummy@example.com")  # Assuming dummy email for simplicity
        user.follow_user(user_to_follow)
        print(f"You are now following user: {follow_username}")

if __name__ == "__main__":
    main()
