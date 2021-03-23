from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Session
from datetime import datetime


def index(request):
    return HttpResponse("Viewing user_tracking index. Placeholder.")

def log_session(user_google_id, user_name, user_email):
    """Creates a new session in database for provided user. If user is a new unseen user, adds
    a new user to database as well..

    Args:
        user_google_id (int): google id of user, provided by google authenticate
        user_name (str): Full name of user
        user_email (str): Email of user

    Returns:
        None: Stores in database with no return values
    """

    # See if user exists in database. Query by their google_id.
    try:
        user = User.objects.get(google_id=user_google_id)
    except User.DoesNotExist:
        # User was not found in database. Create a new user and save.
        user = User()
        user.google_id = user_google_id
        user.full_name = user_name
        user.email = user_email
        user.save()

    # Create new session and save
    current_session = Session()
    current_session.user = user
    current_session.save()

    print(user)
    print(current_session)
    return None

def all_users():
    """Returns all users in database sorted by name

    Returns:
        QuerySet[User]: List containing each User instance
    """
    # Return all unique users in Database. 
    # sorted by full name
    # returns query set. same as python list. Each index in user_list is a user model.
    user_list = User.objects.order_by("full_name")
    return user_list    

def all_sessions():
    """Returns all sessions in database sorted by time.

    Returns:
        QuerySet[Session]: List containing each Session instance
    """
    session_list = Session.objects.order_by("log_time")

    return session_list

def get_sessions_from_user(user_google_id):
    """Returns all sessions for a User given their google id sorted by time. 
    Returns None if no sessions for user found. 
    This would imply the user is not even in the database as all Users are guaranteed to have at least one session.

    Args:
        user_google_id (int): Google ID of user

    Returns:
        QuerySet: List containing each Session instance for user or None if no sessions found
    """
    user_sessions = Session.objects.filter(user__google_id=user_google_id).order_by("log_time")
    return user_sessions