<h1 align="center">✊ Jokenpô Battle ✋</h1>

<div align="center">

<img width="186" height="74" alt="StickmanJokenpoBattle" src="https://github.com/user-attachments/assets/5954edb3-7016-4942-855f-192c895755ee" />

<br/><br/>

![Python](https://img.shields.io/badge/Python-3.13%20|%203.14-1e1e2e?style=plastic&logo=python&logoColor=00d4ff)
![Status](https://img.shields.io/badge/Status-Concluído-1e1e2e?style=plastic&logoColor=39ff14)
[![Licença](https://img.shields.io/badge/Licença-CC%20BY--NC%204.0-1e1e2e?style=plastic&logo=creativecommons&logoColor=ff79c6)](https://creativecommons.org/licenses/by-nc/4.0/)

**PjBL RA1 — Daniel Godri · Diego Soares · João Victor M. B.**

</div>

---

Jogo de Pedra, Papel e Tesoura em Python com 5 modos de jogo. Tem animações em ASCII, títulos com pyfiglet, efeitos sonoros com winsound e centenas de linhas de código.

<div align="center">

![Validação](https://img.shields.io/badge/✔%20Validação%20de%20Input-1e1e2e?style=plastic)
![Anti-Cola](https://img.shields.io/badge/✔%20Anti--Cola-1e1e2e?style=plastic)
![IA](https://img.shields.io/badge/✔%20IA%20Aleatória-1e1e2e?style=plastic)
![Eliminação](https://img.shields.io/badge/✔%20Sistema%20de%20Eliminação-1e1e2e?style=plastic)
![Figlet](https://img.shields.io/badge/✔%20Títulos%20ASCII-1e1e2e?style=plastic)
![Som](https://img.shields.io/badge/✔%20Músicas-1e1e2e?style=plastic)

</div>

---

## Modos de Jogo

### 1. Humano × Humano

Dois jogadores se revezam no mesmo terminal. O jogo valida cada entrada e rejeita qualquer coisa fora de `1`, `2` ou `3`.

```python
while j1 != "1" and j1 != "2" and j1 != "3":
    j1 = input("Jogador 1, escolha:\n'1' - Pedra\n'2' - Papel\n'3' - Tesoura\n")
    if j1 != "1" and j1 != "2" and j1 != "3":
        print("Não é uma possibilidade, insira novamente.\n")
```

Essa lógica de validação é a base de todos os outros modos, adaptada conforme a necessidade de cada um.

---

### 2. Humano × Computador

A diferença aqui é que a jogada do computador é gerada aleatoriamente com `random.randint`, depois convertida para string para ficar no mesmo formato do input do jogador.

```python
j2 = random.randint(1, 3)  # escolha aleatória
j2 = str(j2)               # converte para string
```

---

### 3. Computador × Computador

Aplica a mesma lógica do Modo 2 para os dois jogadores. Partida totalmente automática, útil para testes e demonstrações.

```python
j1 = str(random.randint(1, 3))
j2 = str(random.randint(1, 3))
```

---

### 4. 2v2

Além da jogada (Pedra/Papel/Tesoura), cada jogador também escolhe **qual adversário atacar**. A tela é limpa entre os turnos para ninguém ver o que o outro digitou.

```python
# Escolha da jogada
while j1 != "1" and j1 != "2" and j1 != "3":
    j1 = input("J1 escolha (1 Pedra  2 Papel  3 Tesoura): ")

# Escolha do alvo
alvoJ1 = ""
while alvoJ1 != "1" and alvoJ1 != "2":
    alvoJ1 = input("J1 ataca (1) J3 ou (2) J4: ")
    if alvoJ1 != "1" and alvoJ1 != "2":
        print("Não é uma possibilidade, insira novamente.")

# Limpa a tela antes do próximo jogador
print("\033[H\033[J", end="")
```

---

### 5. Battle Royale ⚔️

Vários jogadores entram e o grupo majoritário elimina o perdedor a cada rodada, até sobrar um campeão.

```python
elif pedra > papel and pedra > tesoura:
    print(f"Pedra domina, logo, {tesoura} tesoura(s) foram eliminadas: {nomesTesoura}.")

    quantJog -= tesoura
    tesoura = 0

    time.sleep(5)
    print("\033[H\033[J", end="")

    print(f"Os sobreviventes são: {nomesPedra} {nomesPapel}.")
    repeat = input("\nDigite qualquer coisa para ir para a próxima rodada.\n")
```

As três combinações de eliminação são tratadas: `Pedra → Tesoura`, `Papel → Pedra` e `Tesoura → Papel`.

---

## Tecnologias

| Biblioteca | Uso |
|---|---|
| `random` | Jogadas do computador |
| `pyfiglet` | Títulos em ASCII art |
| `winsound` | Efeitos sonoros (Windows) |
| `time` | Delays entre animações |
| ANSI Escape Codes | Limpeza de tela no terminal |

---

## Como Executar

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

# Instale a dependência
pip install pyfiglet

# Rode o jogo
python main.py
```

> ⚠️ Os efeitos sonoros com `winsound` funcionam **apenas no Windows**.

---

## Licença

Distribuído sob a licença [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) — uso não comercial com atribuição.
