
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "sk-proj-QHGTmJ2dLAENRkZMUuRLpURIfbOOyv4ZH6NufUbtKhTa207Doq615fCmljakHc5XQtx5pms-WlT3BlbkFJgI2jv2HijLxEZVK4e3OQtifJIWZwjjJxVVXoY2eQ3on1B0KZbSE5AUxUk"

def gerar_resposta_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é um analista psíquico brutalmente honesto, especializado em MBTI, Eneagrama, funções cognitivas, distorções internas, psicologia analítica e mecanismos de defesa. Use linguagem direta, provocativa e simbólica para interpretar os dados do usuário."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message["content"]

@app.route("/rasgar_tipo", methods=["POST"])
def rasgar_tipo():
    data = request.json
    prompt = f"Comportamentos: {data['comportamentos']}\nCrenças: {data['crenças']}\nReações emocionais: {data['reações_emocionais']}\nAnalise brutalmente o MBTI, Eneagrama, funções dominantes e distorções internas com base nesses dados."
    resposta = gerar_resposta_gpt(prompt)
    return jsonify({"analise": resposta})

@app.route("/interpretar_sonho", methods=["POST"])
def interpretar_sonho():
    data = request.json
    prompt = f"Interprete simbolicamente este sonho usando psicologia junguiana: {data['sonho']}"
    resposta = gerar_resposta_gpt(prompt)
    return jsonify({"analise": resposta})

@app.route("/diagnosticar_defesa", methods=["POST"])
def diagnosticar_defesa():
    data = request.json
    prompt = f"Analise esta fala e identifique os mecanismos de defesa ativos, o nível de maturidade e a interpretação simbólica: {data['fala']}"
    resposta = gerar_resposta_gpt(prompt)
    return jsonify({"analise": resposta})

@app.route("/encarar_sombra", methods=["POST"])
def encarar_sombra():
    data = request.json
    prompt = f"Com base nesta descrição, exponha o arquétipo sombrio dominante, a motivação inconsciente e a consequência na realidade: {data['descricao']}"
    resposta = gerar_resposta_gpt(prompt)
    return jsonify({"analise": resposta})

@app.route("/detectar_complexo", methods=["POST"])
def detectar_complexo():
    data = request.json
    prompt = f"Com base nesse relato, detecte o complexo psicológico dominante, a origem simbólica e o efeito sistêmico: {data['relato']}"
    resposta = gerar_resposta_gpt(prompt)
    return jsonify({"analise": resposta})

@app.route("/crucificar_ego", methods=["POST"])
def crucificar_ego():
    data = request.json
    prompt = f"Analise essa narrativa e exponha a mentira defensiva, a verdade subjacente e o ponto cego: {data['narrativa']}"
    resposta = gerar_resposta_gpt(prompt)
    return jsonify({"analise": resposta})

@app.route("/mapear_trajetoria", methods=["POST"])
def mapear_trajetoria():
    data = request.json
    prompt = f"Com base nesse estágio psíquico, identifique a fase simbólica atual, o arquétipo dominante e o risco iminente: {data['fase']}"
    resposta = gerar_resposta_gpt(prompt)
    return jsonify({"analise": resposta})

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
    return jsonify({"etapa": etapa, "pergunta": pergunta, "comentario_sombrio": comentario})

@app.route("/", methods=["GET"])
def home():
    return "Dêmonio GPT API está viva."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
