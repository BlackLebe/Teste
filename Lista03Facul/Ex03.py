alt = int(input("Digite o Primeiro elemento: ") )
r = int(input("Digite a Razão: ") )
n = int(input("Qual a posição do número que você quer descobrir? ") )

u = alt + (n-1)*r
u = u + 1

for pa in range(alt, u, r):
    print(pa)