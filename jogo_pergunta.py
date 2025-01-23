def jogo_perguntas():
    print("Bem-vindo ao jogo de perguntas e respostas!")
    print("Responda corretamente para ganhar pontos.")
    print("-----------------------------------------\n")
    
    perguntas = [
        "Qual é a capital da França?",
        "Quanto é 5 + 3?",
        "Quem escreveu 'Dom Quixote'?",
        "Qual é o planeta mais próximo do Sol?"
    ]
    respostas = [
        "Paris",
        "8",
        "Miguel de Cervantes",
        "Mercúrio"
    ]
    
    pontos = 0
    
    for i in range(len(perguntas)):
        print(f"Pergunta {i + 1}: {perguntas[i]}")
        resposta_jogador = input("Sua resposta: ").strip()
        if resposta_jogador.lower() == respostas[i].lower():
            print("Resposta correta!\n")
            pontos += 1
        else:
            print(f"Resposta errada! A resposta correta era: {respostas[i]}\n")
    
    print("-----------------------------------------")
    print(f"Fim do jogo! Você acertou {pontos} de {len(perguntas)} perguntas.")
    if pontos == len(perguntas):
        print("Parabéns! Você acertou todas as perguntas!")
    elif pontos > len(perguntas) / 2:
        print("Bom trabalho! Você foi bem.")
    else:
        print("Continue praticando e tente novamente!")


jogo_perguntas()
