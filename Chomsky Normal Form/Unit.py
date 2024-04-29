class UnitOperation:
    @staticmethod
    def do(P: dict[str, list[str]] = None, Vn: list[str] = None, Vt: list[str] = None) -> dict[str, list[str]]:
        if P is None or Vn is None or Vt is None:
            return {}

        # Remove unit productions
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
