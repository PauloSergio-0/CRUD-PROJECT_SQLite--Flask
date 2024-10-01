from flask import  jsonify

import requests

class Access_data:

    def obter_veiculos(self):
        # URL da outra API
        url = 'http://localhost:8000/db/list_data'
        try:
            # Fazendo uma requisição GET para a API externa
            response = requests.get(url)

            # Verificando se a requisição foi bem-sucedida
            if response.status_code == 200:
                carros = response.json()  # Convertendo a resposta JSON para dicionário Python
                return jsonify(carros)  # Retornando os dados para o cliente que acessou seu endpoint
            else:
                return jsonify({"error": "Falha ao acessar a API externa", "status": response.status_code}), response.status_code

        except Exception as e:
            return jsonify({"error": str(e)}), 500  # Retornando erro em caso de falha

    def filtro_veiculo(self, payload: dict):

        url_filter = f'http://localhost:8000/db/filter_data'
        try:
            response = requests.get(url_filter, params=payload)

            if response.status_code == 200:
                filtro = response.json()
                return jsonify(filtro)
        except Exception as e:
            return jsonify({"Erro": str(e)}), 500


    def insert_veiculo(self,marca_v: str = None, modelo_v: str = None, preco_v: float = None, qtde_v:int = None):
        url_insert = f"http://localhost:8000/db/insert_data"

        payload = {
            "marca_veiculo": marca_v,
            "modelo_veiculo": modelo_v,
            "preco_veiculo": preco_v,
            "qtde_veiculo": qtde_v
            }

        for key, values in payload.items():
            if not values:
                return jsonify({"MenssageError": f"Chave {key}: não pode ser vazia"}),400


        try:
            
            reponse = requests.post(url_insert, params=payload)

            if reponse.status_code == 200:
                menssage = reponse.json()
                return jsonify(menssage), 200
        except Exception as e:
            return jsonify({"Erro": str(e)}), 500


    def delete_veiculo(self,payload: dict):
        url_insert = "http://localhost:8000/db/delete_data"
        
        try:
            response = requests.delete(url_insert, params=payload)
            if response.status_code == 200:

                menssage = response.json()
                return jsonify(menssage), 200

        except Exception as e:
            return jsonify({"Erro": str(e)}), 500
        
    def update_veiculo(self, payload: dict):
        url_update = "http://localhost:8000/db/update"
        
    
        if all(payload.get(param) is None for param in ["new_marca_veiculo", "new_modelo_veiculo", "new_preco_veiculo", "new_qtde_veiculo"]):
            return jsonify({"Menssage": "deve passar no minimo um parametro para o update"}), 400
        
        try:
            response = requests.post(url_update, params=payload)
            
            if response.status_code == 200:
                menssage = response.json()
                return jsonify(menssage), 200
            
        except Exception as e:
            return jsonify({"Erro": e}), 500
