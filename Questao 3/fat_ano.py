import os
import json

# Abre e le o arquivo json
cur_caminho = os.path.dirname(__file__)
nov_caminho = cur_caminho + '\dados.json'
arquivo_json = open(nov_caminho)
dados_json = json.load(arquivo_json)


#Armazena todas as faturas em um vetor
#so com os valores
faturas_ano = []
for dados_dia in dados_json:
    faturas_ano.append(dados_dia["valor"])

pri_val = True
min_fat = 0
max_fat = 0

med_anu = 0
num_dias_med = 0
num_dias_max = 0

for fat_dia in faturas_ano:
    if fat_dia == 0:
        continue

    if pri_val:
        min_fat = fat_dia
        max_fat = fat_dia
        pri_val = False
    else:
        if fat_dia < min_fat:
            min_fat = fat_dia
        elif fat_dia > max_fat:
            max_fat = fat_dia

    num_dias_med += 1
    med_anu += fat_dia

med_anu /= num_dias_med

for fat_dia in faturas_ano:
    if fat_dia > med_anu:
        num_dias_max += 1

print(f"A menor fatura diaria do ano foi de: {min_fat}")
print(f"A maior fatura diaria do ano foi de: {max_fat}")
print(f"A media das faturas desse ano e de: {med_anu}")
print(f"A quantidade de dias que teve faturas maior que a media anual foi de: {num_dias_max}")
