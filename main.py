import simplification


class CFG:
    Σn: list
    Σt: list
    P: dict
    S: list

    def __init__(self, nonTerminals: list, terminals: list, productions: dict, startSymbol: list):
        self.Σn = nonTerminals
        self.Σt = terminals
        self.P = productions
        self.S = startSymbol

    def print(self, text):
        print('\n' + text + '\n')
        print('G = ({' + ', '.join(self.Σn) + '}, {' + ', '.join(self.Σt) + '}, P, ' + self.S[0] + ')\n')
        print('P:')
        for i in range(len(self.Σn)):
            print(self.Σn[i] + ' --> ', end='')
            print(*(x for x in self.P[self.Σn[i]]), sep='|')

    def simplify(self):
        self.print('The CFG entered is:')
        simplification.removeNonGeneratingSymbols(self)
        simplification.removeNonReachableSymbols(self)
        self.print('The CFG simplified is:')


def createCFG():
    return simplification.createCFG()


if __name__ == "__main__":
    print("Welcome to the CFG Simplification program :)\n")
    CFG = createCFG()
    CFG.simplify()

