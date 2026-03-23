# 📚 Biblioteca Temporal - Sistema de Gestão de Ontologias

Este projeto é uma aplicação web desenvolvida em **Flask** que consome uma ontologia alojada num servidor **GraphDB**. O sistema permite navegar por um catálogo de livros que existem em diferentes linhas temporais e referenciam eventos históricos ou futuros.

---

## 🛠️ Tecnologias Utilizadas

* **Python / Flask**: Backend e rotas da aplicação.
* **SPARQL**: Linguagem de consulta para extrair dados da ontologia.
* **GraphDB**: Base de dados orientada a grafos (RDF).
* **W3.CSS / Font Awesome**: Estilização da interface e ícones.
* **Jinja2**: Motor de templates para renderizar o HTML dinâmico.

---

## 📂 Estrutura do Projeto

* `app.py`: Servidor principal com as rotas para o catálogo e detalhes.
* `mquery.py`: Módulo de ligação e execução de queries no endpoint do GraphDB.
* `templates/`: Contém os ficheiros HTML (`layout.html`, `lista.html`, `detalhe.html`).
* `biblioteca_temporal_populated.ttl`: Ficheiro da ontologia em formato Turtle.

---

## 🚀 Como Executar

### 1. Configurar o GraphDB
* Cria um repositório chamado `linhaTemporal`.
* Faz o upload e o import do ficheiro `.ttl` fornecido (`biblioteca_temporal_populated.ttl`).

```bash
pip install flask SPARQLWrapper
