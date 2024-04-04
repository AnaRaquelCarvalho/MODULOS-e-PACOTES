print('-='*16)
print('{:^32}'.format(' MÓDULOS - PROGRAMA PRINCIPAL '))


from valor import metade, dobro, aumentar, diminuir
preco = float(input('Digite o preço R$ '))
print('-='*16)
print('RESULTADO: ')
print()
print(f'A metade de R$ {preco} é R$ {metade(preco)}')
print(f'O dobro de R$ {preco} é R$ {dobro(preco)}')
print(f'Aumentando 10%, temos {aumentar(preco, 10)}')
print(f'Diminuir 10%, temos {diminuir(preco, 10)}')
print('-='*16)