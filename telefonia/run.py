import json

class Sessao:
    """
    Representa uma unica sessao de telefonia, com numero e dados.
    Equivalente a classe 'Sessao' do Java.
    """
    def __init__(self, numero_celular, dados_sessao):
        self.numero_celular = numero_celular
        self.dados_sessao = dados_sessao

    def __str__(self):
        # Formata a saida para ser mais legivel.
        try:
            dados_formatados = json.dumps(json.loads(self.dados_sessao), indent=4)
            return f"Numero: {self.numero_celular}\nDados:\n{dados_formatados}"
        except:
            return f"Numero: {self.numero_celular}\nDados: {self.dados_sessao}"

def carregar_sessoes(nome_arquivo="telephony_sessions.txt"):
    """
    Le o arquivo de log e retorna um dicionario com as sessoes.
    O dicionario funciona como um HashMap, usando o numero como chave.
    """
    sessoes_map = {}
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                if ';' in linha:
                    numero, dados = linha.strip().split(';', 1)
                    sessoes_map[numero] = Sessao(numero, dados)
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' nao encontrado.")
    
    return sessoes_map

def main():
    """
    Funcao principal que controla o menu e a interacao com o usuario.
    """
    # Carrega os dados do arquivo para a memoria.
    sessoes = carregar_sessoes()
    
    if not sessoes:
        print("Nenhuma sessao carregada. Encerrando.")
        return

    print(f"\n{len(sessoes)} sessoes carregadas.")

    # Loop principal do menu.
    while True:
        print("\n--- Menu ---")
        print("1. Buscar por numero")
        print("2. Sair")
        
        opcao = input("Escolha uma opcao: ")
        
        if opcao == '1':
            celular_busca = input("Digite o numero do celular: ")
            
            # Busca o numero no dicionario.
            sessao_encontrada = sessoes.get(celular_busca)
            
            if sessao_encontrada:
                print("\n--- Sessao Encontrada ---")
                print(sessao_encontrada)
            else:
                print("\nNumero nao encontrado.")
                
        elif opcao == '2':
            print("Saindo...")
            break
            
        else:
            print("Opcao invalida.")

# Ponto de entrada do programa.
if __name__ == "__main__":
    main()
