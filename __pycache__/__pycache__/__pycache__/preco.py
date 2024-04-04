print('-='*16)
print('{:^32}'.format(' FORMATAÇÃO DE MOEDAS - PROGRAMA PRINCIPAL '))


import Funpreco
preco = float(input('Digite o preço R$ '))
print('-='*16)
print('RESULTADO: ')
print()
print(f'A metade de  {Funpreco.moeda(preco)} é {Funpreco.metade(preco, True)}')
print(f'O dobro de  {Funpreco.moeda(preco)} é {Funpreco.dobro(preco, True)}')
print(f'Aumentando 10%, temos {Funpreco.aumentar(preco, 10, True)}')
print(f'Diminuir 10%, temos {Funpreco.diminuir(preco, 10, True)}')
print('-='*16)