# 🖥️ AWS Lambda - Função Olá Mundo

Este repositório contém uma função simples criada diretamente no console da AWS Lambda, escrita em Python. A função recebe um nome via JSON e retorna uma mensagem personalizada.

---

## 📌 Descrição

A função `lambda_handler` é acionada com um objeto `event` contendo um campo `"nome"`. 
Ela responde com uma saudação personalizada. Se nenhum nome for fornecido, responde com "visitante".

---

## 📦 Requisitos

- Conta AWS com acesso ao serviço [AWS Lambda](https://console.aws.amazon.com/lambda/)
- Conhecimentos básicos de AWS Console
- Navegador com acesso à internet

---

## Como executar
Faça o deploy da função Lambda no AWS.
Teste no console Lambda passando o evento JSON.
Verifique o retorno da função.

## 🧭 Passo a Passo para Testar
No console AWS Lambda, clique em "Teste"
Insira um evento de teste.

## Observações
A função é simples e não acessa nenhum recurso externo, logo não há necessidade de permissões especiais.


## 🚀 Código da Função

```python
def lambda_handler(event, context):
    nome = event.get("nome", "visitante")
    return {
        "statusCode": 200,
        "body": f"Olá, {nome}! Sua função Lambda está funcionando com sucesso."
    }.


