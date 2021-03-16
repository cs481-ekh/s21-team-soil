from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Session
# import datetime 
from datetime import datetime
def index(request):
    return HttpResponse("Viewing user_tracking index. Placeholder.")

def log_session(user_google_id, user_name, user_email):
    """[summary]

    Args:
        user_google_id ([type]): [description]
        user_name ([type]): [description]
        user_email ([type]): [description]

    Returns:
        [type]: [description]
    """

    # WORKS

    # Look up user, 
    # if existing get primary ID. 
    # if new, create new user
    # then, create new session model no matter what that depends on the user retrieved/created
    
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
    #  WORKS
    # Return all unique users in Database. 
    # sorted by full name
    # returns query set. same as python list. Each index in user_list is a user model.
    user_list = User.objects.order_by("full_name")

    # TODO: take out
    for user in user_list:
        print(user)

    return user_list    

def all_sessions():
    session_list = Session.objects.order_by("log_time")
    
    # TODO: Take out
    for s in session_list:
        print(s)
    return session_list

def get_sessions_from_user(user_pk):
    # Where user_pk is primary key of user model (not google id)
    # returns queryset 
    user_sessions = Session.objects.filter(user__id=user_pk).order_by("log_time")
    return user_sessions