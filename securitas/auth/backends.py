from django.contrib.auth.models import User
#from django.conf import settings
from securitas.models import TwoFactor
from securitas.utils import get_twofactor_method


class SecuritasBackend(object):
    def get_user(self, user_id=None):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def authenticate(self, username=None, password=None, otp=None):
        result = None
        try:
            # TODO check for custom main identifier
            user = User.objects.get(username=username)
            if user.check_password(password):
                try:
                    # From here on, the user is already logged in
                    # TODO make a settings variable to make
                    #      OTP mandatory to log in
                    result = user
                    if otp:
                        twofactor = TwoFactor.objects.filter(user=user)
                        for registered_method in twofactor:
                            method = get_twofactor_method(
                                registered_method.type)()
                            check = method.verify(
                                otp,
                                method=registered_method)
                            if check:
                                return user
                except TwoFactor.DoesNotExist:
                    # Let the user login if not have a two-auth
                    # method registered
                    result = user
        except User.DoesNotExist:
            pass

        return result
