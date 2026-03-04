# TPC4: Ontologia da Biblioteca Intemporal

## 1. Introdução
Este projeto foca-se na criação, povoamento e interrogação de uma ontologia denominada **Biblioteca Intemporal**. O domínio aborda a gestão de livros que existem em diferentes linhas temporais (Originais e Alternativas), os seus autores, bibliotecários e leitores.

## 2. Objetivos e Requisitos
De acordo com o enunciado da **Semana 4**, o trabalho cumpre os seguintes requisitos:
* **Modelo Ontológico:** Construção de uma hierarquia de classes e propriedades no Protegé.
* **Povoamento Automatizado:** Criação de um script Python utilizando a biblioteca `rdflib` para instanciar 200 indivíduos a partir de datasets JSON.
* **Interrogação SPARQL:** Especificação de 10 queries complexas para extração de informação.

## 3. Estrutura do Modelo
A ontologia baseia-se numa hierarquia de classes organizada para suportar restrições semânticas:

### Classes Principais
* **Agente:** Inclui a classe `Pessoa` e as suas subclasses `Autor`, `Leitor` e `Bibliotecário`.
* **Livros:** Subdivididos em `LivroHistorico`, `LivroFiccional` e `LivroParadoxal`.
* **LinhaTemporal:** Distinção entre `LinhaOriginal` e `LinhaAlternativa`.
* **Eventos:** Classificação entre `EventoHistorico` e `EventoFuturo`.

### Propriedades de Objeto (Object Properties)
* `saoEscritosPor`: Liga um livro ao seu autor.
* `existemEm`: Liga um livro a uma ou mais linhas temporais.
* `refereEvento`: Liga um livro ao evento que descreve.
* `trabalhamEm`: Liga um bibliotecário à sua biblioteca de origem.



## 4. Questões SPARQL Implementadas
As queries desenvolvidas respondem aos seguintes desafios de análise de dados:

1. **Listagem por Contexto:** Identificação de livros em linhas temporais específicas (Original vs Alternativa).
2. **Análise de Paradoxos:** Deteção de livros que desafiam a unicidade temporal por existirem em múltiplas linhas.
3. **Métricas de Autoria:** Contagem e ordenação dos autores mais prolíficos no dataset.
4. **Validação Semântica:** Identificação de inconsistências, como livros históricos que referem eventos futuros.
5. **Gestão de Infraestrutura:** Mapeamento de bibliotecários e as respetivas bibliotecas onde exercem funções.
6. **Casos Específicos:** Interrogação sobre indivíduos específicos do modelo, como o autor Cronos.



## 5. Questões Bónus (Lógica Condicional)
Foram também explorados cenários de ausência de dados utilizando lógica condicional (`OPTIONAL` e `FILTER !bound`):
* Identificação de obras que não possuem eventos associados.
* Deteção de indivíduos que acumulam múltiplas funções (ex: Autores que também são Leitores). (NAO IMPLEMENTADO)

---
**Nota:** Este projeto foi testado utilizando o motor de inferência **HermiT** no Protegé e o repositório **GraphDB** para execução das queries SPARQL.
