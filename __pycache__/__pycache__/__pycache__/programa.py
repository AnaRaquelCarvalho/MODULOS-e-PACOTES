print('-='*26)
print('{:^52}'.format(' RESUMO DO PROGRAMA - PROGRAMA PRINCIPAL '))


import FuncoesPrograma
preco = float(input('Digite o preço R$ '))
FuncoesPrograma.resumo(preco, 20, 12)
