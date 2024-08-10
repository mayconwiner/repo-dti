vendas_produtos = [1500,150,2100,1950]
produtos = ['vinho','cerveja','refrigerante','suco']

lista_aux = list(zip(vendas_produtos,produtos))
lista_aux.sort(reverse=True)
produtos = [produto for vendas,produto in lista_aux]
print(produtos)