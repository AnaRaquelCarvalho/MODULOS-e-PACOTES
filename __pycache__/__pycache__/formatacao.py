print('-='*16)
print('{:^32}'.format(' FORMATAÇÃO DE MOEDAS - PROGRAMA PRINCIPAL '))


import format
preco = float(input('Digite o preço R$ '))
print('-='*16)
print('RESULTADO: ')
print()
print(f'A metade de  {format.moeda(preco)} é {format.moeda(format.metade(preco))}')
print(f'O dobro de  {format.moeda(preco)} é {format.moeda(format.dobro(preco))}')
print(f'Aumentando 10%, temos {format.moeda(format.aumentar(preco, 10))}')
print(f'Diminuir 10%, temos {format.moeda(format.diminuir(preco, 10))}')
print('-='*16)