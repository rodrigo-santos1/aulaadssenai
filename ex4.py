class Calculadora:
    def mult(self, a, b):
        return a*b
    def divisao(self, a, b):
        if b == 0:
            return ("Não dividimos por 0")
        else:
            return(a/b)
        
calc = Calculadora
print(calc.divisao(5,0))
print(calc.mult(5*0))