print('{:^32}'.format(' E SUAS FUNÇÕES '))
print('-='*16)

def metade(num = 0):
    return num / 2
def dobro(num = 0):
    return num * 2
def diminuir(num = 0, taxa = 0):
    return num - (num * taxa/100)
def aumentar(num = 0, taxa = 0):
    return num + (num * taxa/100)
def moeda(num = 0, moeda = 'R$ '):
    return f'{moeda}{num:.2f}'.replace('.',',')