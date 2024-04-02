class AuthorizationError(Exception):

    def __str__(self):
        return "You have exceeded the maximum number of authorization attempts. Access is denied"
