# ===== Sistema Acadêmico =====

# Dicionário global para armazenar os dados dos alunos
sistema_academico = {}
import os
import time

def adicionar_aluno(sistema, nome, nota1, nota2, nota3):
    """Adiciona um aluno com notas, média e situação ao sistema acadêmico."""
    media = (nota1 + nota2 + nota3) / 3
    situacao = "Aprovado" if media >= 7.0 else "Reprovado"
    
    sistema[nome] = {
        "notas": [nota1, nota2, nota3],
        "media": media,
        "situacao": situacao
    }
    
    print(f"✅ Aluno '{nome}' adicionado com média {media:.2f} e situação '{situacao}'.")
    os.system('cls')


def exibir_boletim(sistema):
    """Exibe o boletim de todos os alunos do sistema acadêmico."""
    if not sistema:
        print("⚠ Não há alunos cadastrados no sistema.")
        time.sleep(3)
        os.system('cls')
       
    else:
        print("\n📄 Boletim dos alunos:")
        for nome, dados in sistema.items():
            print(f"\nAluno: {nome}")
            print(f"Notas: {dados['notas']}")
            print(f"Média: {dados['media']:.2f}")
            print(f"Situação: {dados['situacao']}")

def Usuarios():
    usuarios = [{
        "Nome": "Pamela", 
        "Senha": "1234Pa",
    },
    {
        "Nome": "Luca", 
        "Senha": "1234Lu",
    }]
    return usuarios


def Login():

    while True:
        print("\n******   Sistema Acadêmico Escolar ******")
        usuario = (input("Digite seu login: "))
        senha = (input("Digite a senha: "))
        usuarios = Usuarios()
        for i in usuarios:
            if usuario == i["Nome"]:
                if senha == i["Senha"] :
                    print("Acesso permitido!")
                    time.sleep(2)
                    os.system('cls')
                    main()
                else :
                    print("Login ou senha incorreto. Tente novamente!")
                    time.sleep(2)
                    os.system('cls')
                    Login()
           
        print("Usuario não encontrado")
        time.sleep(2)
        os.system('cls')
def main():
    """Função principal que executa o menu do sistema acadêmico."""
    while True:
        print("\n******   Sistema Acadêmico Escolar ******")
        print("\n1 - Boletim de alunos")
        print("2 - Adicionar aluno(a)")
        print("0 - Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("❌ Entrada inválida. Por favor, digite um número.")
            continue
       
        

        if opcao == 1:
            exibir_boletim(sistema_academico)
            

        elif opcao == 2:
            try:
                os.system('cls')
                print("\n****** Sistema Acadêmico ******")
                quantidade = int(input("\nQuantos alunos você deseja adicionar? "))
                for _ in range(quantidade):
                    nome = input("Digite o nome do aluno(a): ")
                    nota1 = float(input("Nota do primeiro bimestre: "))
                    nota2 = float(input("Nota do segundo bimestre: "))
                    nota3 = float(input("Nota do terceiro bimestre: "))
                    adicionar_aluno(sistema_academico, nome, nota1, nota2, nota3)
                   
            except ValueError:
                print("❌ Entrada inválida. Por favor, digite números para as notas.")

        elif opcao == 0:
            print("✅ Programa encerrado!\n")
            break
       

        else:
            print("\n⚠ Escolha uma opção válida!\n")

# Executa o programa apenas se for o arquivo principal
if __name__ == "__main__":
    Login()
