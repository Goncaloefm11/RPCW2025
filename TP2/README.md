# Ontologia de Cinema (Cinema Ontology)

Uma ontologia estruturada em **OWL (Web Ontology Language)** que descreve o domínio do cinema, focando-se na classificação de filmes, profissionais da indústria e as relações entre personagens e obras.

## Visão Geral
Esta ontologia permite modelar o conhecimento sobre produções cinematográficas, estabelecendo relações complexas entre filmes, realizadores, atores e géneros. Graças à lógica descritiva integrada, a ontologia é capaz de realizar **inferências automáticas** (ex: classificar uma Pessoa como Ator se ela atuar num filme).

## Estrutura da Ontologia

### 1. Classes Principais
* **Filme**: Classe base para todas as obras. Inclui subclasses inferidas como:
    * `longasMetragens`: Filmes com duração superior a 60 minutos.
    * `FilmesInteressantes`: Filmes que possuem 2 ou mais géneros associados.
    * **Géneros**: `FilmesAventura`, `FilmesTerror`, `FilmesRomanticos`, `FilmesDramáticos` e `FilmesInfantis`.
* **Pessoa**: Classe base para indivíduos, com subclasses dinâmicas:
    * `Ator`: Qualquer pessoa que possua a propriedade `Atuou` ligada a um Filme.
    * `Realizador`: Qualquer pessoa que `realizou` um Filme.
    * `Escritor` / `Músico`: Autores de argumentos, livros ou bandas sonoras.
* **Género**: Classe definida por uma enumeração (Ação, Aventura, Comédia, Drama, Ficção, Infantil, Romance, Terror e Thriller).
* **Personagem**: Representa os papéis interpretados nas obras.

### 2. Propriedades Principais
* **Object Properties**:
    * `atuou` / `temAtor`: Define a participação de atores em filmes.
    * `realizou` / `foiRealizado`: Define a direção técnica da obra.
    * `representa`: Liga um Ator a uma Personagem específica.
    * `temGénero`: Associa um filme à sua categoria temática.
* **Data Properties**:
    * `titulo`: Nome da obra (string).
    * `duracao`: Tempo de execução em minutos (integer).
    * `data`: Data de lançamento (string).
    * `temSexo`: Identificador de género biográfico ("M" ou "F").

## Casos de Estudo (Dados Reais)
A ontologia inclui dados detalhados para três filmes de referência:

| Filme | Realizador | Géneros | Personagens Principais |
| :--- | :--- | :--- | :--- |
| **Madagascar 2** | Tom McGrath, Eric Darnell | Aventura, Infantil | Alex, Marty, Melman, Gloria |
| **Scary Movie** | Keenen Ivory Wayans | Terror | Cindy, Bobby, Shorto, Idiota |
| **Twilight** | Catherine Hardwicke | Drama, Romance, Thriller | Bella Swan, Edward Cullen |

## Como Utilizar
1. Instale o [Protégé](https://protege.stanford.edu/).
2. Carregue o ficheiro `Cinema(3filmes).ttl`.
3. Ative um raciocinador (Reasoner), como o **HermiT** ou o **Pellet**, para visualizar as classes inferidas.
4. Utilize a aba **DL Query** para fazer perguntas à ontologia (ex: `Pessoa and Atuou some FilmesTerror`).
