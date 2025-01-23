def jogo_perguntas():
    print("Bem-vindo ao jogo de perguntas e respostas!")
    
    perguntas = [
        "Qual é a capital da França?",
        "Quanto é 7 x 8?", 
        "Quem descobriu o Brasil?"
    ]
    respostas = [
        "Paris", 
        "56", 
        "Pedro Alvares Cabral"
    ]
    
    for i in range(3):
        print(perguntas[i])
        resposta_jogador = input("Sua resposta: ").strip()
        
        if resposta_jogador.lower() == respostas[i].lower():
            print("Resposta correta! Parabéns!\n")
        else:
            print(f"Resposta errada! A resposta correta era: {respostas[i]}\n")
        
jogo_perguntas()
