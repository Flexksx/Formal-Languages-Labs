import json


class Variant:
    def __init__(self, _variantpath):
        self.variantpath = _variantpath

    def __read_variant(self) -> dict:
        with open(self.variantpath, 'r') as f:
            variant = json.load(f)
        return variant

    def getVN(self) -> list:
        return self.__read_variant()['VN']

    def getVT(self) -> list:
        return self.__read_variant()['VT']

    def getP(self) -> list:
        return self.__read_variant()['P']

