import hashlib
import base64


class DigestAndPayload:
    def __init__(self):
        self.__blue_print = None
        self.__payload_msg_body = None
        self.json_path = None

    def string_digest_generation(self, json_path_data):
        # This method returns digest value which is SHA-256 hash of the payload which is BASE-64 Encoded
        self.json_path = json_path_data
        message_body = self.json_path
        hashobj = hashlib.sha256()
        hashobj.update(message_body.encode('utf-8'))
        hash_data = hashobj.digest()
        encoded_data = base64.b64encode(hash_data)
        blue_print = encoded_data

        return blue_print

    # This method reads the data from request.json and forms a string of data acquired from the request.json file
    # noinspection PyMethodMayBeStatic
    def string_payload_generation(self, path):
        message_list = []
        message_body = ""
        requestfile = open(path)

        for i in requestfile:
            message_list.append(i)
            message_body = "".join(message_list)
        requestfile.close()

        return message_body
