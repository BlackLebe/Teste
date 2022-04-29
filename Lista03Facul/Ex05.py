#Excecicio nao forneceu quanto inteiro tem que parar ou seja break.
pares=0
imper=0
n=int(input("digite certa numero inteiro e não negativo: "))
while n>=0:
  if n % 2 !=0:
    imper+=1
  else:
    pares+=1
print("soma de pares: ",pares,"soma de imper: ",imper)