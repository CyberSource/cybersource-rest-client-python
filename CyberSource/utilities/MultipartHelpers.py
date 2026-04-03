
import uuid
import os
import io

class MultipartHelpers:
    @staticmethod
    def build_post_body_for_files(file_params):
        if not file_params or len(file_params) == 0:
            return None

        file_name_and_content = {}
        for file_key, file_param in file_params.items():

            if  isinstance(file_param, (str, bytes, os.PathLike, int)) and os.path.isfile(file_param):
                # if the file_param is a file path
                file_name = os.path.basename(file_param)
                file_content = None
                with open(file_param, 'r') as reader:
                    file_content = reader.read()
                file_name_and_content[file_name] = file_content

            elif hasattr(file_param, 'name') or os.path.isfile(file_param.name):
                # in case of file-like object (e.g., io.BytesIO)
                # or if the file_param is a file object with a name attribute
                file_name = os.path.basename(file_param.name)
                file_content = None
                with open(file_param.name, 'r') as reader:
                    file_content = reader.read()
                file_name_and_content[file_name] = file_content

            else:
                raise ValueError(f"The parameter for input '{file_key}' is not a valid file or file path.")

        boundary = uuid.uuid4().hex
        delimiter = '-------------' + boundary
        eol = '\r\n'
        data = []

        for name, content in file_name_and_content.items():
            data.append('--' + delimiter)
            data.append(f'Content-Disposition: form-data; name="{name}"; filename="{name}"')
            data.append('Content-Transfer-Encoding: binary')
            data.append('')
            data.append(content)

        data.append('--' + delimiter + '--')
        data.append('')

        return eol.join(data), delimiter