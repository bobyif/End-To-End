
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.profile_picture = None
        self.following = []

    def upload_profile_picture(self, picture):
        self.profile_picture = picture

    def follow_user(self, user):
        self.following.append(user)

    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}"
