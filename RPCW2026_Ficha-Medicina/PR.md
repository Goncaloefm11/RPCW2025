# RPCW2026-Ficha-Medicina

## Data: 23 de Março de 2026
## Autor: Gonçalo Magalhães
## Disciplina: Representação e Processamento de Conhecimento na Web

---

## 1. Sinopse
[cite_start]O objetivo desta ficha foi avaliar competências na especificação e desenvolvimento de ontologias, bem como o seu povoamento e interrogação utilizando tecnologias da Web Semântica[cite: 7]. [cite_start]O trabalho focou-se no domínio médico, relacionando doenças, sintomas, tratamentos e pacientes[cite: 84].

## 2. Povoamento da Ontologia
[cite_start]Para o povoamento, foi desenvolvido um script em Python (`script.py`) que utiliza a biblioteca `rdflib` para processar os datasets fornecidos:
* [cite_start]**Disease_Syntoms.csv**: Criação de instâncias de `:Disease` e `:Symptom`, estabelecendo a relação `:hasSymptom`.
* **Disease_Description.csv**: Adição de descrições às doenças através de uma nova propriedade de dados[cite: 163].
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
3. Executar a query de **Diagnóstico (Alínea 12)** no GraphDB como um `INSERT` para persistir as relações de diagnóstico.
4. Executar as restantes queries presentes em `sparql.txt` para obter as métricas e listagens solicitadas.

---
**Fim do Relatório**
