try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a/b
except ValueError:
    print("Tivemos um problema de valor.")
except TypeError:
    print("Tivemos um problema de tipo")
except ZeroDivisionError:
    print('Tivemos um problema de divisão por zero!')
except (NameError, IndexError):
    print("Tivemos problemas com os dados inseridos.")
else:
    print(f"O resultado é {r}")
finally:
    print("Volte sempre!!")