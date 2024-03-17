class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = open(file_path, "r")
        self.lines = self.file.readlines()
        self.line_number = 0