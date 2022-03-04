from authenticationsdk.core.TokenGeneration import *
from authenticationsdk.util.GlobalLabelParameters import *

class OAuthToken(TokenGeneration):
    def __init__(self):
        self.merchant_config = None        

    def oauth_token(self, mconfig):
        self.merchant_config = mconfig

    def get_token(self):        
        return self.merchant_config.access_token
