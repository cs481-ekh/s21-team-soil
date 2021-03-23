from django.db import models
""" All models for user_tracking module.
    These models are used to relevant info from google authentication
    services in the database.
"""


class User(models.Model):
    """ Model representing a User instance.
    Stores google_id, name, and email.
    Args:
        models (Model): Django's default models.Model class

    """
    google_id = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)

    def __str__(self):
        info = f"Name: {self.full_name}, " \
            f"Email: {self.email}, " \
            f"GoogleID: {self.google_id}"
        return info


class Session(models.Model):
    """Model representing a Session instance.
    Stores when a user logs on to the website via Google authenticate.

    Args:
        models (Model): Django's default models.Model class

    """
    log_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # For debugging output.
        # Causes pylint to fail even though it is proper Django syntax.
        # return f"UserID: {self.user.google_id}, Time: {self.log_time}"
        return f"Time: {self.log_time}"
