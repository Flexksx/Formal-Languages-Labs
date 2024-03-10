import json

class Variant:
    def __init__(self,path:str)->None:
        self.path = path
        self.variant = json.loads(open(self.path).read())

    def getVariant(self):
        return self.variant

    def getVN(self) -> list:
        return self.variant['VN']

    def getVT(self) -> list:
        return self.variant['VT']

    def getP(self) -> list:
        return self.variant['P']