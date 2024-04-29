# Laboratory Work Nr.5 Chomsky Normal Form Converter

### Course: Formal Languages & Finite Automata
### Author: Cretu Cristian
### Group: FAF-223
----

## Theory
In formal language theory, a context-free grammar, G, is said to be in Chomsky normal form (first described by Noam Chomsky) if all of its production rules are of the form:
A → BC, or 
A → a, or 
S → ε,
where A, B, and C are nonterminal symbols, the letter a is a terminal symbol (a symbol that represents a constant value), S is the start symbol, and ε denotes the empty string. 
Also, neither B nor C may be the start symbol, and the third production rule can only appear if ε is in L(G), the language produced by the context-free grammar G.
Every grammar in Chomsky normal form is context-free, and conversely, every context-free grammar can be transformed into an equivalent one which is in Chomsky normal form and has a size no larger than the square of the original grammar's size.

## Objectives:
1. Learn about Chomsky Normal Form (CNF) [1].
2. Get familiar with the approaches of normalizing a grammar.
3. Implement a method for normalizing an input grammar by the rules of CNF.
    1. The implementation needs to be encapsulated in a method with an appropriate signature (also ideally in an appropriate class/type).
    2. The implemented functionality needs executed and tested.
    3. A **BONUS point** will be given for the student who will have unit tests that validate the functionality of the project.
    4. Also, another **BONUS point** would be given if the student will make the aforementioned function to accept any grammar, not only the one from the student's variant.



## Implementation description

To execute the conversion of a context free grammar to the Chomsky Normal Form, there are some operations that help us do that. This is why I chose to implement them separately in each class.

#### START Operation:
START: Eliminate the start symbol from right-hand sides.
Introduce a new start symbol S0, and a new rule 
S0 → S, 
where S is the previous start symbol. This does not change the grammar's produced language, and S0 will not occur on any rule's right-hand side.
```python
class StartOperation:
    @staticmethod
    def do(P: dict = None, S: str = None, Vn: list = None):
        try:
            for value in P.values():
                for production in value:
                    for character in production:
                        if character == S:
                            raise ValueError('S is in a production')
        except:
            new_P = {'X': [S]}
            new_P.update(P)
            S = 'X'
            Vn.append(S)
            P = new_P

        return P, S, Vn
```


#### TERM Operation:
To eliminate each rule
A → X1 ... a ... Xn
with a terminal symbol a being not the only symbol on the right-hand side, introduce, for every such terminal, a new nonterminal symbol Na, and a new rule
Na → a.
Change every rule
A → X1 ... a ... Xn
to
A → X1 ... Na ... Xn.
If several terminal symbols occur on the right-hand side, simultaneously replace each of them by its associated nonterminal symbol. This does not change the grammar's produced language.
```python
class TermOperation:
    @staticmethod
    def do(P: dict = None, S: str = None, Vn: list[str] = None, Vt: list[str] = None):
        new_P = TermOperation.replace_terminals_with_nonterminals(P, Vn, Vt)
        return new_P

    @staticmethod
    def replace_terminals_with_nonterminals(P: dict, Vn: list[str], Vt: list[str]) -> dict:
        terminal_to_nonterminal = {}
        new_P = P.copy()  # Initialize new_P with a copy of P
        for key, productions in P.items():
            new_productions = []
            for prod in productions:
                new_prod = TermOperation.replace_terminal(prod, Vt, terminal_to_nonterminal, Vn, new_P)
                new_productions.append(new_prod)
            new_P[key] = new_productions
        return new_P
```
#### BIN Operation
Replace each rule
A → X1 X2 ... Xn
with more than 2 nonterminals X1,...,Xn by rules
A → X1 A1,
A1 → X2 A2,
... ,
An-2 → Xn-1 Xn,
where Ai are new nonterminal symbols. Again, this does not change the grammar's produced language.
```python
class BinOperation:
    @staticmethod
    def do(P: dict[str, list[str]] = None, Vn: list[str] = None) -> dict[str, list[str]]:
        if P is None or Vn is None:
            return {}

        existing_binaries = {}
        new_productions_dict = {}
        for key, productions in P.items():
            new_productions = []
            for production in productions:
                if len(production) > 2:
         ...
```
#### DEL Operation
An ε-rule is a rule of the form
A → ε,
where A is not S0, the grammar's start symbol.
To eliminate all rules of this form, first determine the set of all nonterminals that derive ε. Hopcroft and Ullman (1979) call such nonterminals nullable, and compute them as follows:
If a rule A → ε exists, then A is nullable.
If a rule A → X1 ... Xn exists, and every single Xi is nullable, then A is nullable, too.
Obtain an intermediate grammar by replacing each rule
A → X1 ... Xn
by all versions with some nullable Xi omitted. By deleting in this grammar each ε-rule, unless its left-hand side is the start symbol, the transformed grammar is obtained.
For example, in the following grammar, with start symbol S0,
S0 → AbB | C
B → AA | AC
C → b | c
A → a | ε
the nonterminal A, and hence also B, is nullable, while neither C nor S0 is. Hence the following intermediate grammar is obtained:
S0 → AbB | AbB | AbB | AbB   |   C
B → AA | AA | AA | AεA   |   AC | AC
C → b | c
A → a | ε
In this grammar, all ε-rules have been "inlined at the call site".[note 4] In the next step, they can hence be deleted, yielding the grammar:
S0 → AbB | Ab | bB | b   |   C
B → AA | A   |   AC | C
C → b | c
A → a
This grammar produces the same language as the original example grammar, viz. {ab,aba,abaa,abab,abac,abb,abc,b,bab,bac,bb,bc,c}, but has no ε-rules.

```python
class DelOperation:
    @staticmethod
    def do(P: dict[str, list[str]] = None, S: str = None, Vn: list[str] = None) -> dict[str, list[str]]:
        if P is None or S is None or Vn is None:
            return {}

        count_null = 0
        null_prods = []
        for key, value in P.items():
            for production in value:
                if production == '':
                    count_null += 1
                    null_prods.append(key)
                    value.remove(production)
        ...
```
#### UNIT Operation
A unit rule is a rule of the form
A → B,
where A, B are nonterminal symbols. To remove it, for each rule
B → X1 ... Xn,
where X1 ... Xn is a string of nonterminals and terminals, add rule
A → X1 ... Xn
unless this is a unit rule which has already been (or is being) removed. The skipping of nonterminal symbol B in the resulting grammar is possible due to B being a member of the unit closure of nonterminal symbol A.
```python
class UnitOperation:
    @staticmethod
    def do(P: dict[str, list[str]] = None, Vn: list[str] = None, Vt: list[str] = None) -> dict[str, list[str]]:
        if P is None or Vn is None or Vt is None:
            return {}
        for key, value in P.items():
            for production in value[:]:
                if key == production:
                    value.remove(production)
        changes = True
        while changes:
            changes = False
            for key, value in P.items():
                for production in value[:]:
                    if production in Vn:
                        value.remove(production)
                        for prod in P[production]:
                            if prod not in value:
                                value.append(prod)
                        changes = True
        return P
```
#### Order of operations
When choosing the order in which the above transformations are to be applied, it has to be considered that some transformations may destroy the result achieved by other ones. For example, START will re-introduce a unit rule if it is applied after UNIT. The table shows which orderings are admitted.
Moreover, the worst-case bloat in grammar size depends on the transformation order.
Using |G| to denote the size of the original grammar G, the size blow-up in the worst case may range from $|G|^2$ to $2^2$ $|G|$, depending on the transformation algorithm used.
The blow-up in grammar size depends on the order between DEL and BIN. It may be exponential when DEL is done first, but is linear otherwise. UNIT can incur a quadratic blow-up in the size of the grammar.
The orderings START,TERM,BIN,DEL,UNIT and START,BIN,DEL,UNIT,TERM lead to the least (i.e. quadratic) blow-up.
#### Testing
The testing of correct execution is done by the ```TestGrammar``` class that executes the operations on the grammar and returns a new set of production rules. By iterating over them, we can see which operations succeeded or failed.
```python
from Grammar import Grammar
from ChomskyNormalFormConverter import ChomskyNormalFormConverter
from Start import StartOperation
from Bin import BinOperation
from Del import DelOperation
from Term import TermOperation
from Unit import UnitOperation
import unittest
class TestGrammar(unittest.TestCase):
    def __init__(self, grammar:Grammar=None, converter:ChomskyNormalFormConverter=None) -> None:
        self.grammar = grammar
        self.converter = converter
        
    def run(self):
        self.test_start()
        self.test_del()
        self.test_unit()
        self.test_bin()
        self.test_term()
        
    def test_start(self):
        P,S,Vn = self.grammar.productions, self.grammar.start_symbol, self.grammar.nonterminals
        new_P,new_S,new_Vn = StartOperation.do(P=P, S=S, Vn=Vn)
        for prod in new_P.values():
            self.assertNotIn(new_S, prod)
        print("START test passed")
        
    def test_del(self):
        P,S,Vn = self.grammar.productions, self.grammar.start_symbol, self.grammar.nonterminals
        new_P = DelOperation.do(P=P, S=S, Vn=Vn)
        for prod in new_P.values():
            self.assertNotIn("", prod)
        print("DEL test passed")
        
    def test_unit(self):
        P,Vn,Vt = self.grammar.productions, self.grammar.nonterminals, self.grammar.terminals
        new_P = UnitOperation.do(P=P, Vn=Vn, Vt=Vt)
        for prod in new_P.values():
            for production in prod:
                self.assertFalse(len(production) == 1 and production.isupper())
        print("UNIT test passed")
        
    def test_bin(self):
        P,Vn= self.grammar.productions, self.grammar.nonterminals
        new_P = BinOperation.do(P=P, Vn=Vn)
        for prod in new_P.values():
            for production in prod:
                self.assertTrue(len(production) <= 2)
        print("BIN test passed")
        
    def test_term(self):
        P,Vt,Vn,S = self.grammar.productions, self.grammar.terminals, self.grammar.nonterminals,self.grammar.start_symbol
        new_P = TermOperation.do(P=P, Vt=Vt,Vn=Vn,S=S)
        for prods in new_P.values():
            for prod in prods:
                if len(prod) > 1:
                    self.assertTrue(all(char in Vn for char in prod))

        print("TERM test passed")
```
### Execution
To showcase the execution of the program, I have restructured my variant in a ```.json``` file and read it using a ```Variant``` class. Then, with all before-mentioned functional encapsulated in the ```ChomskyNormalFormConverter``` class, I execute them after testing all operations separately in the ```TestGrammar``` class.
```python
from ChomskyNormalFormConverter import ChomskyNormalFormConverter
from Variant import Variant
from Grammar import Grammar
from UnitTests import TestGrammar

variant = Variant('/Users/cristiancretu/Documents/UniCode/LFA/Chomsky Normal Form/variant.json')
production = variant.getP()
terminals = variant.getVT()
non_terminals = variant.getVN()

grammar = Grammar(terminals=terminals, non_terminals=non_terminals, productions=production)
converter = ChomskyNormalFormConverter(grammar)

print(grammar)

test = TestGrammar(grammar=grammar, converter=converter)
test.run()
print("All tests passed",end="\n\n")

new_grammar = converter.transform()
print(new_grammar)
```

Which outputs to this:
```
Vn=['S', 'A', 'B', 'C', 'E']
Vt=['a', 'b']
Start_symbol=S
Productions=
S -> ['bA', 'B']
A -> ['a', 'AS', 'bAaAb']
B -> ['AC', 'bS', 'aAa']
C -> ['', 'AB']
E -> ['BA']

START test passed
DEL test passed
UNIT test passed
BIN test passed
TERM test passed
All tests passed

Vn=['S', 'A', 'B', 'C', 'X', 'D', 'F', 'G', 'H', 'X', 'K', 'L']
Vt=['a', 'b']
Start_symbol=X
Productions=
X -> ['KA', 'AC', 'KS', 'LD', 'L', 'AS', 'KH']
S -> ['KA', 'AC', 'KS', 'LD', 'L', 'AS', 'KH']
A -> ['L', 'AS', 'KH']
B -> ['AC', 'KS', 'LD', 'L', 'AS', 'KH']
C -> ['AB']
D -> ['AL']
F -> ['AK']
G -> ['LF']
H -> ['AG']
K -> ['b']
L -> ['a']
```
## Conclusions
In summary, the CNF converter implementation demonstrates a modular design with each transformation operation encapsulated in its own class, promoting code reusability and readability. Static methods within each class allow for direct invocation of operations, simplifying usage. Error handling mechanisms are incorporated to address potential issues during transformation. Additionally, iterative approaches, like in the UNIT operation, efficiently eliminate unit rules until convergence is achieved. These implementation insights highlight a systematic and robust approach to grammar normalization, ensuring the reliability and versatility of the CNF converter.