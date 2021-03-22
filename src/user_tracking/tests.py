from django.test import TestCase

from .models import *
from .views import get_sessions_from_user, log_session

class UserTrackingTests(TestCase):
    """Test methods provided by user_tracking app. Ensure proper storing and retrieval 
    of user tracking data. To run tests from src folder run: "python manage.py test user_tracking" on the
    command line.

    Args:
        TestCase (TestCase): Django's testing framework TestCase
    """

    def test_create_new_user(self):
        """Tests that views.log_session() will create a new user in database if it is 
        asked to create a new session for a user that does not currently exist.
        """
        test_google_id = -1
        test_name = "new username"
        test_email = "test1@gmail.com"
        log_session(test_google_id, test_name, test_email)

        try:
            test_user = User.objects.get(google_id=test_google_id)
        except User.DoesNotExist:
            self.fail("log_session failed to create a new user")

        user = User()
        user.google_id = test_google_id
        user.full_name = test_name
        user.email = test_email

        self.assertEqual(user.__str__(), test_user.__str__())
        

    def test_add_session_to_old_user(self):
        """Ensure views.log_session() will add a new session to an existing user in the database.
        """

        test_google_id = - 2
        test_name = "new_username"
        test_email = "test2@gmail.com"

        user = User()
        user.google_id = test_google_id
        user.full_name = test_name
        user.email = test_email
        user.save()

        session_count = len(Session.objects.all())
        user_count = len(User.objects.all())

        # Should add 1 new session to database but NO new users to database
        log_session(test_google_id, test_name, test_email)

        new_session_count = len(Session.objects.all())
        new_user_count = len(User.objects.all())

        self.assertEqual(new_user_count, user_count)
        self.assertEqual(new_session_count, session_count + 1)
        return None

    def test_sessions_from_user(self):
        """Ensures get_sessions_from_user returns all sessions for an existing User in database.
        """
        
        test_google_id = - 3
        test_name = "new_username"
        test_email = "test2@gmail.com"

        user = User()
        user.google_id = test_google_id
        user.full_name = test_name
        user.email = test_email
        user.save()
        num_new_sessions = 3
        session_1 = Session()
        session_1.user = user
        session_1.save()

        session_2= Session()
        session_2.user = user
        session_2.save()

        session_3 = Session()
        session_3.user = user
        session_3.save()

        session_count = len(get_sessions_from_user(test_google_id))

        self.assertEqual(session_count, num_new_sessions )
