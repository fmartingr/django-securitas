from django.contrib.auth.models import User
from securitas import settings
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
                    # Log in the user if the OTP is not mandatory
                    if not settings.OTP_MANDATORY:
                        result = user

                    if otp:
                        twofactor = TwoFactor.objects.filter(user=user)

                        # Checks the registered two factor auths
                        # method for this user
                        for registered_method in twofactor:
                            method = get_twofactor_method(
                                registered_method.type)()
                            try:
                                check = method.verify(
                                    otp, method=registered_method)
                                # Returns the user when a twoauth method
                                # is valid
                                if check:
                                    return user
                            except:
                                # Incorrect format OTPs
                                pass
                except TwoFactor.DoesNotExist:
                    # Let the user login if not have a two-auth
                    # method registered
                    result = user
        except User.DoesNotExist:
            pass

        return result


class SecuritasDemoBackend(object):
    """
    Backend for presentations that don't check for a correct
    OTP value
    """
    pass
