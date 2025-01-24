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
    max_tentativas = 3
    pergunta_atual = 0
    
    while pergunta_atual < len(perguntas):
        tentativas = 0
        print(f"Pergunta {pergunta_atual + 1}: {perguntas[pergunta_atual]}")
        
        while tentativas < max_tentativas:
            resposta_jogador = input(f"Tentativa {tentativas + 1}/{max_tentativas} - Sua resposta: ").strip()
            if resposta_jogador.lower() == respostas[pergunta_atual].lower():
                print("Resposta correta!\n")
                pontos += 1
                break
            else:
                tentativas += 1
                if tentativas < max_tentativas:
                    print("Resposta errada! Tente novamente.\n")
                else:
                    print(f"Resposta errada! A resposta correta era: {respostas[pergunta_atual]}\n")
        
        if tentativas == max_tentativas:
            resposta_errada = input("Você quer tentar de novo a pergunta anterior? (s/n): ").strip().lower()
            if resposta_errada == 's' and pergunta_atual > 0:
                pergunta_atual -= 1  
                print("Você voltou para a pergunta anterior.")
            else:
                pergunta_atual += 1 
        else:
            pergunta_atual += 1
    
    print("-----------------------------------------")
    print(f"Fim do jogo! Você acertou {pontos} de {len(perguntas)} perguntas.")
    if pontos == len(perguntas):
        print("Parabéns! Você acertou todas as perguntas!")
    elif pontos > len(perguntas) / 2:
        print("Bom trabalho! Você foi bem.")
    else:
        print("Continue praticando e tente novamente!")

jogo_perguntas()

#Não consegui fazer voltar na primeira pergunta, se você tentar ele só passa pra próxima, mas depois ele volta normal 
