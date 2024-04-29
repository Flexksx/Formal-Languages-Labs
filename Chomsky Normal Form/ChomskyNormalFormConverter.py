from Grammar import Grammar
from Variant import Variant
from Start import StartOperation
from Term import TermOperation
from Bin import BinOperation
from Del import DelOperation
from Unit import UnitOperation
class ChomskyNormalFormConverter:
    def __init__(self, grammar: Grammar) -> None:
        self.grammar = grammar
    
    def transform(self):
        S = 'S'
        P = self.grammar.productions
        Vn = self.grammar.nonterminals
        Vt = self.grammar.terminals
        P, S, Vn = StartOperation.do(P=P, S=S, Vn=Vn)
        P = DelOperation.do(P=P, S=S, Vn=Vn)
        P = UnitOperation.do(P=P, Vn=Vn, Vt=Vt)
        P = TermOperation.do(P=P, S=S, Vn=Vn, Vt=Vt)
        P = BinOperation.do(P=P, Vn=Vn)
        P, Vn = self.remove_inaccessible_symbols(P, S, Vn)
        return Grammar(non_terminals=Vn, terminals=Vt, productions=P, start_symbol=S)

    def remove_inaccessible_symbols(self, P: dict[str, list[str]], S: str, Vn: list[str]) -> tuple[dict[str, list[str]], list[str]]:
        accessible = {S}
        queue = [S]

        while queue:
            current = queue.pop(0)
            for production in P.get(current, []):
                for symbol in production:
                    if symbol in Vn and symbol not in accessible:
                        accessible.add(symbol)
                        queue.append(symbol)

        Vn = [nt for nt in Vn if nt in accessible]
        new_P = {nt: P[nt] for nt in P if nt in accessible}

        return new_P, Vn



    

