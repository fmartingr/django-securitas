from yubikey import Yubikey


class YubicoOTPMethod(object):
    def verify(self, otp, method):
        yubi = Yubikey(
            method.secret_id,
            method.secret_key
        )

        return yubi.verify(otp)

    @staticmethod
    def __unicode__():
        return 'Yubico - OTP'

twoauth_methods = [
    ('yubico-otp', YubicoOTPMethod),
]
