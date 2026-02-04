# Manifesto: TPC1 - Ontologia da História e Dataset de Compras

**Data:** 2026-02-04
**Unidade Curricular:** Representação e Processamento de Conhecimento na Web (RPCW2025)
**Autor:** Gonçalo Emanuel Ferreira Magalhães (Pg16524)

## Resumo
Este trabalho consistiu na criação de uma ontologia baseada numa história sobre a aprendizagem de línguas na Universidade do Minho. O objetivo foi modelar classes, propriedades e indivíduos no software **Protégé** e exportar o resultado no formato Turtle (TTL). Adicionalmente, foi explorada a geração automática de ontologias a partir de datasets JSON.

## Exercícios Realizados

### 1. Ontologia da História
Foi modelada a história do Eduardo, um estudante de 21 anos oriundo do Porto.
- **Classes Criadas:** `Pessoa`, `Lingua`, `Curso`, `Universidade`, `Cidade`.
- **Propriedades de Objeto:** `falaLingua`, `naturalDe`, `inscritoEm`, `parceiroDe`, `leciona`.
- **Propriedades de Dados:** `temIdade`, `diaDaAula`.
- **Indivíduos:** Eduardo, Carlos, Ana, Helmut Ratz, Hanna e respetivas entidades relacionadas (como línguas e a Universidade do Minho).

### 2. Questões Respondidas via DL Query
Após a execução do Reasoner no Protégé, a ontologia permite responder a:
1. **Quantas línguas fala o Eduardo?** Português, Espanhol, Inglês e Alemão.
2. **Quem se inscreveu no curso de alemão?** Eduardo, Carlos e Ana.
3. **Quem é Hanna?** Uma estudante alemã de biotecnologia e parceira de aprendizagem do Eduardo.

### 3. Dataset de Compras
Análise de um dataset JSON contendo listas de compras.
- Especificação do modelo ontológico para suportar `Lista`, `Produto`, `Categoria` e `Quantidade`.
- Preparação de uma script Python para a geração automática de indivíduos a partir do ficheiro JSON.

## Ficheiros Incluídos
- `README.md`: Este manifesto.
- `historia.ttl`: Ontologia final da história em formato Turtle.
- `semana1.pdf`: Enunciado dos exercícios.
