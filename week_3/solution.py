class FileReader:
    def __init__(self, path):
        self.__path = path

    def read(self):
        try:
            with open(self.__path, 'r') as f:
                return f.read()
        except IOError:
            return ""


reader = FileReader("example.txt")
print(reader.read())
