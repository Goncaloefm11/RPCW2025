import re
from flask import Flask, render_template
from mquery import exec_query

app = Flask(__name__)

@app.route('/')
@app.route('/livros')
def index():
    q = """
    PREFIX : <http://www.semanticweb.org/gugafm11/ontologies/2026/untitled-ontology-15#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?livroID ?autorID 
        (GROUP_CONCAT(DISTINCT ?tipoID; separator=", ") AS ?tipos) 
        (GROUP_CONCAT(DISTINCT ?linhaID; separator=", ") AS ?linhas) 
        (GROUP_CONCAT(DISTINCT ?eventoID; separator=", ") AS ?eventos) 
    WHERE {
        ?s a ?classe .
        FILTER(?classe IN (:LivroHistorico, :LivroFiccional, :LivroParadoxal))
        
        BIND(STRAFTER(STR(?s), "#") AS ?livroID)
        BIND(STRAFTER(STR(?classe), "#") AS ?tipoID)
        
        OPTIONAL { 
            ?s :saoEscritosPor ?autor .
            BIND(STRAFTER(STR(?autor), "#") AS ?autorID)
        }
        OPTIONAL {
            ?s :existemEm ?linha .
            BIND(STRAFTER(STR(?linha), "#") AS ?linhaID)
        }
        OPTIONAL {
            ?s :refereEvento ?ev .
            BIND(STRAFTER(STR(?ev), "#") AS ?eventoID)
        }
    }
    GROUP BY ?livroID ?autorID
    ORDER BY ?livroID
    """
    res = exec_query(q)
    livros = []
    if res and "results" in res:
        dados = res["results"]["bindings"]
        print(f"DEBUG: Encontrados {len(dados)} resultados")
        
        for row in dados:
            livros.append({
                # Usamos .get() com um valor por defeito para evitar o KeyError
                "id": row["livroID"]["value"],
                "tipo": row.get("tipos", {}).get("value", "Desconhecido"),
                "autor": row.get("autorID", {}).get("value", "N/A"),
                "linhas": row.get("linhas", {}).get("value", "---"),
                "eventos": row.get("eventos", {}).get("value", "---")
            })
    return render_template("lista.html", livros=livros)

@app.route('/livro/<id_livro>')
def rota_detalhe(id_livro):
    # Query específica para um único livro com base no ID clicado
    q = f"""
    PREFIX : <http://www.semanticweb.org/gugafm11/ontologies/2026/untitled-ontology-15#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?p ?o WHERE {{
        :{id_livro} ?p ?o .
    }}
    """
    res = exec_query(q)
    detalhes = []
    if res:
        for row in res["results"]["bindings"]:
            detalhes.append({
                "pred": row["p"]["value"].split("#")[-1],
                "obj": row["o"]["value"].split("#")[-1] if "http" in row["o"]["value"] else row["o"]["value"]
            })
    return render_template("detalhe.html", id=id_livro, detalhes=detalhes)

if __name__ == '__main__':
    app.run(debug=True)