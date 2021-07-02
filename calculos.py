#calculos

def soma(primeironumero, segundonumero):
    resultado = primeironumero + segundonumero
    return resultado
primeironumero = 1
segundonumero = 2
print(soma(primeironumero, segundonumero))

def sub(primeironumero, segundonumero):
    resultado = primeironumero - segundonumero
    return resultado
primeironumero = 20
segundonumero = 5
print(sub(primeironumero, segundonumero))

def mult(primeironumero, segundonumero):
    resultado = primeironumero * segundonumero
    return resultado
primeironumero = 25
segundonumero = 5
print(mult(primeironumero, segundonumero))

def div(primeironumero, segundonumero):
    if(segundonumero == 0):
        return "Essa operação e infinita" 
    resultado = primeironumero / segundonumero
    return resultado
primeironumero = 10
segundonumero =  0
print(div(primeironumero, segundonumero))


