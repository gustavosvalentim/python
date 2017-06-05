class Calc:
    def __init__(self, formula, variaveis):

        self.formula = formula
        self.variaveis = variaveis
        dic = {}

        self.variaveis = self.variaveis.replace(' ', '').replace(',', '')

        for letra in self.variaveis:
            abc = input(letra + ': ')
            dic[letra] = int(abc)

        self.result = eval(self.formula, dic)
