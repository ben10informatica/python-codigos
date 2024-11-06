from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Criar um novo chatbot
chatbot = ChatBot('MeuChatBot')

# Treinar o chatbot com o conjunto de dados padrão
trainer = ChatterBotCorpusTrainer(chatbot)

# Treinando o chatbot com o corpus em português
trainer.train("chatterbot.corpus.portuguese")

print("Chatbot está pronto para conversar! Digite 'sair' para encerrar.")

# Loop de conversa
while True:
    try:
        entrada_usuario = input("Você: ")
        if entrada_usuario.lower() == 'sair':
            print("Chatbot: Até logo!")
            break

        resposta = chatbot.get_response(entrada_usuario)
        print(f"Chatbot: {resposta}")

    except (KeyboardInterrupt, EOFError, SystemExit):
        break