def lambda_handler(event, context):
    nome = event.get("nome", "visitante")
    return {
        "statusCode": 200,
        "body": f"Olá, {nome}! Sua função Lambda está funcionando com sucesso."
    }
