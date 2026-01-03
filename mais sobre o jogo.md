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