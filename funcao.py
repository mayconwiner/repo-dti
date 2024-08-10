meta = 10000
vendas = {
    'João': 15000,
    'Julia': 27000,
    'Marcus': 9900,
    'Maria': 37500,
    'Ana': 10300,
    'Alon': 7870
}

def preco_final(preco, **adicionais):
    print(adicionais)
    if 'desconto' in adicionais:
        preco *= (1 - adicionais['desconto'])
    if 'garantia_extra' in adicionais:
        preco += adicionais['garantia_extra']
    if 'imposto' in adicionais:
        preco *= (1 + adicionais['imposto'])
    return preco

def calculo_meta(meta,vendas):
    '''Calcula a porcentagem de vendedores que bateram a meta e retorna uma lista com os vendedores que bateram a meta'''
    bateram_meta = []
    for vendedor in vendas:
        if vendas[vendedor] >= meta:
            bateram_meta.append(vendedor)
    perc_baterammeta = len(bateram_meta) / len(vendas) * 100
    '''Retorna a porcentagem de vendedores que bateram a meta e uma lista com os vendedores que bateram a meta'''
    return perc_baterammeta,bateram_meta

p_meta, vendedores_acima_meta = calculo_meta(meta, vendas)
print(p_meta)
print(vendedores_acima_meta)





