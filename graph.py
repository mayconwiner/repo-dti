import matplotlib.pyplot as plt
vendas_meses = [1500, 1700, 2000, 1900, 1800, 1950, 2100, 2200, 2300, 2400, 2500, 2600]
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

plt.plot(meses, vendas_meses)
plt.xlabel('Meses')
plt.ylabel('Vendas')
plt.axis([0, 12, 0, max(vendas_meses) + 500])
plt.show()

