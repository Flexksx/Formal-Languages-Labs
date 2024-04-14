import json

class Variant:
    def __init__(self,path:str)->None:
        self.path = path
        self.variant = json.loads(open(self.path).read())

    def getVariant(self):
        return self.variant

    def getVN(self) -> list:
        if 'VN' in self.variant:
            return self.variant['VN']
        elif 'Vn' in self.variant:
            return self.variant['Vn']

    def getVT(self) -> list:
        if 'VT' in self.variant:
            return self.variant['VT']
        elif 'Vt' in self.variant:
            return self.variant['Vt']
        
    def getP(self) -> list:
        return self.variant['P']