
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/interpretar_sonho", methods=["POST"])
def interpretar_sonho():
    data = request.json
    sonho = data.get("sonho", "")
    return jsonify({
        "arquétipos": ["Sombra", "Anima", "Herói"],
        "símbolos": {
            "cobra": "Transformação e libido reprimida",
            "casa antiga": "Estado psíquico ancestral"
        },
        "análise": "Você está sendo chamado a encarar aspectos negados de si mesmo que estão amadurecendo no inconsciente."
    })

@app.route("/diagnosticar_defesa", methods=["POST"])
def diagnosticar_defesa():
    data = request.json
    fala = data.get("fala", "")
    return jsonify({
        "defesas_identificadas": ["Projeção", "Intelectualização", "Idealização"],
        "nível_de_maturidade": "Neurótica",
        "interpretação": "Você está tentando se distanciar da dor real racionalizando e projetando a fraqueza em terceiros."
    })

@app.route("/rasgar_tipo", methods=["POST"])
def rasgar_tipo():
    data = request.json
    return jsonify({
        "mbti": "INFJ",
        "eneagrama": "4w5 sx/sp",
        "funções_dominantes": ["Ni", "Fe"],
        "distorções": [
            "Martírio simbólico",
            "Autoimagem inflada e simultaneamente autodepreciativa",
            "Vício em significância"
        ]
    })

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
