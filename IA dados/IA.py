from transformers import pipeline

# Substitua 'your_token' pelo seu token de acesso
token = "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"

# Inicializa o pipeline de geração de texto com autenticação
generator = pipeline('text-generation', model='gpt-2', use_auth_token=token)

# Função para gerar dados com base no comando do usuário
def generate_data(command):
    generated_text = generator(command, max_length=100, num_return_sequences=1)
    return generated_text[0]['generated_text']

# Exemplo de uso
command = "Crie uma lista de tarefas para um projeto de desenvolvimento de software"
generated_data = generate_data(command)
print(generated_data)
