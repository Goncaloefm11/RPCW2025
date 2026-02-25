# Relatório de Resolução: Ontologia "O Polvo Filosófico"

Este repositório contém a resolução técnica para a gestão de dados do restaurante **O Polvo Filosófico**, utilizando tecnologias da Web Semântica (**OWL**, **RDF** e **SPARQL**).

## 🎯 Objetivos do Projeto
O objetivo foi modelar um domínio complexo com restrições lógicas específicas (como o "não-canibalismo" de polvos) e resolver ambiguidades ontológicas (como o caso do gato Schrödinger).

---

## 🛠️ Resolução das Questões (SPARQL)

Abaixo seguem as queries utilizadas para extrair informações da ontologia desenvolvida.

### Pergunta 1: Quem foram os clientes?
Esta consulta identifica todos os indivíduos classificados como clientes na base de dados.

```sparql
PREFIX owl: [http://www.w3.org/2002/07/owl#](http://www.w3.org/2002/07/owl#)
PREFIX rdfs: [http://www.w3.org/2000/01/rdf-schema#](http://www.w3.org/2000/01/rdf-schema#)
PREFIX rdf: [http://www.w3.org/1999/02/22-rdf-syntax-ns#](http://www.w3.org/1999/02/22-rdf-syntax-ns#)
PREFIX : [http://example.org/polvo-filosofico#](http://example.org/polvo-filosofico#)

SELECT ?nomeCliente WHERE {
    ?nomeCliente rdf:type :Cliente .
}

PREFIX owl: [http://www.w3.org/2002/07/owl#](http://www.w3.org/2002/07/owl#)
PREFIX rdfs: [http://www.w3.org/2000/01/rdf-schema#](http://www.w3.org/2000/01/rdf-schema#)
PREFIX rdf: [http://www.w3.org/1999/02/22-rdf-syntax-ns#](http://www.w3.org/1999/02/22-rdf-syntax-ns#)
PREFIX : [http://example.org/polvo-filosofico#](http://example.org/polvo-filosofico#)

SELECT ?pratos WHERE {
    { ?pratos a :PratoCarnivoro } UNION
    { ?pratos a :PratoVegano } UNION
    { ?pratos a :PratoOntologicamenteAmbiguo }
}

PREFIX owl: [http://www.w3.org/2002/07/owl#](http://www.w3.org/2002/07/owl#)
PREFIX rdfs: [http://www.w3.org/2000/01/rdf-schema#](http://www.w3.org/2000/01/rdf-schema#)
PREFIX rdf: [http://www.w3.org/1999/02/22-rdf-syntax-ns#](http://www.w3.org/1999/02/22-rdf-syntax-ns#)
PREFIX : [http://example.org/polvo-filosofico#](http://example.org/polvo-filosofico#)

SELECT ?Nomeingredientes WHERE {
    ?s :temIngrediente ?Nomeingredientes .
}

PREFIX owl: [http://www.w3.org/2002/07/owl#](http://www.w3.org/2002/07/owl#)
PREFIX rdfs: [http://www.w3.org/2000/01/rdf-schema#](http://www.w3.org/2000/01/rdf-schema#)
PREFIX rdf: [http://www.w3.org/1999/02/22-rdf-syntax-ns#](http://www.w3.org/1999/02/22-rdf-syntax-ns#)
PREFIX : [http://example.org/polvo-filosofico#](http://example.org/polvo-filosofico#)

SELECT ?pessoa WHERE {
    ?pessoa rdf:type :Funcionario ;
            rdf:type :Cliente .
}

```

