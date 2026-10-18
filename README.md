# 💧 Monitor de Níveis de Água

Um projeto desenvolvido em **Python** que simula o monitoramento de diferentes níveis de água, exibindo alertas textuais com cores para facilitar a identificação de cada situação.

O projeto foi criado com o objetivo de praticar conceitos fundamentais da programaçã, explorar novas ferramentas, incluindo minha primeira experiência utilizando o gerenciador de biblioteca do Python, o pip, para instalar e utlizar duas bibliotecas, uma externa (colorama) e outra interna(random).

---

## 🖥️ Demonstração

O programa seleciona aleatoriamente um dos cinco níveis de água disponíveis e exibe uma mensagem correspondente, utilizando cores diferentes para representar cada situação.

| Nível | Mensagem | Cor |
|:---:|---|---|
| `nivel1` | Muito baixo (crítico) | 🔴 Vermelho |
| `nivel2` | Baixo | 🟡 Amarelo |
| `nivel3` | Médio | 🟢 Verde |
| `nivel4` | Alto | 🩵 Ciano |
| `nivel5` | Muito alto (alerta) | 🔵 Azul |

---

## ⚙️ Tecnologias e ferramentas

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Colorama-Color_Output-4B8BBE?style=for-the-badge" alt="Colorama"/>
  <img src="https://img.shields.io/badge/Random-Biblioteca_Nativa-6A5ACD?style=for-the-badge" alt="Random"/>
  <img src="https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white" alt="Visual Studio Code"/>
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
</p>

### 📚 Bibliotecas utilizadas

**🎨 Colorama**

A Colorama foi a primeira biblioteca externa que aprendi a instalar e utilizar em um projeto Python. Ela permite adicionar cores e estilos ao texto exibido no terminal, tornando as mensagens mais visuais e facilitando a identificação dos diferentes níveis de água.

Neste projeto, utilizei `Fore` para definir as cores das mensagens e `Style.RESET_ALL` para restaurar o estilo padrão do terminal.

**🎲 Random**

O módulo `random` faz parte da biblioteca padrão do Python, portanto não precisa ser instalado separadamente. Utilizei a função `choice()` para selecionar aleatoriamente um dos níveis de água disponíveis na lista e depois armazenei em uma variável.

---

## 🧠 Conceitos praticados

- **Listas:** organização dos cinco níveis de água possíveis.
- **Funções:** utilização de uma função para separar e organizar a exibição das mensagens.
- **Condicionais (`if`, `elif`):** identificação do nível sorteado e escolha da mensagem correspondente.
- **Importação de módulos:** utilização de recursos disponíveis no Python.
- **Biblioteca externa:** instalação e aplicação prática da Colorama.
- **Geração aleatória:** seleção de um nível utilizando `random.choice()`.
- **Formatação de terminal:** aplicação de cores para melhorar a visualização das informações.

---

## 🚀 Como executar o projeto

### 1. Pré-requisitos

- Python instalado na máquina.
- Um editor de código, como o Visual Studio Code.

### 2. Instale a Colorama

Abra o terminal na pasta do projeto e execute:

```bash
pip install colorama
```

### 3. Execute o programa

Salve o código em um arquivo chamado `main.py` ou do seu critério e execute:

```bash
python main.py
```

O programa exibirá uma das cinco mensagens possíveis, de acordo com o nível de água selecionado aleatoriamente.

---

## 🎯 Objetivo do projeto

Este projeto faz parte da minha jornada de aprendizado em programação, com foco na construção de uma base sólida em Python e no desenvolvimento de pequenos projetos práticos.

Mais do que criar um programa funcional, o objetivo foi aprender a trabalhar com bibliotecas, organizar o código em funções e explorar recursos que tornam a saída de um programa mais clara e intuitiva.

**Cada projeto é uma oportunidade de transformar conhecimento em prática e evoluir como desenvolvedor.** 🚀

---

⭐ Se você gostou do projeto, considere deixar uma estrela no repositório!