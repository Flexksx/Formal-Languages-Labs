class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = open(file_path, "r")
        self.lines = self.file.readlines()
        self.lines=self.get()
        self.line_number = 0
        self.file.close()
    
    def get_strip(self):
        lines = [line.strip() for line in self.lines]
        return lines
    
    def print_strip(self):
        print(self.get_strip())
        
    def print(self):
        print(self.lines)
    
    def get(self):
        return self.lines