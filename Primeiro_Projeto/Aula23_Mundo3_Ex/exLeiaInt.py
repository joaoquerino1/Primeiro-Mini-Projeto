def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print("Erro! Tente novamente digitando um número INTEIRO.")
            continue
        else:
            return n
        
        
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except:
            print("Erro! Tente novamente digitando um número REAL.")
            continue
        else:
            return n


num1 = leiaInt("Digite um número INTEIRO: ")
num2 = leiaFloat("Digite um número REAL: ")
print(f"O numero inteiro digitado foi {num1} e o numero real foi {num2}.")