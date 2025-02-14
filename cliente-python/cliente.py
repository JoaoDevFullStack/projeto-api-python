import requests


def buscar_registro(id):
    url = f'http://localhost:5200/api/pessoa/{id}'  
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            pessoa = response.json() 
            categorizar_idade(pessoa) 
        else:
            print(f"Erro ao buscar o registro. Código de status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro na requisição: {e}")


def categorizar_idade(pessoa):
    idade = pessoa['idade']
    categoria = ""
    
    if idade < 30:
        categoria = "Jovem"
    elif 30 <= idade <= 40:
        categoria = "Adulto"
    else:
        categoria = "Sênior"
    
    print(f"Nome: {pessoa['nome']}")
    print(f"Idade: {pessoa['idade']} ({categoria})")
    print(f"Cidade: {pessoa['cidade']}")
    print(f"Profissão: {pessoa['profissao']}")
    print("\n")


id_pessoa = int(input("Digite o ID da pessoa: "))
buscar_registro(id_pessoa)
