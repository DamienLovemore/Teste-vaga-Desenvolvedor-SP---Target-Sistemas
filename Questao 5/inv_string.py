texto_usu = input("Digite o texto que sera invertido: ")

texto_rev = ""
for idx in range(len(texto_usu), 0, -1):
    texto_rev += texto_usu[idx-1]

print(f"O texto digitado invertido fica como: {texto_rev}")