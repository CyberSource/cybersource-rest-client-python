class JWEException(Exception):
    def __init__(self, reason=None):
        super(JWEException, self).__init__(reason)
