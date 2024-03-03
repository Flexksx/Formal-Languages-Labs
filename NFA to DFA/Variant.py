import json

class Variant:
    path ="/Users/cristiancretu/Documents/UniCode/LabsLFA/NFA to DFA/variant.json"
    def __init__(self):
        self.variant = json.loads(open(self.path).read())

    def getVariant(self):
        return self.variant
