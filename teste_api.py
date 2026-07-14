import requests
import pytest
def test_verificar_api():
	# Identificação obrigatória
	print("\n--- Teste de API executado por: [Rafael, Ysack, Johao] ---")
	# URL estável da JSONPlaceholder
	url = "https://jsonplaceholder.typicode.com/users"
	resposta = requests.get(url)
	# Validação do status code
	assert resposta.status_code == 200
	print(f"Status {resposta.status_code} recebido com sucesso.")
# --- Desafio Bônus ---
def test_verificar_api_falha():
	# Testando um ID que não existe para validar o erro 404
	url_falha = "https://jsonplaceholder.typicode.com/users/9999"
	resposta = requests.get(url_falha)
	assert resposta.status_code == 404
	print(f"Teste de falha validado: Status {resposta.status_code} recebido.")