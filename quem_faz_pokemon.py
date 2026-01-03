"""
# O jogo "Quem faz o quê?"
Essa é uma aplicação de "Quem faz o quê?" com o baralho de tipos de Pokémon.
Esse é um jogo simples, para jogar basta uma coleção de elementos e uma relação de vitórias.

Nele cada jogador recebe alguns elementos (cartas, tipos, etc) e cada elemento vence outros elementos segundo a relação pré-definida.
Cada jogador deve dizer quantas vitórias ele terá. 

O sistema de pontuação varia a quantia de erros que cada jogador pode ter.
Uma vez que o número de erros é alcançado, o jogador perde.
Último jogador vence.

# Pokémon
Nesse jogo, os elementos são os tipos de Pokémon.
Cada tipo possui relações de vantagem e desvantagem contra outros tipos.

Há 3 tipos de relações: 
1. Dano duplo
2. Dano metade
3. Sem dano

Para esse jogo, vamos considerar apenas o dano duplo.

Como as relações são assimétricas (A pode vencer B, mas B não vence A), será o seguinte:
Se o J1 tem A e o J2 tem B, J1 conta uma vitória contra J2 se A causa dano duplo a B.
Se A e B forem simétircos, os dois ganham.

# REGRAS:
N -> número de tipos que cada jogador possui
J -> número de jogadores
E -> número de erros permitidos

O baralho é composto por 60 cartas, sendo 3 cópias de todos os tipos de Pokémon.

## O Jogo:
Na primira rodada, cada jogador recebe 1 tipo de Pokémon.
A cada rodada, cada jogador recebe mais 1 tipo de Pokémon. 
    E.g. rodada 1: 1 tipo, rodada 2: 2 tipos, etc.
    Se (N + 1) x J > 60, então a próxima rodade volta a ter uma carta e reinicia a contagem.
Cada jogador deve dizer quantos vitórias ele terá (de 0 a N) naquela rodada.
A cada rodada, o jogador joga uma carta (tipo de Pokémon). 
A rodada termina quando todos os jogadores tiverem jogado as N cartas deles.
Deve vencer todos os J jogadores para ter 1 vitória.
Cada jogador pode errar E vezes.
Quem errar E vezes, perde.
Último jogador vence.

# Fonte dos dados
https://pokeapi.co/

## ESTRUTURA DOS DADOS:
1. pokemon.json: dicionário onde a chave é o nome do tipo
2. quem_faz_pokemon.py: jogo "Quem faz o quê?" com tipos de Pokémon

# COMO JOGAR: 
Bastar rodar o arquivo quem_faz_pokemon.py
"""
import json
from random import shuffle

tipos = ""
with open("pokemon.json", "r") as f:
    tipos = json.load(f)

baralho = []
for tipo in tipos.keys():
    for _ in range(3):
        baralho.append(tipo)


def eliminar_jogadores(jogadores, n_erros):
    """Remove players with erros >= n_erros from the jogadores dict and return list of removed player names."""
    eliminados = []
    for jogador in list(jogadores.keys()):
        if jogadores[jogador]["erros"] >= n_erros:
            eliminados.append(jogador)
            jogadores.pop(jogador, None)
    return eliminados

def jogar(n_jogadores_robos = 1, n_erros = 5):
    # Configurações iniciais dos jogadores
    jogadores = {
        "Voce": {
            "erros": 0,
            "tipos": []
        }
    }

    for i in range(n_jogadores_robos):
        jogadores[f"Robo {i+1}"] = {
            "erros": 0,
            "tipos": []
        }
    
    N = 1  # Número de tipos por jogador
    while True:
        # 1. Passo: Embaralhar o baralho
        aux_baralho = baralho.copy()
        shuffle(aux_baralho)

        # 2. Passo: Distribuir os tipos
        # Verifica se é necessário reiniciar a contagem
        if (N + 1) * len(jogadores) > len(baralho):
            N = 1

        # Distribui os tipos para cada jogador
        for jogador in jogadores:
            for _ in range(N):
                if aux_baralho:
                    jogadores[jogador]["tipos"].append(aux_baralho.pop())
        
        # 3. Passo: Cada jogador diz quantas vitórias terá
        apostas = {}
        for jogador in jogadores:
            if jogador == "Voce":
                while True:
                    try:
                        aposta = int(input(f"Quantas vitórias você acha que terá com os tipos {jogadores[jogador]['tipos']}? (0 a {N}): "))
                        if 0 <= aposta <= N:
                            apostas[jogador] = aposta
                            break
                        else:
                            print(f"Por favor, insira um número entre 0 e {N}.")
                    except ValueError:
                        print("Entrada inválida. Tente novamente.")
            else:
                # Lógica simples para robôs: aposta aleatória
                from random import randint
                apostas[jogador] = randint(0, N)
                print(f"{jogador} aposta que terá {apostas[jogador]} vitórias.")

        print()
        
        # 4. Passo: Jogar as cartas
        vitorias = {jogador: 0 for jogador in jogadores}
        for rodada in range(N):
            cartas_jogadas = {}
            # Os robos jogam primeiro
            for jogador in jogadores:
                if jogador != "Voce":
                    # Lógica simples para robôs: joga o primeiro tipo disponível
                    carta = jogadores[jogador]['tipos'].pop(0)
                    cartas_jogadas[jogador] = carta
                    print(f"{jogador} joga o tipo {carta}.")   
            
            for jogador in jogadores:
                if jogador == "Voce":
                    while True:
                        tipos_para_jogar = ""
                        for index, tipo in enumerate(jogadores[jogador]['tipos']):
                            tipos_para_jogar += f"{index + 1} - {tipo} "
                        carta = input(f"Escolha um tipo para jogar nesta rodada (tipos disponíveis: {tipos_para_jogar}): ")
                        
                        for index, tipo in enumerate(jogadores[jogador]['tipos']):
                            if carta == str(index + 1):
                                carta = tipo
                                break
                        
                        if carta in jogadores[jogador]['tipos']:
                            cartas_jogadas[jogador] = carta
                            jogadores[jogador]['tipos'].remove(carta)
                            break
                        else:
                            print("Tipo inválido. Tente novamente.")
        
            # Determinar vencedores da rodada
            for jogador1 in jogadores:
                for jogador2 in jogadores:
                    if jogador1 != jogador2:
                        tipo1 = cartas_jogadas[jogador1]
                        tipo2 = cartas_jogadas[jogador2]
                        
                        if tipos[tipo1]["Dano duplo a"] and tipo2 in tipos[tipo1]["Dano duplo a"]:
                            vitorias[jogador1] += 1
                            print(f"{tipo1} vence {tipo2}!\n")
        
        # 5. Passo: Verificar apostas
        for jogador in jogadores:
            if vitorias[jogador] != apostas[jogador]:
                jogadores[jogador]["erros"] += abs(vitorias[jogador] - apostas[jogador])
                print(f"{jogador} errou a aposta! Erros: {jogadores[jogador]['erros']}/{n_erros}")
            else:
                print(f"{jogador} acertou a aposta!")

        print()
        
        # 6. Passo: Verificar eliminados
        eliminados = eliminar_jogadores(jogadores, n_erros)
        for jogador in eliminados:
            print(f"{jogador} foi eliminado do jogo!")

        N += 1

if __name__ == "__main__":
    jogar(n_jogadores_robos=2)
