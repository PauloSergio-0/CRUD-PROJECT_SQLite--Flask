from flask import Flask, jsonify, request
from routes.routes import Access_data
app = Flask(__name__)




@app.route("/ola")
def hello():
    return jsonify({"menssage": "ola"})

@app.route("/list_data")
def data():
    return Access_data().obter_veiculos()

@app.route("/filter")
def filter_data():
    marca = request.args.get('marca')

    if not marca:
        return jsonify({"Erro": "Marca não fornecida."}), 400
    
    return Access_data().filtro_veiculo(marca.capitalize())

if __name__ == "__main__":
    app.run(debug=True, port=5000)