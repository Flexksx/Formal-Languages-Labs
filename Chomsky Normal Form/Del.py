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
        for i in range(count_null):
            new_P = P.copy()  # Make a copy of P
            for key, value in P.items():
                for production in value:
                    for character in production:
                        if character == null_prods[i]:
                            new_productions = DelOperation.create_new_productions(production, null_prods[i])
                            for j in new_productions:
                                if j not in new_P[key]:
                                    new_P[key].append(j)
                            break
            P.update(new_P)
        
        return P

    @staticmethod
    def create_new_productions(production: str, character: str) -> list[str]:
        results = []
        for i in range(len(production)):
            if production[i] == character:
                new_production = production[:i] + production[i + 1:]
                results.append(new_production)
        return results
