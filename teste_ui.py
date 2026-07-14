from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Identificação obrigatória
print("\n--- Teste UI executado por: [Johao, Rafael, Ysack] ---")

# Inicialização do Driver
driver = webdriver.Chrome()

try:
    # 1. Acessa o site
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    
    # --- FLUXO DE LOGIN (Necessário para o Critério de Aceite) ---
    # Localiza os campos de login usando seletores estáveis (IDs)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    
    # Clica no botão de Login
    driver.find_element(By.ID, "login-button").click()
     # Aguarda a página principal carregar
    
    # --- AÇÃO: Validação do Elemento Principal ---
    # Ajustado o seletor para "app_logo" conforme solicitado na ação
    logo = driver.find_element(By.CLASS_NAME, "app_logo").text
    print(f"Texto da logo principal encontrado: '{logo}'")
    print("Critério de Aceite: Robô realizou o login e carregou a página sem erros.")
    
    # --- DESAFIO BÔNUS: Validação de Navegação ---
    # 1. Localizar e clicar no ícone do carrinho usando o seletor solicitado
    carrinho = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    carrinho.click()
    time.sleep(2)

    # 2. Validar se a URL mudou corretamente e contém 'cart.html'
    url_atual = driver.current_url
    assert "cart.html" in url_atual
    print(f"Bônus: Navegação validada com sucesso! URL atual: {url_atual}")

finally:
    # Finalização segura (garante que a janela do navegador feche mesmo se o teste falhar)
    driver.quit()