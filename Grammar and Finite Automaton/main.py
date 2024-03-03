from Variant import Variant
from Grammar import Grammar

'''Get the variant from the restructured to json file'''
variant = Variant('/Users/cristiancretu/Documents/UniCode/LabsLFA/Lab1/variant.json')
VN = variant.getVN()
VT = variant.getVT()
P = variant.getP()
print("My variant is: ")
print(VN)
print(VT)
print(P)
print()

'''Create the grammar and the finite automation'''
g = Grammar(VN, VT, P)
'''Press Ctrl+Left Click on Grammar to see the implementation'''
fa = g.to_finite_automation()
print(g.generate_strings())

'''Test the grammar by generating 5 strings and checking if they belong to the language'''
for i in range(5):
    test = g.generate_strings()
    for string in test:
        if not fa.string_belongs_to_language(string):
            print(f'{string} did not pass the test')
    print("Test passed!")

'''Test if some random strings belong to the language'''
print(fa.string_belongs_to_language("a"))
print(fa.string_belongs_to_language("ab"))
print(fa.string_belongs_to_language("ba"))
print(fa.string_belongs_to_language("FAFTOPCIK"))
print(fa.string_belongs_to_language("abcabcaaaaaae"))
