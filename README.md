# AWS Lambda - Função Olá Mundo

Este projeto contém um exemplo simples de função AWS Lambda escrita em Python. A função recebe um nome via `event` e retorna uma mensagem personalizada.

---

## 📦 Requisitos

- Conta AWS com acesso ao [AWS Lambda](https://console.aws.amazon.com/lambda/home)
- Python 3.12 ou superior (para testes locais, se desejar)
- Git instalado
- Editor de código (VSCode, por exemplo)

---

## 🚀 Como funciona

A função espera receber um JSON no seguinte formato:

```json
{
  "nome": "Gustavo"
}


E retorna:


{
  "statusCode": 200,
  "body": "Olá, Gustavo! Sua função Lambda está funcionando com sucesso."
}

