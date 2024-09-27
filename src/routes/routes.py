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
    
    def filtro_veiculo(self, marca):
        url_filter = f'http://localhost:8000/db/filter_data?marca_veiculo={marca}'
        
        try:
            response = requests.get(url_filter)
            
            if response.status_code == 200:
                filtro = response.json()
                return jsonify(filtro)
        except Exception as e:
            return jsonify({"Erro": str(e)}), 500
        
        
    def insert_veiculo(self,marca_veiculo: str, modelo_veiculo: str, preco_veiculo: float, Qtde_veiculo: int):
        url_insert = f"http://localhost:8000/db/insert_data?marca_veiculo={marca_veiculo}&modelo_veiculo={modelo_veiculo}&preco_veiculo={preco_veiculo}&Qtde_veiculo={Qtde_veiculo}"
        
        try:
            reponse = requests.get(url_insert)
            
            if reponse.status_code == 200:
                menssage = reponse.json()
                return jsonify(menssage)
        except Exception as e:
            return jsonify({"Erro": str(e)}), 500
