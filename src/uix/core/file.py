class File():
    def __init__(self, name, size, type, lastModified, url):
        self.name = name
        self.size = size
        self.type = type
        self.lastModified = lastModified
        self.url = url
    def __str__(self):
        return str(self.__dict__)