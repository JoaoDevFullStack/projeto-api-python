import requests

# Função para buscar um registro pelo ID
def buscar_registro(id):
    url = f'http://localhost:5200/api/pessoa/{id}'  # URL da sua API C#
    
    try:
        response = requests.get(url)  # Requisição GET para buscar o registro
        
        if response.status_code == 200:
            pessoa = response.json()  # Converte a resposta para formato JSON
            categorizar_idade(pessoa)  # Chama a função para categorizar a idade
        else:
            print(f"Erro ao buscar o registro. Código de status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro na requisição: {e}")

# Função para categorizar a idade
def categorizar_idade(pessoa):
    idade = pessoa['idade']
    categoria = ""
    
    # Categorizar a pessoa com base na idade
    if idade < 30:
        categoria = "Jovem"
    elif 30 <= idade <= 40:
        categoria = "Adulto"
    else:
        categoria = "Sênior"
    
    # Exibir as informações organizadas
    print(f"Nome: {pessoa['nome']}")
    print(f"Idade: {pessoa['idade']} ({categoria})")
    print(f"Cidade: {pessoa['cidade']}")
    print(f"Profissão: {pessoa['profissao']}")
    print("\n")

# Exemplo de como usar a função
id_pessoa = int(input("Digite o ID da pessoa: "))
buscar_registro(id_pessoa)
