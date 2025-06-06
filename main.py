# Membros do Grupo:
# - Nome: Diogo Oliveira Lima - 562559
# - Nome: Lucas dos Reis Aquino - 562414
# - Nome: Lucas Perez Bonato - 565356

from functions import prompt_raindrop

def main():
    print(r"""
      ___   _              _          ______         _                    
     / _ \ | |            | |         | ___ \       (_)                   
    / /_\ \| |  ___  _ __ | |_   __ _ | |_/ /  __ _  _  _ __  _ __   ___  
    |  _  || | / _ \| '__|| __| / _` || ___ \ / _` || || '__|| '__| / _ \ 
    | | | || ||  __/| |   | |_ | (_| || |_/ /| (_| || || |   | |   | (_) |
    \_| |_/|_| \___||_|    \__| \__,_|\____/  \__,_||_||_|   |_|    \___/ 
    """)
    print("\nBem-vindo ao sistema calculador do tipo de chuvas!\n")
    print("----------------------------------------------------------------------\n")
    print("Este programa foi feito para auxiliar no cálculo feito pelo arduíno, auxiliando no reconhecimento do tipo de chuva.")
    print("Assim, o sistema conseguirá definir com mais facilidade se a chuva é forte, podendo ajudar na prevenção de alagamentos e outros problemas relacionados.")
    print("Portanto, vamos começar!!")
    print("\n----------------------------------------------------------------------")
    while True:
        print("\nEscolha uma opção:")
        print("1) Classificar uma gota de chuva")
        print("2) Classificar chuva por várias gotas")
        print("3) Sair")
        option = input("Digite o número da opção desejada: ").strip()
        if option == "1":
            prompt_raindrop(is_single_drop=True)
        elif option == "2":
            prompt_raindrop(is_single_drop=False)
        elif option == "3":
            print("Saindo do programa. Obrigado por usar o sistema!")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()