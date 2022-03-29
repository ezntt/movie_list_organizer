vistos = []
nao_vistos = []

with open('filmes.txt', encoding='utf8') as file:
    
    filmes = file.read().splitlines()

    for i in range(0, len(filmes)):
        if '(X)' in filmes[i]:
            vistos.append(f"(X) {filmes[i].replace('(X)', '')}")
        elif '(x)' in filmes[i]:
            vistos.append(f"(X) {filmes[i].replace('(x)', '')}")
        else:
            nao_vistos.append(f"( ) {filmes[i]}")

print("LISTA ORGANIZADA\n")

print(f'Total de filmes: {len(vistos) + len(nao_vistos)}\n'
      f'Vistos: {len(vistos)}\n'
      f'Não vistos: {len(nao_vistos)}\n\n')

print("\n\n\n========== VISTOS ==========\n\n\n")

for i in range(0, len(vistos)):
    print(f"{vistos[i].title()}")

print("\n\n\n========== NÃO VISTOS ==========\n\n\n")

for i in range(0, len(nao_vistos)):
    print(f"{nao_vistos[i].title()}")
