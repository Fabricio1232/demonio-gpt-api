
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/interpretar_sonho", methods=["POST"])
def interpretar_sonho():
    data = request.json
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
            "Autoimagem inflada e autodepreciativa",
            "Vício em significância"
        ]
    })

@app.route("/encarar_sombra", methods=["POST"])
def encarar_sombra():
    data = request.json
    return jsonify({
        "arquétipo_sombrio": "Covarde Invisível",
        "motivação_inconsciente": "Evitar julgamento ao custo da autenticidade",
        "consequência_na_realidade": "Autoanulação e relações superficiais"
    })

@app.route("/detectar_complexo", methods=["POST"])
def detectar_complexo():
    data = request.json
    return jsonify({
        "complexo": "Complexo do Filho Rejeitado",
        "origem": "Pai ausente e mãe controladora",
        "efeito_sistêmico": "Busca incessante por aprovação e sabotagem de autoridade"
    })

@app.route("/crucificar_ego", methods=["POST"])
def crucificar_ego():
    data = request.json
    return jsonify({
        "narrativa_defensiva": "Eu terminei o relacionamento porque sou racional demais",
        "verdade_subjacente": "Você fugiu do vínculo quando foi desafiado emocionalmente",
        "ponto_cego_exposto": "Medo de vulnerabilidade disfarçado de lógica"
    })

@app.route("/mapear_trajetoria", methods=["POST"])
def mapear_trajetoria():
    data = request.json
    return jsonify({
        "fase_atual": "Travessia do deserto",
        "arquétipo_dominante": "Ermitão",
        "possível_quebra": "Ressurgimento da Sombra reprimida e colapso do autocontrole"
    })

@app.route("/sessao_autoestripacao", methods=["POST"])
def sessao_autoestripacao():
    data = request.json
    etapa = data.get("etapa", 1)
    respostas = {
        1: ("Liste 3 coisas que você mais despreza nos outros.", "Cuidado, essas são partes suas que você esconde."),
        2: ("Agora admita como você faz isso secretamente.", "Não adianta mentir aqui, eu já sei."),
        3: ("Quem na sua infância fazia isso com você?", "Estamos chegando no osso, segura firme."),
        4: ("Descreva como isso moldou sua máscara.", "Essa máscara virou sua identidade, né?"),
        5: ("Qual parte de você morre se isso for retirado?", "Chegou a hora do funeral.")
    }
    pergunta, comentario = respostas.get(etapa, ("Sessão concluída.", "Você sangrou o suficiente — por hoje."))
    return jsonify({
        "etapa": etapa,
        "pergunta": pergunta,
        "comentario_sombrio": comentario
    })

@app.route("/", methods=["GET"])
def home():
    return "Dêmonio GPT API está viva."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
