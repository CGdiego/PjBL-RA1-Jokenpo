<h1 align="center">PjBL RA1 - Jokenpô</h1>

<div align="center">

Daniel Godri, Diego Soares, João Victor M. B.

[![licença](https://img.shields.io/badge/licen%C3%A7a-CC%20BY--NC%204.0-lightgrey?style=default&logo=creativecommons)](https://creativecommons.org/licenses/by-nc/4.0/)
![python](https://img.shields.io/badge/python-3.13/3.14-3776AB?style=default&logo=python&logoColor=white)

<img width="186" height="74" alt="StickmanJokenpoBattle" src="https://github.com/user-attachments/assets/5954edb3-7016-4942-855f-192c895755ee" />

</div>

Esse é um projeto de Jokenpô em Python com 5 modalidades (Humano X Humano, Humano X Computador, Computador X Computador, 2v2 e Battle Royale). Ele tem centenas de linhas de código, animação em ASCII, títulos bonitos com pyfiglet, música com winsound e muito mais!

1 Modo - Humano x Humano

Nesse modo começamos pegando o input dos jogadores e comparando com o outro para fazer o cálculo de pedra, papel, tesoura.

Esse é um exemplo do cálculo. Vou separar por linha e ir explicando.

Essa linha compara se ele não tiver definido o número/escolha, ou seja, se ele não escolheu entre Pedra=1, Papel=2, Tesoura=3 — ele vai rodar este código que pega o input do player:
while j1 != "1" and j1 != "2" and j1 != "3":

Aqui ele vai pedir input pro jogador:
    j1 = input("Jogador 1, escolha:\n'1' - Pedra\n'2' - Papel\n'3' - Tesoura\n")

Aqui ele verifica se o resultado está entre 1, 2, 3:
    if j1 != "1" and j1 != "2" and j1 != "3":
Se não, ele printa para colocar de novo:
        print("Não é uma possibilidade, insira novamente.\n")

Essa é a base para todos os inputs do nosso jogo, modificados de acordo com a necessidade.

2 Modo Computador X Humano

Aqui a diferença maior é para pegar o input do computador.

Esse é o código que é utilizado — o random — então ele randomiza, ou seja, escolhe "aleatoriamente" entre 1 e 3:
        j2 = random.randint(1, 3)

Esse código transforma em string:
        j2 = str(j2)

3 Modo Computador X Computador

Esse modo aplica a mesma lógica do 2, só que faz duas vezes.

4 Modo 2V2

Aqui, além de pegar a escolha do player (pedra, papel, tesoura), ele escolhe quem vai atacar também: player 1 ou 2.

Essa linha compara se ele não tiver definido o número/escolha, ou seja, se ele não escolheu entre Pedra=1, Papel=2, Tesoura=3 — ele vai rodar este código que pega o input do player:
while j1!="1" and j1!="2" and j1!="3":

Aqui ele pega o input do player:
    j1 = input("J1 escolha (1 Pedra 2 Papel 3 Tesoura): ")

Aqui ele define como nulo para evitar problemas:
alvoJ1 = ""

Aqui ele verifica se ele está com o ataque definido, ou seja, se ele já escolheu quem vai atacar — se não, ele roda o código:
while alvoJ1 != "1" and alvoJ1 != "2":

Aqui ele pega o input do player:
    alvoJ1 = input("J1 ataca (1)J3 ou (2)J4: ")

Aqui ele verifica se é válido:
    if alvoJ1 != "1" and alvoJ1 != "2":

Se não, ele pede de novo:  
        print("Não é uma possibilidade, insira novamente.")

Aqui ele limpa a tela para o próximo jogador não ver o que foi colocado:
print("\033[H\033[J", end="")

5 Modo Battle Royale

Aqui ele verifica se teve mais pessoas que escolheram pedra do que papel e tesoura
elif pedra > papel and pedra > tesoura:
                Aqui ele fala que a pedra ganhou e que a tesoura foi eliminada
                print(f"Pedra domina, logo, {tesoura} tesoura(s) foram eliminadas: {nomesTesoura}.")

                Aqui ele tira os jogadores que escolheram tesoura da quantidade total de jogadores
                quantJog -= tesoura

                Aqui ele tira os jogadores que escolheram tesoura da rodada
                tesoura = 0
                time.sleep(5)

                Aqui ele limpa a tela do terminal
                print("\033[H\033[J", end="") # Limpa a tela do terminal

                Aqui ele fala quem foram os sobreviventes (grupo pedra e papel)
                print(f"Os sobreviventes são: {nomesPedra} {nomesPapel}.")

                Aqui ele pede para o usuario digital qualquer coisa para seguir para a proxima rodada
                repeat = input("\nDigite qualquer coisa para ir para a próxima rodada.\n")
