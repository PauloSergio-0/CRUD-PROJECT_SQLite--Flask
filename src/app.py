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
    marca: str = request.args.get('marca')
    modelo: str = request.args.get('modelo')
    preco = request.args.get('preco')
    qtde = request.args.get('qtde')
    
    payload = {
        k: v.capitalize() for k, v in
            {
            "marca_veiculo": marca,
            "modelo_veiculo": modelo,
            "preco_veiculo":  float(preco) if preco else None,
            "qtde_veiculo": int(qtde) if preco else None
            }.items() if v is not None
        }
    
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
    data = {}
    try:
        marca = request.args.get('marca')
        modelo = request.args.get('modelo')
        
        data = {
            k: v for k, v in {
                "marca_veiculo": marca.capitalize(),
                "modelo_veiculo": modelo.capitalize()
            }.items() if v is not None
        }
        print(data)
    except Exception as e:
        return jsonify({"Erro": f"Esse é o erro {e}"})
    
    return Access_data().delete_veiculo(data)


@app.route("/update", methods = ["POST"])
def update():
    marca_veiculo = request.args.get('marca')
    modelo_veiculo = request.args.get('modelo')
    new_marca = request.args.get('new_marca')
    new_modelo = request.args.get('new_modelo')
    new_preco = request.args.get('new_preco')
    new_qtde = request.args.get('new_qtde')

        
    data_update = {
        k: v for k, v in {
            "marca_veiculo": marca_veiculo.capitalize(),
            "modelo_veiculo": modelo_veiculo.capitalize(),
            "new_marca_veiculo": new_marca.capitalize(),
            "new_modelo_veiculo": new_modelo.capitalize(),
            "new_preco_veiculo": float(new_preco),
            "new_qtde_veiculo": int(new_qtde)
            }.items() if v is not None
        }
    print(data_update)
    return Access_data().update_veiculo(data_update)

if __name__ == "__main__":
    app.run(debug=True, port=5000)