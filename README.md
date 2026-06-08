# 🐾 Adoção+ — Sistema de Gestão de Centro de Adoção de Animais

> Sistema de linha de comando para gerenciar animais, cuidados e adoções de forma prática e eficiente.

---

## 📋 Sumário

- [Sobre o projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Como executar](#como-executar)
- [Como usar](#como-usar)
  - [Sistema do Gestor](#sistema-do-gestor)
  - [Sistema do Usuário](#sistema-do-usuário)
- [Estrutura de arquivos](#estrutura-de-arquivos)
- [Restrições e observações](#restrições-e-observações)
- [Equipe](#equipe)

---

## Sobre o projeto

Desenvolvido em Python, o **Adoção+** é um sistema elaborado para ajudar centros de adoção de animais a organizar seus registros de forma prática e eficiente. A ferramenta permite cadastrar animais, registrar cuidados e agendamentos, acompanhar datas importantes e encontrar o animal ideal para cada adotante.

Esse projeto foi desenvolvido na disciplina de Fundamentos de Programação, ministrada pelo professor Marcelo Arcoverde.

---

## Funcionalidades

### ✅ CRUD de Animais
Cadastro completo com nome, espécie, raça, idade, estado de saúde, comportamento e data de chegada. É possível adicionar, visualizar, editar e excluir animais.

### ✅ Acompanhamento da Rotina dos Animais
Registro de tarefas para cada animal (vacina, banho, consulta veterinária e treino) com data prevista e responsável atribuído automaticamente por sorteio entre os funcionários.

### ✅ Contagem Regressiva e Alertas
Ao visualizar os cuidados de um animal, o sistema exibe quantos dias faltam para cada agendamento:
- 🔔 **Hoje** — ao cuidado deve ser realizado na data atual.
- 🟢 **Faltam X dia(s)** — está agendado para uma data futura.
- Agendamentos já expirados são excluídos automaticamente sempre que o sistema é iniciado.

### ✅ Armazenamento em CSV
Todos os dados são salvos em arquivos `.csv` na pasta `data/`:
- `animais.csv` — cadastro de animais
- `agendamentos.csv` — registro de cuidados e tarefas

### ✅ Sugestões Personalizadas
O sistema do usuário guia o adotante por filtros progressivos (espécie → raça → faixa de idade → comportamento) para encontrar o animal mais compatível com seu perfil.

### ✅ Funcionalidade Extra — Dois sistemas integrados e sorteio de responsáveis
O sistema é dividido em dois módulos independentes: o sistema do gestor, destinado aos funcionários do centro, e o sistema do usuário, destinado a adotantes. Cada um tem seu próprio fluxo e ponto de entrada, tornando a experiência mais clara e adequada para cada perfil.
Além disso, ao registrar uma tarefa, o sistema sorteia automaticamente um funcionário responsável de forma rotativa, garantindo distribuição justa entre a equipe. Cada funcionário só é sorteado novamente após todos terem sido escolhidos pelo menos uma vez.

---

## Como executar

### Pré-requisitos
- Python 3.x instalado
- Nenhuma biblioteca externa necessária

### Passos

1. Clone o repositório:
```bash
git clone https://github.com/Adocao-G3/projeto-fp-adocao-plus-g3.git
cd projeto-fp-adocao-plus-g3
```

2. Execute o sistema do **gestor** (para funcionários do centro):
```bash
python sistema_gestor.py
```

3. Ou execute o sistema do **usuário** (para adotantes):
```bash
python sistema_usuario.py
```

---

## Como usar

### Sistema do Gestor

Destinado aos funcionários do centro de adoção. Ao iniciar, exibe o menu principal:

```
[1] Adicionar animais
[2] Verificar animais
[3] Atualizar animais
[4] Deletar animais
```

#### [1] Adicionar animais
Informe os dados do animal, incluindo nome, espécie, raça, idade, estado de saúde, comportamento e data de chegada. A data pode ser registrada automaticamente com o dia atual ou inserida manualmente no formato DD/MM/AAAA.

#### [2] Verificar animais
Para localizar um animal, informe seu nome. Se houver mais de um registro com o mesmo nome, o sistema apresentará todos os resultados encontrados para escolha. Em seguida, um submenu com as ações disponíveis será exibido:

```
[1] Ver cuidados cadastrados   → lista tarefas com contagem regressiva
[2] Adicionar novo cuidado     → registra nova tarefa com data e responsável
[3] Voltar ao menu principal
```

#### [3] Atualizar animais
Busca o animal pelo nome e permite editar qualquer campo individualmente. É possível editar múltiplos campos em sequência antes de salvar.

#### [4] Deletar animais
Busca o animal pelo nome, exibe suas informações completas e solicita confirmação antes de excluir.

---

### Sistema do Usuário

Destinado a pessoas interessadas em adotar um animal. O sistema guia o adotante por uma série de filtros:

1. **Espécie** — cachorro, gato, pássaro ou réptil
2. **Raça** — específica ou sem preferência
3. **Idade** — faixa de idade mínima e máxima (use `-1` para sem limite)
4. **Comportamento** — agitado, calmo, neutro ou sem preferência

Ao final, o sistema exibe os animais disponíveis que combinam com o perfil informado.

> ⚠️ Animais com estado de saúde "ruim" não aparecem nos resultados do sistema do usuário.

---

## Estrutura de arquivos

```
projeto-fp-adocao-plus-g3/
│
├── sistema_gestor.py       # Ponto de entrada — sistema do gestor
├── sistema_usuario.py      # Ponto de entrada — sistema do usuário
│
├── src/
│   ├── funcoes.py          # Toda a lógica do sistema
│   ├── menus.py            # Textos e menus exibidos no terminal
│   └── __init__.py
│
└── data/
    ├── animais.csv         # Dados dos animais cadastrados
    └── agendamentos.csv    # Dados dos cuidados e tarefas
```

---

## Restrições e observações

- O sistema funciona **apenas via terminal** (linha de comando)
- Utilize **Python 3.x** — não compatível com Python 2
- A pasta `data/` e os arquivos `.csv` são criados automaticamente na primeira execução
- Datas devem ser inseridas no formato **DD/MM/AAAA**
- Ao iniciar o sistema do gestor, agendamentos com datas passadas são **removidos automaticamente**
- Animais com estado de saúde "ruim" são ocultados do sistema do usuário
- Não há suporte a acentos em alguns terminais Windows — recomenda-se uso do terminal com encoding UTF-8

---

## Equipe

Desenvolvido pelo **Grupo 3** — Turma de Fundamentos de Programação

| Nome | GitHub |
|---|---|
| João Vitor de Melo | [@itsjvsouza](https://github.com/itsjvsouza) |
| João Vitor Rodrigues | [@Rodrigues2109](https://github.com/Rodrigues2109) |
| Jullya Medeiros | [@juuvmed](https://github.com/juuvmed) |
| Lucas Calixto | [@lucas-calixto-lemos](https://github.com/lucas-calixto-lemos) |
| Maria Giulia Maciel | [@mgiuliamaciel](https://github.com/mgiuliamaciel) |
| Mateus Davi | [@mateus-aguiaar](https://github.com/mateus-aguiaar) |
