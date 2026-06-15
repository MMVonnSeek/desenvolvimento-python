## 🏗 Em construção...
# 🐍 desenvolvimento-python
[![Curso](https://img.shields.io/badge/Curso-Desenvolvedor_Python-356CC4?style=for-the-badge)](https://github.com/MMVonnSeek/desenvolvimento-python)
[![Instituição](https://img.shields.io/badge/Instituição-SENAI_DF-FFCB39?style=for-the-badge)](https://github.com/MMVonnSeek/desenvolvimento-python)
[![Professor](https://img.shields.io/badge/Professor-Max_Muller-black?style=for-the-badge)](https://github.com/MMVonnSeek)
[![Carga Horária](https://img.shields.io/badge/Carga_Horária-220h-FFCB39?style=for-the-badge)](https://github.com/MMVonnSeek/desenvolvimento-python)
[![Python](https://img.shields.io/badge/Python-3.10+-356CC4?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

> Material didático completo do curso  de qualificação **Desenvolvedor Python** · SENAI - DF · 220 horas · 2026

---

## Sobre o repositório

Este repositório reúne todo o material produzido para o curso de **Desenvolvedor Python** do SENAI - DF. O conteúdo está organizado por módulo e capitulo, e inclui apostilas, roteiros de aula, exemplos de código comentados e projetos práticos.

O curso forma profissionais capazes de desenvolver soluções com Python desde a lógica de programação até integração com dados e APIs — totalizando **220 horas** distribuídas em **4 módulos** e **8 capitulos**.

---

<div align="center">
  <img src="screenshot/MMVonnSeek.png" alt="logo-python" width="800">
</div>

---

## Estrutura do repositório

```
desenvolvimento-python/
│
├── modulo1-fundamentos/
│   ├── uc1-intro/              # Introdução à Programação em Python (20h)
│   └── uc2-estruturas/         # Estruturas de Dados e Funções (24h)
│
├── modulo2-backend/
│   ├── uc3-poo/                # Programação Orientada a Objetos (40h)
│   └── uc4-arquivos/           # Manipulação de Arquivos e Exceções (20h)
│
├── modulo3-dados/
│   ├── uc5-externos/           # Bibliotecas Externas (28h)
│   └── uc6-analise/            # Introdução a Dados e Análise (36h)
│
└── modulo4-projeto/
    ├── uc7-planejamento/       # Planejamento de Projeto (20h)
    └── uc8-projeto/            # Projeto Final (12h)
```

Cada pasta de UC segue sempre a mesma organização interna:

```
ucX-nome/
├── apostila.docx       # apostila completa para o aluno
├── README.md           # descrição da UC e índice de aulas
├── roteiros/           # roteiros do professor (uso interno)
│   └── aulaXX.docx
├── exemplos/           # código demonstrado em aula (VS Code + datashow)
│   └── aulaXX_tema.py
├── atividades/         # enunciados das atividades em sala
└── projetos/           # projetos práticos e projeto final da UC
```

---

## Módulos e Unidades Curriculares

| Módulo | UC | Título | Carga | Aulas | Status |
|--------|----|--------|:-----:|:-----:|--------|
| 1 – Fundamentos | UC1 | Introdução à Programação em Python | 20h | 5 | ✅ Completo |
| 1 – Fundamentos | UC2 | Estruturas de Dados e Funções | 24h | 6 | 🔜 Em breve |
| 2 – Backend e POO | UC3 | Programação Orientada a Objetos | 40h | 10 | 🔜 Em breve |
| 2 – Backend e POO | UC4 | Manipulação de Arquivos e Exceções | 20h | 5 | 🔜 Em breve |
| 3 – Dados e Integração | UC5 | Bibliotecas Externas | 28h | 7 | 🔜 Em breve |
| 3 – Dados e Integração | UC6 | Introdução a Dados e Análise | 36h | 9 | 🔜 Em breve |
| 4 – Projeto | UC7 | Planejamento de Projeto | 20h | 5 | 🔜 Em breve |
| 4 – Projeto | UC8 | Projeto Final | 12h | 3 | 🔜 Em breve |
| | | **Total** | **220h** | **50** | |

---

## Conteúdo atual

### Módulo 1 – Fundamentos

<details>
<summary><strong>UC1 · Introdução à Programação em Python</strong> — 20h · 5 aulas</summary>

| Aula | Tema | Arquivo |
|------|------|---------|
| 01 | Algoritmos, ambiente de desenvolvimento, `print()` | `exemplos/aula01_print_comentarios.py` |
| 02 | Variáveis, tipos de dados, `input()`, constantes | `exemplos/aula02_variaveis_tipos.py` |
| 03 | Operadores aritméticos, relacionais, lógicos e condicionais | `exemplos/aula03_operadores_condicionais.py` |
| 04 | Estruturas de repetição e listas | `exemplos/aula04_repeticao_listas.py` |
| 05 | Funções e boas práticas (PEP 8) | `exemplos/aula05_funcoes.py` |

**Projeto final:** Sistema de Gerenciamento de Turma com menu, funções e listas.

</details>

<details>
<summary><strong>UC2 · Estruturas de Dados e Funções</strong> — 24h · 6 aulas</summary>

| Aula | Tema | Arquivo |
|------|------|---------|
| 01 | Listas — estrutura, métodos e fatiamento | `exemplos/aula01_listas.py` |
| 02 | Tuplas e Conjuntos | `exemplos/aula02_tuplas_conjuntos.py` |
| 03 | Dicionários | `exemplos/aula03_dicionarios.py` |
| 04 | Funções avançadas — `*args`, `**kwargs`, lambda, recursão | `exemplos/aula04_funcoes_avancadas.py` |
| 05 | Comprehensions e funções built-in | `exemplos/aula05_comprehensions.py` |
| 06 | Projeto integrador | `projetos/projeto_final/biblioteca.py` |

**Projeto final:** Biblioteca Digital com cadastro, empréstimo, devolução e estatísticas.

</details>

---

## Como usar os exemplos de aula

Os arquivos `.py` da pasta `exemplos/` são **roteiro e código ao mesmo tempo**. Cada arquivo combina:

- comentários com erros intencionais para demonstrar em aula
- comentários com dicas pedagógicas
- código real executável no VS Code

O arquivo é aberto no VS Code e projetado no datashow. O professor executa bloco a bloco conforme o andamento da turma, usando as pausas `input('[ Enter para continuar... ]')` entre os blocos.

---

## Ambiente recomendado

| Ferramenta | Versão mínima | Link |
|------------|:-------------:|------|
| Python | 3.10+ | [python.org](https://www.python.org/downloads/) |
| VS Code | qualquer | [code.visualstudio.com](https://code.visualstudio.com/) |
| Extensão Python (VS Code) | — | Microsoft |
| Git | qualquer | [git-scm.com](https://git-scm.com/) |

---

## Como clonar e usar

```bash
# Clonar o repositório
git clone https://github.com/MMVonnSeek/desenvolvimento-python.git
cd desenvolvimento-python

# Navegar até a aula desejada
cd modulo1-fundamentos/uc1-intro/exemplos

# Executar um exemplo
python aula01_print_comentarios.py
```

---

## Convenções do repositório

| Prefixo / Padrão | Significado |
|------------------|-------------|
| `apostila.docx` | Material do aluno — entregue impresso ou em PDF |
| `roteiros/aulaXX.docx` | Roteiro do professor — uso interno |
| `exemplos/aulaXX_tema.py` | Código demonstrado no datashow |
| `atividades/` | Enunciados das atividades em sala |
| `projetos/` | Projetos práticos e projeto final da UC |
| `🔜 Em breve` | UC ainda não iniciada |
| `✅ Completo` | UC com todos os materiais publicados |

---

## Autor

**Max Muller**
Professor · SENAI-DF
Curso Técnico em Desenvolvimento de Sistemas

[![GitHub](https://img.shields.io/badge/GitHub-MMVonnSeek-181717?style=flat&logo=github)](https://github.com/MMVonnSeek)

---

## Licença

Material didático de uso educacional.

---
<div align="center">
 
[![Stars](https://img.shields.io/github/stars/MMVonnSeek/desenvolvimento-python?style=social)](https://github.com/MMVonnSeek/desenvolvimento-python/stargazers)
[![Forks](https://img.shields.io/github/forks/MMVonnSeek/desenvolvimento-python?style=social)](https://github.com/MMVonnSeek/desenvolvimento-python/network/members)
[![Follow](https://img.shields.io/github/followers/MMVonnSeek?style=social)](https://github.com/MMVonnSeek)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Max_Muller-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/max-muller-685705248/)

<br>

  [Voltar ao topo](#-desenvolvimento-python)

</div>
