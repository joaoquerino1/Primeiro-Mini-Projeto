def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(res)
   
def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)

   
def metade(preço=0, formato=False):
    res = preço/2
    return res if not formato else moeda(res)
 

def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda="R$"):
    return f'{moeda}{preço:>.2f}'.replace('.',',')


def resumo(preço=0, taxaa=10, taxar=5):
    print("-="*30)
    print("RESUMO DO VALOR".center(30))
    print("-="*30)
    print(f'Preço analisado: {moeda(preço)}')
    print(f"O dobro do preço: {dobro(preço, True)}")
    print(f"Metade do preço: {metade(preço, True)}")
    print(f"Com {taxaa}% de aumento: {aumentar(preço, taxaa, True)}")
    print(f"Com {taxar}% de redução: {diminuir(preço, taxar, True)}")
    print("-="*30)
    
    
def leiaDinheiro(msg):
    válido=False
    while not válido:
        entrada=str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada=='':
            print(f"ERRO. {entrada} é um preço inválido!")
        else:
            válido=True
            return float(entrada)
        