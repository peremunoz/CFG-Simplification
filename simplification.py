from main import *


def createCFG():  # Create a new CFG
    nonTerminals = input("\t» Input the non terminal symbols separated by whitespaces:\tΣn = ").split()
    terminals = input("\t» Input the terminal symbols separated by whitespaces:\t\tΣt = ").split()
    print("Now we are going to set the productions\nExample usage:\n\tS --> aA|bBb|a\n")
    productions = {}
    for i in range(len(nonTerminals)):
        tempProduction = input(
            "\t» Input the production for the non terminal [" + nonTerminals[i] + "]:\t" + nonTerminals[
                i] + " --> ").split("|")
        productions[nonTerminals[i]] = tempProduction
    startSymbol = input("\t» Input the start symbol:\t").split()
    return CFG(nonTerminals, terminals, productions, startSymbol)


def removeNonGeneratingSymbols(CFGobject: CFG):
    Ω = []
    Σf = []
    #   Identifying the productions with terminal symbols (search char by char)
    for key in CFGobject.P:
        for value in range(len(CFGobject.P[key])):
            isGenerating = True
            for ch in range(len(CFGobject.P[key][value])):
                if CFGobject.P[key][value][ch] not in CFGobject.Σt:
                    isGenerating = False
                    break
            if isGenerating:
                Σf.append(key)
                break

    #   Generating symbols algorithm
    while Σf != Ω:
        Ω = Σf.copy()
        for key in CFGobject.P:
            if key in Σf:
                continue
            for value in range(len(CFGobject.P[key])):
                isGenerating = True
                for ch in range(len(CFGobject.P[key][value])):
                    if CFGobject.P[key][value][ch] not in Σf and CFGobject.P[key][value][ch] not in CFGobject.Σt:
                        isGenerating = False
                        break
                if isGenerating:
                    Σf.append(key)
                    break
    #   Remove from the CFG the symbols that aren't in the Σf set
    i = 0
    k = len(CFGobject.Σn)
    while i < k:
        symbolToCheck = CFGobject.Σn[i]
        if symbolToCheck not in Σf:
            CFGobject.Σn.remove(symbolToCheck)  # Remove from non-terminals set
            CFGobject.P.pop(symbolToCheck)      # Remove its production
            for key in CFGobject.P:
                for value in range(len(CFGobject.P[key])):
                    for ch in range(len(CFGobject.P[key][value])):
                        if CFGobject.P[key][value][ch] not in Σf and CFGobject.P[key][value][ch] not in CFGobject.Σt:
                            CFGobject.P[key].remove(CFGobject.P[key][value])    # Remove all the productions that go to the deleted symbol
            i -= 1
            k -= 1
        i += 1


def removeNonReacheableSymbols(CFGObject: CFG):
    Ω = []
    Σac = CFGObject.S
    while Σac != Ω:
        Ω = Σac.copy()
        for symbol in Σac:
            if symbol in CFGObject.Σt:
                continue
            for value in range(len(CFGObject.P[symbol])):
                for ch in range(len(CFGObject.P[symbol][value])):
                    if CFGObject.P[symbol][value][ch] not in Σac:
                        Σac.append(CFGObject.P[symbol][value][ch])

    i = 0
    k = len(CFGObject.Σn)
    while i < k:
        symbolToCheck = CFGObject.Σn[i]
        if symbolToCheck not in Σac:
            CFGObject.Σn.remove(symbolToCheck)
            CFGObject.P.pop(symbolToCheck)
            i -= 1
            k -= 1
        i += 1

    i = 0
    k = len(CFGObject.Σt)
    while i < k:
        symbolToCheck = CFGObject.Σt[i]
        if symbolToCheck not in Σac:
            CFGObject.Σt.remove(symbolToCheck)
            i -= 1
            k -= 1
        i += 1
