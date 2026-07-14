import sqlite3

# Identificação obrigatória
print("\n--- Teste de Banco de Dados executado por: [Johao, Rafael, Ysack] ---")

# Conexão e Preparação do Banco Local
conexao = sqlite3.connect("banco_do_projeto.db")
cursor = conexao.cursor()

# CORREÇÃO DA LINHA 8: Agora ela está em uma única linha contínua, sem quebrar as aspas
cursor.execute("CREATE TABLE IF NOT EXISTS projetos (id INTEGER PRIMARY KEY, grupo TEXT, tema TEXT)")

# Limpa a tabela para garantir um ambiente de teste isolado e limpo
cursor.execute("DELETE FROM projetos")
conexao.commit()

# ==============================================================================
# AÇÃO: Insira aqui o Nome do seu Grupo e o Tema do Projeto
# ==============================================================================

nome_do_grupo = ""      # <- Substitua pelo nome do seu grupo
tema_do_projeto = "Criação BD"  # <- Substitua pelo tema do seu projeto


# --- CRITÉRIO DE ACEITE: Inserção Única e Validação via SELECT ---
cursor.execute("INSERT INTO projetos (grupo, tema) VALUES (?, ?)", (nome_do_grupo, tema_do_projeto))
conexao.commit()

# Validação via comando SQL (SELECT)
cursor.execute("SELECT grupo, tema FROM projetos WHERE grupo = ?", (nome_do_grupo,))
resultado = cursor.fetchone()

def test_validar_banco_principal():
    assert resultado is not None
    print(f"Teste Principal: Registro encontrado e persistido via SELECT com sucesso!")


# --- DESAFIO BÔNUS: Estresse de Volume (100 registros) ---
print("Iniciando Desafio Bônus: Limpando tabela para carga de 100 registros...")
cursor.execute("DELETE FROM projetos")  # Reseta para garantir a contagem exata de 100
conexao.commit()

print("Inserindo registros no banco...")
for i in range(100):
    cursor.execute("INSERT INTO projetos (grupo, tema) VALUES (?, ?)", (f"Grupo_{i+1}", f"Tema_Carga_{i+1}"))

# Envia tudo de uma vez após o laço
conexao.commit()

# Validação do Desafio Bônus com SELECT COUNT(*) exigido
cursor.execute("SELECT COUNT(*) FROM projetos")
total = cursor.fetchone()[0]

def test_validar_banco_bonus():
    # Valida se o total de registros na tabela é exatamente 100 conforme o enunciado
    assert total == 100
    print(f"SELECT COUNT executado. Total verificado: {total} registros na tabela.")

# Executa as funções de validação caso o arquivo seja rodado diretamente por 'python teste_banco.py'
if __name__ == "__main__":
    test_validar_banco_principal()
    test_validar_banco_bonus()
    conexao.close()