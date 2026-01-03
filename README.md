# Quem Faz Pokémon? 🃏

**Descrição**

Aplicação em Python que implementa uma versão do jogo "Quem faz o quê?" usando os **tipos de Pokémon** como elementos do baralho. Cada tipo possui relações de vantagem ("Dano duplo a") contra outros tipos, e elas determinam as vitórias entre as cartas jogadas.

---

## ✨ Recursos principais

- Jogo baseado em apostas de vitórias por rodada
- Tipos de Pokémon e suas relações definidas em `pokemon.json`
- Script utilitário `requisicoes_pokemon.py` para buscar relações da [PokéAPI](https://pokeapi.co/)
- Simples IA de robôs para jogar e apostar

---

## 🧩 Estrutura do projeto

- `quem_faz_pokemon.py` — Código principal do jogo. Contém a função `jogar(n_jogadores_robos=1, n_erros=5)` e uma execução direta no fim do arquivo.
- `requisicoes_pokemon.py` — Script que consulta a PokéAPI e monta a estrutura de relações entre tipos (atualmente com parte comentada).
- `pokemon.json` — Arquivo JSON com os tipos e suas relações (`Dano duplo a`, `Dano metade a`, `Sem dano a`).

---

## ▶️ Como jogar

1. Garanta que você tenha Python 3.x instalado.
2. Instale dependências (se for usar `requisicoes_pokemon.py`):

```bash
pip install requests
```

3. Execute o jogo:

```bash
python3 quem_faz_pokemon.py
```

Observações:
- O arquivo roda `jogar(n_jogadores_robos=2)` por padrão; edite esse valor ou importe a função e chame com outros parâmetros.
- Durante o jogo, você será solicitado a apostar quantas vitórias espera obter e escolher um tipo para jogar em cada rodada.

---

## 🔧 Como atualizar `pokemon.json`

`requisicoes_pokemon.py` faz requisições à PokéAPI e pode gerar a estrutura usada em `pokemon.json`. O código para popular as listas (`Dano duplo a`, etc.) está presente, mas parcialmente comentado — é preciso revisar e descomentar para que ele gere o JSON automaticamente.

Exemplo de uso (apenas como referência):

```bash
python3 requisicoes_pokemon.py
```

---

## 🐞 Problemas conhecidos e melhorias sugeridas

- Remover/evitar modificar um dicionário (`jogadores`) durante a iteração (eliminar jogadores enquanto se itera causa comportamento inesperado). ✅
- Tornar a lógica de robôs mais sofisticada (atualmente escolhem a primeira carta e apostam aleatoriamente).
- Adicionar tratamento de empates, mensagens mais claras na interface e testes automatizados.
- Transformar em um CLI com argumentos (`argparse`) para definir número de robôs e erros permitidos.

> Dica: antes de fazer mudanças na eliminação de jogadores, iterate sobre uma cópia das chaves (`for jogador in list(jogadores):`) para evitar problemas ao remover itens durante a iteração.

---

## 🧑‍💻 Como contribuir

- Fork e crie uma branch com sua feature ou correção.
- Abra um PR descrevendo a mudança e como testá-la.
- Sugestões bem-vindas: melhorias na IA de robôs, correções de bugs, melhorias na UX e cobertura de testes.

---

## 📚 Fontes

- Dados de tipos: [PokéAPI — Type](https://pokeapi.co/api/v2/type/)
- Trecho de código consultando a API baseado em resposta no StackOverflow (licença CC BY-SA 4.0).

---

## 📝 Licença

Adicione uma licença (por exemplo MIT) se for abrir o projeto para colaboração pública.

---

## 🤖 Uso de IA para correções e documentação

Este projeto recebeu assistência de um assistente de IA para acelerar correções, testes e documentação. A ajuda incluiu:

- Adição de um `requirements.txt` com dependências (`requests`, `pytest`).
- Correção de um bug na lógica de eliminação de jogadores: foi criada a função `eliminar_jogadores(jogadores, n_erros)` para evitar remover chaves do dicionário enquanto se itera sobre ele.
- Inclusão de testes automatizados (`tests/test_elimination.py`) e execução de `pytest` para validar a correção.
- Atualização da documentação (`README.md`) para registrar as mudanças e instruções de uso.

Recomendações de transparência:
- Sempre inclua um registro (CHANGELOG ou notas de PR) quando aceitar alterações automáticas por IA.
- Revise manualmente todas as mudanças propostas pela IA antes de mesclar em branches principais.

Se desejar, a IA pode também:
- Implementar o script para gerar/atualizar `pokemon.json` automaticamente a partir da PokéAPI (atualmente listada em `requisicoes_pokemon.py`).
- Adicionar testes adicionais e melhorar a IA de robôs para estratégias melhores.

> Observação: a assistência foi feita interativamente com o assistente **GitHub Copilot** (modelo: **Raptor mini (Preview)**). Se preferir, posso usar outra abordagem ou apenas gerar um patch que você revise antes de aplicar.
