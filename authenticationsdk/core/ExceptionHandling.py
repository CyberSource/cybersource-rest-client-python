# Customized Exception class
class ApiException(Exception):

    def __init__(self, status=None, reason=None):
        super(ApiException, self).__init__(reason)
