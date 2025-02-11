import logging
import re


class SensitiveFormatter(logging.Formatter):
    """Formatter that removes sensitive information in urls."""
    @staticmethod
    def _filter(s):
        s = re.sub(r'"securityCode"\s*:\s*"[0-9]{3,4}"', r'"securityCode":"xxxxx"', s)
        s = re.sub(r'"expirationMonth"\s*:\s*"[0-1][0-9]"', r'"expirationMonth":"xxxx"', s)
        s = re.sub(r'"expirationYear"\s*:\s*"2[0-9][0-9][0-9]"', r'"expirationYear":"xxxx"', s)
        s = re.sub(r'"routingNumber"\s*:\s*"[0-9]+"', r'"routingNumber":"xxxxx"', s)
        s = re.sub(r'"email"\s*:\s*"[a-z0-9!#$.%&*+\/=?^_`{|}~-]+(?:.[a-z0-9.!#$%&*+\/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"', r'"email":"xxxxx"', s)
        s = re.sub(r'"firstName"\s*:\s*"([a-zA-Z]+( )?[a-zA-Z]*?-?[a-zA-Z]*( )?([a-zA-Z]*)?)"', r'"firstName":"xxxxxx"', s)
        s = re.sub(r'"lastName"\s*:\s*"([a-zA-Z]+( )?[a-zA-Z]*?-?[a-zA-Z]*( )?([a-zA-Z]*)?)"', r'"lastName":"xxxxxx"', s)
        s = re.sub(r'"phoneNumber"\s*:\s*"(\\+[0-9]{1,2})?\\([0-9]{3}\\)?[.-]?[0-9]{3}[ .-]?[0-9]{4}"', r'"phoneNumber":"xxxxxx"', s)
        s = re.sub(r'"phoneNumber"\s*:\s*"\+?[0-9]{0,2}[.-]?[0-9]{3}[.-]?[0-9]{3}[.-]?[0-9]{4}"', r'"phoneNumber":"xxxxxx"', s)
        s = re.sub(r'"type"\s*:\s*"[-A-Za-z0-9 ]+"', r'"type":"xxxxx"', s)
        s = re.sub(r'"token"\s*:\s*"[-.A-Za-z0-9+/= ]+"', r'"token":"xxxxx"', s)
        s = re.sub(r'signature="[-.A-Za-z0-9+/= ]+"', r'signature="xxxxxxxx"', s)
        s = re.sub(r'keyid="[-.A-Za-z0-9+/= ]+"', r'keyid="xxxxxxxx"', s)

        # masking cardNumber
        matches = re.search(r'"cardNumber"\s*:\s*"(((\s*[s/-]*\s*)+[0-9](\s*[s/-]*\s*)+)+)"', s)
        if matches:
            matchedString= matches.group(0)            
            matchString= matchedString.replace(" ","")
            matchString= matchString.replace("-","")
            pats = re.findall(r'"cardNumber"\s*:\s*"[0-9]+"', matchString)
            if len(pats) > 0:
                pat = pats[0]
                pat = re.sub(r'[0-9](?=.*.{5})', r'x', pat)
                replaceString = re.sub(r'"cardNumber"\s*:\s*"[0-9]+"', pat, matchString)
                s=s.replace(matchedString,replaceString)
        
        # masking number
        matches = re.search(r'"number"\s*:\s*"(((\s*[s/-]*\s*)+[0-9](\s*[s/-]*\s*)+)+)"', s)
        if matches:
            matchedString= matches.group(0)
            matchString= matchedString.replace(" ","")
            matchString= matchString.replace("-","")
            pats = re.findall(r'"number"\s*:\s*"[0-9]+"', matchString)
            if len(pats) > 0:
                pat = pats[0]
                pat = re.sub(r'[0-9](?=.*.{5})', r'x', pat)
                replaceString = re.sub(r'"number"\s*:\s*"[0-9]+"', pat, matchString)
                s=s.replace(matchedString,replaceString)
        
        # masking account
        matches = re.search(r'"account"\s*:\s*"(((\s*[s/-]*\s*)+[0-9](\s*[s/-]*\s*)+)+)"', s)
        if matches:
            matchedString= matches.group(0)
            matchString= matchedString.replace(" ","")
            matchString= matchString.replace("-","")
            pats = re.findall(r'"account"\s*:\s*"[0-9]+"', matchString)
            if len(pats) > 0:
                pat = pats[0]
                pat = re.sub(r'[0-9](?=.*.{5})', r'x', pat)
                replaceString = re.sub(r'"account"\s*:\s*"[0-9]+"', pat, matchString)
                s=s.replace(matchedString,replaceString)
            
        # masking prefix
        matches = re.search(r'"prefix"\s*:\s*"(((\s*[s/-]*\s*)+[0-9](\s*[s/-]*\s*)+)+)"', s)
        if matches:
            matchedString= matches.group(0)
            matchString= matchedString.replace(" ","")
            matchString= matchString.replace("-","")
            pats = re.findall(r'"prefix"\s*:\s*"[0-9]+"', matchString)
            if len(pats) > 0:
                pat = pats[0]
                pat = re.sub(r'(?<=["])([0-9]{6})', r'x', pat)
                replaceString = re.sub(r'"prefix"\s*:\s*"[0-9]+"', pat, matchString)
                s=s.replace(matchedString,replaceString)
                
        # masking bin
        matches = re.search(r'"bin"\s*:\s*"(((\s*[s/-]*\s*)+[0-9](\s*[s/-]*\s*)+)+)"', s)
        if matches:
            matchedString= matches.group(0)
            matchString= matchedString.replace(" ","")
            matchString= matchString.replace("-","")
            pats = re.findall(r'"bin"\s*:\s*"[0-9]+"', matchString)
            if len(pats) > 0:
                pat = pats[0]
                pat = re.sub(r'(?<=["])([0-9]{6})', r'x', pat)
                replaceString = re.sub(r'"bin"\s*:\s*"[0-9]+"', pat, matchString)
                s=s.replace(matchedString,replaceString)

        return s

    def format(self, record):
        original = logging.Formatter.format(self, record)
        return self._filter(original)