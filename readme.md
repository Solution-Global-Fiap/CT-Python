# Classificador de Tipo de Chuva

Este projeto tem como objetivo auxiliar na classificação do tipo de chuva com base na força exercida por gotas d'água. Ele pode ser utilizado como ferramenta complementar a sensores de chuva (por exemplo, via Arduino) para apoiar a detecção de chuvas leves, moderadas ou fortes.

## 👨‍💻 Membros do Grupo

- **Diogo Oliveira Lima** - RM: 562559  
- **Lucas dos Reis Aquino** - RM: 562414  
- **Lucas Perez Bonato** - RM: 565356

## 📄 Descrição

O sistema permite ao usuário informar os dados de gotas de chuva (massa e aceleração), calcula a força aplicada por elas e classifica como:

- **Light** (Leve)
- **Moderate** (Moderada)
- **Heavy** (Forte)

A classificação é feita com base na força média das gotas inseridas.

## 🧠 Funcionalidades

- Inserção de uma única gota para classificação individual.
- Inserção de múltiplas gotas para classificação da chuva.
- Classificação automática com base na força média.
- Testes automatizados para garantir o correto funcionamento.

## 🚀 Como Executar

1. **Execute o programa principal**:
   ```bash
   python main.py
