
import unittest
from user import User
from io import StringIO
from unittest.mock import patch

class TestUser(unittest.TestCase):
    def test_create_user(self):
        user = User("testuser", "test@example.com")
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@example.com")

    def test_upload_profile_picture(self):
        user = User("testuser", "test@example.com")
        user.upload_profile_picture("profile.jpg")
        self.assertEqual(user.profile_picture, "profile.jpg")

    def test_follow_user(self):
        user1 = User("user1", "user1@example.com")
        user2 = User("user2", "user2@example.com")
        user1.follow_user(user2)
        self.assertIn(user2, user1.following)

    @patch('builtins.input', side_effect=['John', 'john@example.com', 'profile.jpg', 'yes', 'user2'])
    def test_main(self, mock_input):
        from main import create_user, main

        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
            output = fake_out.getvalue().strip()
            self.assertIn("User created successfully: Username: John, Email: john@example.com", output)
            self.assertIn("Profile picture uploaded: profile.jpg", output)
            self.assertIn("You are now following user: user2", output)

if __name__ == "__main__":
    unittest.main()
