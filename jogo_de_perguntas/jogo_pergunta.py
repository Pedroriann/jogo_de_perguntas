def jogo_perguntas():
    print("Bem-vindo ao jogo de perguntas e respostas!")
    print("Responda corretamente para ganhar pontos.")
    print("-----------------------------------------\n")
    
    pergunta = "Qual é a capital da França?" 
    resposta_correta = "Paris" 
    
    print(pergunta)
    resposta_jogador = input("Sua resposta: ").strip()  
    
    if resposta_jogador.lower() == resposta_correta.lower(): 
        print("Resposta correta! Parabéns!\n")
    else:
        print(f"Resposta errada! A resposta correta era: {resposta_correta}\n")
    
    print("-----------------------------------------")
    print("Fim do jogo! Obrigado por jogar!")

jogo_perguntas()

