print('-='*16)
print('{:^32}'.format(' MÓDULOS - PROGRAMA PRINCIPAL '))


import moeda
preco = float(input('Digite o preço R$ '))
print('-='*16)
print('RESULTADO: ')
print()
print(f'A metade de R$ {preco} é R$ {moeda.metade(preco)}') 
print(f'O dobro de R$ {preco} é R$ {moeda.dobro(preco)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preco)}')
print('-='*16)