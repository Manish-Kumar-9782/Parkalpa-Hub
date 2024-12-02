
class Error:

    def __init__(self):
        self.errors = {}

    def add_error(self, name, message):
        self.errors[name] = message

    def get_errors(self):
        return self.errors
