# Membros do Grupo:
# - Nome: Diogo Oliveira Lima - 562559
# - Nome: Lucas dos Reis Aquino - 562414
# - Nome: Lucas Perez Bonato - 565356

def main():
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

def calculate_raindrop_force(mass: float, acceleration: float) -> float:
    """
    Calcula a força aplicada por uma gota de chuva.
    mass: massa da gota em miligrama (mg)
    acceleration: aceleração da gota em m/s^2

    Retorna:
        A força aplicada pela gota de chuva em Newtons (N).
    """
    force = mass * acceleration
    print(f"A força da gota da chuva é {force}N.")
    return force

def calculate_raindrop_type(force: float) -> str:
    """
    Determina o tipo de gota de chuva com base na força aplicada.
    force: força em Newtons (N)

    Retorna:
        Uma string indicando o tipo de gota de chuva.
        "Light ", "Moderate" ou "Heavy".
    """
    if force < 0.00130:
        return "Light"
    elif force < 0.00180:
        return "Moderate"
    else:
        return "Heavy"
    
def classify_rain(raindrops: list) -> str:
    """
    Classifica uma lista de gotas de chuva em leves, moderadas ou pesadas.

    raindrops: lista de lista, cada uma contendo (massa, aceleracao)

    Retorna:
        Uma string indicando a classificação da chuva:
        "Light", "Moderate" ou "Heavy".
    """

    forces = []
    for mass, acceleration in raindrops: # pega cada massa e aceleração, calcula uma média e retorna a classificação
        forces.append(calculate_raindrop_force(mass, acceleration))
    avg_force = sum(forces) / len(forces)
    print(f"A força média das gotas de chuva é {avg_force}N.")
    rain_class = calculate_raindrop_type(avg_force)
    return rain_class
    
def ask_yesno_question(question: str) -> bool:
    """
    Faz uma pergunta ao usuário e espera uma resposta sim ou não.

    question: A pergunta a ser feita.

    Retorna:
        True se a resposta for sim, False se for não.
    """
    while True:
        response = input(question + " (s/n): ").strip().lower()
        if response == 's':
            return True
        elif response == 'n':
            return False
        else:
            print("Resposta inválida. Por favor, responda com 's' ou 'n'.")

def prompt_raindrop(is_single_drop: bool) -> list:
    """
    Solicita ao usuário que insira a massa e a aceleração de uma ou mais gotas de chuva.

    is_single_drop: Se True, solicita apenas uma gota; se False, permite inserir várias gotas.

    Retorna:
        Uma lista de tuplas, cada uma contendo a massa (float) e a aceleração (float) de uma gota.
    """

    raindrops = []
    # Faz um loop infinito e para somente quando o usuário decidir parar de inserir gotas
    while True:
        try:
            mass = float(input("Digite a massa da gota (mg): "))
            if mass <= 0:
                print("A massa deve ser um número positivo.")
                continue
            acceleration = float(input("Digite a aceleração da gota (m/s^2): "))
            if acceleration <= 0:
                print("A aceleração deve ser um número positivo. Não é possível ter uma gota com aceleração negativa ou zero.")
                continue
            raindrops.append((mass, acceleration))


            if is_single_drop == False:
                ask_another_drop = ask_yesno_question("Deseja adicionar outra gota?")
                if(ask_another_drop == True):
                    continue

            rain_class = classify_rain(raindrops)
            if is_single_drop == False:
                print(f"Classificação da chuva: {rain_class}")
            else:
                print(f"Classificação da gota: {rain_class}")

            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um valor válido.")

    return raindrops

main()