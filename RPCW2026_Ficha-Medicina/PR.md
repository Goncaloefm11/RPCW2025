# Relatório: RPCW2026-Ficha-Medicina

## Data: 23 de Março de 2026
## Autor: [Teu Nome/ID]
## Disciplina: Representação e Processamento de Conhecimento na Web

---

## 1. Sinopse
[cite_start]O objetivo desta ficha foi avaliar competências na especificação e desenvolvimento de ontologias, bem como o seu povoamento e interrogação utilizando tecnologias da Web Semântica[cite: 7]. [cite_start]O trabalho focou-se no domínio médico, relacionando doenças, sintomas, tratamentos e pacientes[cite: 84].

## 2. Povoamento da Ontologia
[cite_start]Para o povoamento, foi desenvolvido um script em Python (`script.py`) que utiliza a biblioteca `rdflib` para processar os datasets fornecidos[cite: 154]:
* [cite_start]**Disease_Syntoms.csv**: Criação de instâncias de `:Disease` e `:Symptom`, estabelecendo a relação `:hasSymptom`[cite: 160, 162].
* **Disease_Description.csv**: Adição de descrições às doenças através de uma nova propriedade de dados[cite: 163].
* **Disease_Treatment.csv**: Criação de instâncias de `:Treatment` e associação às doenças via `:hasTreatment`[cite: 165, 166].
* **doentes.json**: Criação de instâncias de `:Patient` com IDs únicos, nomes e sintomas exibidos (`:exhibitsSymptom`)[cite: 168].

O processo foi cumulativo, resultando nos ficheiros:
1. `med_doencas.ttl` [cite: 164]
2. `med_tratamentos.ttl` [cite: 167]
3. `med_doentes.ttl` (Ontologia final completa) [cite: 171]

## 3. Interrogação (SPARQL)
As queries desenvolvidas encontram-se no ficheiro `sparql.txt`[cite: 174]. Destacam-se as seguintes funcionalidades:
* [cite_start]**Diagnóstico Automático (Alínea 12)**: Utilização de uma query `CONSTRUCT` para inferir a relação `:hasDisease` baseando-se na correspondência entre os sintomas do paciente e os sintomas característicos da doença[cite: 180].
* [cite_start]**Análise Estatística**: Produção de distribuições de doentes por doença, doenças por sintoma e doenças por tratamento[cite: 182, 183, 184].

## 4. Instruções de Execução
Para replicar os resultados:
1. Executar o script Python: `python3 script.py`.
2. Carregar o ficheiro `med_doentes.ttl` no GraphDB.
3. Executar a query de **Diagnóstico (Alínea 12)** no GraphDB como um `INSERT` para persistir as relações de diagnóstico.
4. Executar as restantes queries presentes em `sparql.txt` para obter as métricas e listagens solicitadas.

---
**Fim do Relatório**
