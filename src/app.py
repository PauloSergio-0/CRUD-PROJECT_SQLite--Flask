from flask import Flask, jsonify, request
from routes.routes import Access_data
app = Flask(__name__)


@app.route("/ola")
def hello():
    return jsonify({"menssage": "ola"})

@app.route("/list_data")
def data():
    return Access_data().obter_veiculos()

@app.route("/filter", methods=["GET"])
def filter_data():
    marca = request.args.get('marca')
    modelo = request.args.get('modelo')
    preco = request.args.get('preco')
    qtde = request.args.get('qtde')
    
    payload = {}
    if marca:
        payload["marca_veiculo"] = marca.capitalize()
        
    if modelo:
        payload["modelo_veiculo"] = modelo.capitalize()
        
    if preco:
        payload["preco_veiculo"] = preco
        
    if qtde:
        payload["qtde_veiculo"] = qtde
    

    # if not marca:
    #     return jsonify({"Erro": "Marca não fornecida."}), 400

    return Access_data().filtro_veiculo(payload)

@app.route("/insert", methods=["POST"])
def insert_data():
    try:
        marca = request.args.get('marca')
        modelo = request.args.get('modelo')
        preco = request.args.get('preco')
        qtde = request.args.get('qtde')
        
    except Exception as e:
        return jsonify({"Erro": f"Esse é o erro {e}"})
    
    return Access_data().insert_veiculo(marca.capitalize(), modelo.capitalize(), preco, qtde)

@app.route("/delete", methods=["DELETE"])
def delete_data():
    
    marca = request.args.get('marca')
    modelo = request.args.get('modelo')

    return Access_data().delete_veiculo(marca_veiculo=marca.capitalize(), modelo_veiculo=modelo.capitalize())


if __name__ == "__main__":
    app.run(debug=True, port=5000)