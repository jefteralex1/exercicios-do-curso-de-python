#Conversor de medidas.
dism = float(input("Digite a distância em metros: "))
km = dism / 1000
hm = dism / 100
dam = dism / 10
dm =  dism * 10
cm = dism * 100
mm = dism * 1000
print(f"A distância {dism} metros corresponde a {km} km")
print(f"A distância {dism} metros corresponde a {hm} hm")
print(f"A distância {dism} metros corresponde a {dam} dam")
print(f"A distância {dism} metros corresponde a {dm} dm")
print(f"A distância {dism} metros corresponde a {cm} cm")
print(f"A distância {dism} metros corresponde a {mm} mm")