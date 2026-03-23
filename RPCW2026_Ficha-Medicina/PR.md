# RPCW2026-Ficha-Medicina

## Data: 23 de Março de 2026
## Autor: Gonçalo Magalhães PG61524
## Disciplina: Representação e Processamento de Conhecimento na Web

---

## 1. Sinopse
O objetivo desta ficha foi avaliar competências na especificação e desenvolvimento de ontologias, bem como o seu povoamento e interrogação utilizando tecnologias da Web Semântica.O trabalho focou-se no domínio médico, relacionando doenças, sintomas, tratamentos e pacientes.

## 2. Povoamento da Ontologia
Para o povoamento, foi desenvolvido um script em Python (`script.py`) que utiliza a biblioteca `rdflib` para processar os datasets fornecidos:
**Disease_Syntoms.csv**: Criação de instâncias de `:Disease` e `:Symptom`, estabelecendo a relação `:hasSymptom`.
* **Disease_Description.csv**: Adição de descrições às doenças através de uma nova propriedade de dados.
* **Disease_Treatment.csv**: Criação de instâncias de `:Treatment` e associação às doenças via `:hasTreatment`.
* **doentes.json**: Criação de instâncias de `:Patient` com IDs únicos, nomes e sintomas exibidos (`:exhibitsSymptom`).

O processo foi cumulativo, resultando nos ficheiros:
1. `med_doencas.ttl` 
2. `med_tratamentos.ttl`
3. `med_doentes.ttl` (Ontologia final completa)

## 3. Interrogação (SPARQL)
As queries desenvolvidas encontram-se no ficheiro `sparql.txt`. Destacam-se as seguintes funcionalidades:
**Diagnóstico Automático (Alínea 12)**: Utilização de uma query `CONSTRUCT` para inferir a relação `:hasDisease` baseando-se na correspondência entre os sintomas do paciente e os sintomas característicos da doença.
**Análise Estatística**: Produção de distribuições de doentes por doença, doenças por sintoma e doenças por tratamento.

## 4. Instruções de Execução
Para replicar os resultados:
1. Executar o script Python: `python3 script.py`.
2. Carregar o ficheiro `med_doentes.ttl` no GraphDB.
3. Executar as queries presentes em `sparql.txt` para obter as métricas e listagens solicitadas.
4. Executar a query de **Diagnóstico (Alínea 12)** no GraphDB como o `CONSTRUCT` e depois com o `INSERT` para que sejam atualizados os dados.

---
**Fim do Relatório**
