from abc import ABCMeta, abstractmethod


class TokenGeneration:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_token(self):
        pass
