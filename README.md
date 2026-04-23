<div align="center">

<img width="186" height="74" alt="StickmanJokenpoBattle" src="https://github.com/user-attachments/assets/5954edb3-7016-4942-855f-192c895755ee" />

```
 
   ✊  J O K E N P Ô   B A T T L E   S Y S T E M  
 
```

![Python](https://img.shields.io/badge/Python-3.13%20%7C%203.14-1e1e2e?style=for-the-badge&logo=python&logoColor=00d4ff)
![Plataforma](https://img.shields.io/badge/Plataforma-Windows-1e1e2e?style=for-the-badge&logo=windows&logoColor=00aaff)
![Status](https://img.shields.io/badge/Status-Concluído-1e1e2e?style=for-the-badge&logo=checkmarx&logoColor=39ff14)
[![Licença](https://img.shields.io/badge/Licença-CC%20BY--NC%204.0-1e1e2e?style=for-the-badge&logo=creativecommons&logoColor=ff79c6)](https://creativecommons.org/licenses/by-nc/4.0/)

![Modos](https://img.shields.io/badge/🎮%20Modos%20de%20Jogo-5-ff6e00?style=for-the-badge)
![ASCII](https://img.shields.io/badge/🎨%20Animações-ASCII%20Art-bd00ff?style=for-the-badge)
![Audio](https://img.shields.io/badge/🔊%20Áudio-winsound-00cfff?style=for-the-badge)

<br/>

> **PjBL RA1** — *Daniel Godri · Diego Soares · João Victor M. B.*

</div>

<br/>

<div align="center">

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   Pedra, Papel e Tesoura reimaginado em Python puro —       │
│   com 5 modos de batalha, animações no terminal,            │
│   trilha sonora e lógica de eliminação em grupo.            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

</div>

---

## ◈ Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Modos de Jogo](#-modos-de-jogo)
- [Tecnologias](#-tecnologias)
- [Como Executar](#-como-executar)
- [Estrutura do Fluxo](#-estrutura-do-fluxo)
- [Licença](#-licença)

---

## ◈ Sobre o Projeto

Este projeto implementa o clássico **Pedra, Papel e Tesoura** em Python com **cinco modos de jogo** completamente distintos. Construído do zero com centenas de linhas de código, o sistema oferece uma experiência de terminal imersiva com:

- 🎨 Títulos animados em ASCII com **pyfiglet**
- 🔊 Efeitos sonoros e trilha via **winsound**
- 🖥️ Limpeza e controle de terminal com **sequências ANSI**
- 🎲 Lógica de aleatoriedade com **random**
- ⏱️ Tempo entre transições com **time**

---

## ◈ Funcionalidades

<div align="center">

![Validação](https://img.shields.io/badge/✔%20Validação%20de%20Input-1e1e2e?style=for-the-badge&logoColor=39ff14)
![Anti-Cola](https://img.shields.io/badge/✔%20Anti--Cola%20(limpeza%20de%20tela)-1e1e2e?style=for-the-badge&logoColor=39ff14)
![IA](https://img.shields.io/badge/✔%20IA%20Aleatória-1e1e2e?style=for-the-badge&logoColor=39ff14)
![Eliminação](https://img.shields.io/badge/✔%20Sistema%20de%20Eliminação-1e1e2e?style=for-the-badge&logoColor=39ff14)
![Figlet](https://img.shields.io/badge/✔%20Títulos%20ASCII%20(pyfiglet)-1e1e2e?style=for-the-badge&logoColor=39ff14)
![Som](https://img.shields.io/badge/✔%20Efeitos%20Sonoros-1e1e2e?style=for-the-badge&logoColor=39ff14)

</div>

---

## ◈ Modos de Jogo

### ❶ Humano × Humano

Dois jogadores se revezam no mesmo terminal. O sistema **valida cada entrada** antes de prosseguir, garantindo que apenas `1` (Pedra), `2` (Papel) ou `3` (Tesoura) sejam aceitos. Entradas inválidas são rejeitadas com mensagem de erro e o jogador é solicitado a tentar novamente.

> Esta é a lógica central do jogo — todos os outros modos derivam dela.

```python
while j1 != "1" and j1 != "2" and j1 != "3":
    j1 = input("Jogador 1, escolha:\n'1' - Pedra\n'2' - Papel\n'3' - Tesoura\n")
    if j1 != "1" and j1 != "2" and j1 != "3":
        print("Não é uma possibilidade, insira novamente.\n")
```

```
  FLUXO:   [ Input ] ──► [ Validação ] ──► [ Comparação ] ──► [ Resultado ]
                              │
                         entrada inválida?
                              │
                         volta ao Input
```

---

### ❷ Humano × Computador

O jogador enfrenta uma **IA que decide aleatoriamente** usando o módulo `random`. A jogada do computador é gerada com `randint(1, 3)` e convertida para `string` para manter uniformidade com o input humano.

```python
j2 = random.randint(1, 3)  # Gera um inteiro aleatório: 1, 2 ou 3
j2 = str(j2)               # Converte para string — mesmo formato do input humano
```

> O computador não tem memória das rodadas anteriores — cada jogada é **completamente independente**, tornando o resultado estatisticamente justo.

---

### ❸ Computador × Computador

Modo autônomo onde **dois agentes de IA se enfrentam** sem intervenção humana. Aplica a lógica do Modo ❷ duas vezes, uma para cada jogador. Ideal para demonstrações e testes de fluxo do jogo.

```python
j1 = str(random.randint(1, 3))  # Jogador 1 — IA
j2 = str(random.randint(1, 3))  # Jogador 2 — IA
```

---

### ❹ 2v2 — Batalha em Times

O modo mais estratégico: cada jogador escolhe sua **jogada** *e* o **alvo** que deseja atacar no time adversário. A tela é **apagada entre os turnos** para que nenhum jogador veja a escolha dos outros.

```python
# ── Fase 1: Escolha da jogada ──────────────────────────────────────
while j1 != "1" and j1 != "2" and j1 != "3":
    j1 = input("J1 escolha (1 Pedra  2 Papel  3 Tesoura): ")
    if j1 != "1" and j1 != "2" and j1 != "3":
        print("Não é uma possibilidade, insira novamente.")

# ── Fase 2: Escolha do alvo ────────────────────────────────────────
alvoJ1 = ""
while alvoJ1 != "1" and alvoJ1 != "2":
    alvoJ1 = input("J1 ataca (1) J3 ou (2) J4: ")
    if alvoJ1 != "1" and alvoJ1 != "2":
        print("Não é uma possibilidade, insira novamente.")

# ── Fase 3: Limpa a tela antes do próximo jogador ─────────────────
print("\033[H\033[J", end="")  # Sequência ANSI — apaga o terminal
```

```
  TIME A         vs         TIME B
  ┌─────────┐             ┌─────────┐
  │ J1 ──────── ataca ──►│ J3 / J4 │
  │ J2 ──────── ataca ──►│ J3 / J4 │
  └─────────┘             └─────────┘
```

---

### ❺ Battle Royale ⚔️

O modo épico: **N jogadores** entram, apenas um sai. A cada rodada, os jogadores escolhem Pedra, Papel ou Tesoura. O **grupo majoritário** elimina o grupo perdedor. O jogo continua até sobrar um único campeão — ou um empate entre grupos iguais.

```python
elif pedra > papel and pedra > tesoura:
    # Pedra é maioria — Tesoura é eliminada
    print(f"Pedra domina, logo, {tesoura} tesoura(s) foram eliminadas: {nomesTesoura}.")

    quantJog -= tesoura   # Remove eliminados da contagem total
    tesoura = 0           # Zera o grupo Tesoura desta rodada

    time.sleep(5)                      # Pausa dramática antes de limpar
    print("\033[H\033[J", end="")      # Limpa o terminal

    print(f"Os sobreviventes são: {nomesPedra} {nomesPapel}.")
    repeat = input("\nDigite qualquer coisa para ir para a próxima rodada.\n")
```

```
  RODADA 1        RODADA 2        FINAL
  ──────────      ──────────      ──────────
  6 jogadores ──► 4 sobreviventes ──► 🏆 Campeão
  2 eliminados    2 eliminados
  (tesoura)       (papel)
```

> As três combinações de eliminação são tratadas:
> `Pedra → Tesoura` · `Papel → Pedra` · `Tesoura → Papel`

---

## ◈ Tecnologias

<div align="center">

| Biblioteca | Função | Badge |
|:---:|:---|:---:|
| `random` | Geração de jogadas do computador | ![random](https://img.shields.io/badge/random-built--in-1e1e2e?style=flat-square&logoColor=white) |
| `pyfiglet` | Títulos estilizados em ASCII art | ![pyfiglet](https://img.shields.io/badge/pyfiglet-pip-bd00ff?style=flat-square) |
| `winsound` | Efeitos sonoros e música (Windows) | ![winsound](https://img.shields.io/badge/winsound-built--in-0078d4?style=flat-square&logo=windows) |
| `time` | Delays dramáticos entre transições | ![time](https://img.shields.io/badge/time-built--in-1e1e2e?style=flat-square) |
| ANSI Escape | Limpeza e controle do terminal | ![ansi](https://img.shields.io/badge/ANSI-escape%20codes-39ff14?style=flat-square) |

</div>

---

## ◈ Como Executar

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git

# 2. Entre na pasta do projeto
cd seu-repositorio

# 3. Instale a única dependência externa
pip install pyfiglet

# 4. Inicie o jogo
python main.py
```

<div align="center">

![Req](https://img.shields.io/badge/Requer-Python%203.13%2B-1e1e2e?style=for-the-badge&logo=python&logoColor=00d4ff)
![SO](https://img.shields.io/badge/Som%20apenas%20em-Windows-1e1e2e?style=for-the-badge&logo=windows&logoColor=ff6b6b)

</div>

> ⚠️ **Nota:** os efeitos sonoros via `winsound` são exclusivos do Windows. O jogo roda normalmente em outros sistemas, mas sem áudio.

---

## ◈ Estrutura do Fluxo

```
main.py
  │
  ├── Menu Principal
  │     ├── [1] Humano × Humano
  │     ├── [2] Humano × Computador
  │     ├── [3] Computador × Computador
  │     ├── [4] 2v2
  │     └── [5] Battle Royale
  │
  ├── Módulo de Input ──► validação em loop até entrada válida
  ├── Módulo de IA ─────► random.randint(1, 3)
  ├── Módulo de Confronto ► comparação e cálculo do vencedor
  ├── Módulo de Display ──► pyfiglet + ANSI + ASCII art
  └── Módulo de Áudio ───► winsound (Windows only)
```

---

## ◈ Licença

<div align="center">

[![CC BY-NC 4.0](https://img.shields.io/badge/Creative%20Commons-BY--NC%204.0-1e1e2e?style=for-the-badge&logo=creativecommons&logoColor=ff79c6)](https://creativecommons.org/licenses/by-nc/4.0/)

Uso livre para fins **não comerciais** com atribuição aos autores.

<br/>

*Made with 🖤 by Daniel Godri · Diego Soares · João Victor M. B.*

</div>
