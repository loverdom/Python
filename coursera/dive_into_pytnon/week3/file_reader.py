class FileReader:

    def __init__(self, filepath):
        assert isinstance(filepath, object)
        self.filepath = filepath


    def read(self):
        try:
            with open(self.filepath, 'r') as read_file:
                return read_file.read()

        except FileNotFoundError:
            return ""
