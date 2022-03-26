# Nosso time de futebol terminou o campeonato. O resultado de cada correspondência é semelhante a "x: y". Os resultados de todas as partidas são registrados na coleção.
# Por exemplo: [" 3: 1 "," 2: 2 "," 0: 1 ", ...]
# Escreva uma função que leve essa arrecadação e conte os pontos da nossa equipe no campeonato. Regras para contagem de pontos para cada partida:
# - se x> y - 3 pontos
# - se x <y - 0 ponto
# - se x = y - 1 ponto
# OBS: há 10 partidas no campeonato

placares = ["3:1", "2:2", "0:1", "2:0", "5:1", "3:2", "1:2", "6:3", "7:2", "3:0"]

soma_pontos = 0
for v in placares:
    v1, v2 = v.split(":")
    if v1 > v2:
        soma_pontos += 3
    elif v1 < v2:
        soma_pontos += 0
    else:
        soma_pontos += 1
print(soma_pontos)
