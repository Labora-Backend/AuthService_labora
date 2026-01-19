from rest_framework_simplejwt.tokens import AccessToken

def generate_jwt(user):

    token = AccessToken.for_user(user)
    token["role"] = user.role
    token["user_id"] = user.id
    return str(token)
