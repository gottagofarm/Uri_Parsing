"""
This file contains the URI Python class and the validation variables.
"""

VALID_SCHEMES = [
    "visma-identity"
]

VALID_PATHS = {
    "login": {
        "source": "string"
    },
    "confirm": {
        "source": "string",
        "paymentnumber": "number"
    },
    "sign": {
        "source": "string",
        "documentid": "string"
    }
}

class URI:
    """
    This class takes an uri as constructor parameter and parses it.
    scheme: String
    path: String
    params: Dict
    """
    scheme = ""
    path = ""
    params = {}

    def __init__(self, uri: str):
        """
        This function splits the uri to isolate the components
        """
        temp_uri = uri.split('://')
        self.scheme = temp_uri[0]
        temp_uri = temp_uri[1].split('?')
        self.path =  temp_uri[0]
        params_list = temp_uri[1].split('&')

        for param in params_list:
            param = param.split("=")
            self.params[param[0]] = param[1]

        self.validate()

    def validate(self):
        """
        This function validates class attributes and parameter types.
        """
        if self.scheme not in VALID_SCHEMES or self.path not in VALID_PATHS:
            return False

        for param in self.params:
            if param not in VALID_PATHS[self.path]:
                return False
            if VALID_PATHS[self.path][param] == "number":
                try:
                    self.params[param] = int(self.params[param])
                except ValueError:
                    return False

        return True
