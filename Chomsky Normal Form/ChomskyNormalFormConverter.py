from Grammar import Grammar
from Variant import Variant


class ChomskyNormalFormConverter:
    
    def __init__(self, grammar_to_convert:Grammar) -> None:
        self.grammar:Grammar = grammar_to_convert
        
       
    def remove_epsilon_production(self):
        new_production = self.__replace_starting_non_terminal(productions=self.grammar.productions)
        print(new_production)
        empty_productions = self.__find_initial_epsilon_productions(productions=self.grammar.productions)
        new_production = self.__derive_epsilon_productions(productions=new_production, empty_found=empty_productions)
        print(new_production)
        
    def __replace_starting_non_terminal(self, productions:dict=None):
        """This function replaces the starting non-terminal with a new non-terminal
        ----------
        Args:
            productions (dict, optional): This is the dictionary that contains the productions. Defaults to None.
        ----------
        Returns:
            dict: For the ease of use and clearness, this function adds a T instead of S0 and will will make it to produce S.
        """
        starting = "S"
        new_starting = "T"
        productions[new_starting] = [starting]
        return productions
    
    def __find_initial_epsilon_productions(self, productions:dict=None):
        empty_productions = {}
        for symbol in productions:
            options = productions[symbol]
            if len(options)>1:
                for result in options:
                    if result == 'empty' or result=='$':
                        # Let's denote empty strings with a dollar symbol cuz why not
                        productions[symbol]=['$']
                        empty_productions.update({symbol:result})
                        print(f'Found epsilon production {symbol} -> {result}')
        return empty_productions 
 

    def __derive_epsilon_productions(self, productions:dict=None, empty_found:dict=None):
        for symbol in productions:
            possible_productions = productions[symbol]
            if len(possible_productions)>1:
                for result in possible_productions:
                    for production_symbol in result:
                        if production_symbol in list(empty_found.keys()):
                            new_production = result.replace(production_symbol,'$')
                            productions[symbol].append(new_production)
            else:
                result = possible_productions[0]
                for symbol in result:
                    if symbol in empty_found:
                        new_production=result.replace(symbol,'$')
                        productions[symbol].append(new_production)
        return productions






 
        
variant = Variant('/home/flexksx/Documents/Labs/LabsLFA/Chomsky Normal Form/variant.json')
production = variant.getP()
terminals = variant.getVT()
non_terminals = variant.getVN()
# print(production)
# print(terminals)
# print(non_terminals)

grammar = Grammar(terminals=terminals, non_terminals=non_terminals, productions=production)
converter = ChomskyNormalFormConverter(grammar)
converter.remove_epsilon_production()