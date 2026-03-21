## 🎮 Jogo 2D em Pygame

Projeto desenvolvido em Python utilizando Pygame como trabalho acadêmico, com foco em arquitetura de jogos, controle de estados e organização de código.

---

## 🕹️ Sobre o Jogo

O jogo consiste em um sistema de combate onde o jogador escolhe um personagem e enfrenta inimigos que surgem ao longo do tempo.
 
---

## O projeto implementa um fluxo completo de jogo:

# Menu inicial
- Seleção de personagem
  
- Fase principal
  
- Tela de Game Over
  
- Tela de Vitória

---

## 🎭 Personagens

# 🔥 Diablo

- Personagem terrestre
  
- Movimentação limitada ao eixo horizontal
  
# ✨ Genius

- Personagem voador
  
- Movimentação livre na tela (horizontal e vertical)
  
# 👾 Inimigos

- Spawn de inimigos baseado em tempo (pygame.USEREVENT)
  
- Controle de dificuldade por frequência de spawn
  
- Sistema de colisão
  
- Movimentação fluida dos personagens
  
- Controle de limites da tela (incluindo personagem voador)

---
  
## 🧠 Arquitetura

O projeto foi estruturado com separação de responsabilidades:

- Game → gerenciamento de estados
  
- Level → lógica da fase
  
- EntityFactory → criação de entidades
  
- Entities → jogadores e inimigos

Essa organização facilita manutenção, escalabilidade e entendimento do código.

---

## 🛠️ Tecnologias Utilizadas

- Python
  
- Pygame
  
- Programação Orientada a Objetos

---

## ▶️ Como Executar
# 🔹 Opção 1 — Executável (Recomendado)

Basta executar o arquivo:
```bash
dist/main.exe
```
(Não é necessário instalar Python ou dependências)

#🔹 Opção 2 — Código-fonte
1 - nstale as dependências:
```bash
pip install pygame
```
2 - Execute o projeto:
```bash
python main.py
```
---
## 📂 Estrutura do Projeto
⚠️ Estrutura simplificada — pode conter mais arquivos internos
```bash
project/
│
├── main.py
├── code/
├── entities/
├── assets/
├── dist/          # executável
├── build/         # arquivos do pyinstaller
```
---
## ✅ Status do Projeto

✔️ Finalizado
✔️ Jogável
✔️ Executável disponível
---
## 🎓 Contexto Acadêmico

# Projeto desenvolvido como trabalho de faculdade com foco em:

- Lógica de jogos
  
- Estruturação de projetos
  
- Organização de código
  
- Uso de bibliotecas gráficas
---
## 👨‍💻 Autor

Desenvolvido por Brian Sato
---


