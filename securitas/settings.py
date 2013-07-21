from django.conf import settings


# Make the OTP field mandatory
OTP_MANDATORY = getattr(settings, 'SECURITAS_OTP_MANDATORY', False)

# Allows the use of the password field to enter an OTP value
# Using this variable both password or OTP will allow the user to log in
# TODO not working ATM
#OTP_OR_PASSWORD = getattr(settings,
#                          'SECURITAS_OTP_OR_PASSWORD',
#                          not OTP_MANDATORY)
OTP_OR_PASSWORD = False
