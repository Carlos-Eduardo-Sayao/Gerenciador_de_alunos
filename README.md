🇺🇸 **English version:** [Click here](https://github.com/Carlos-Eduardo-Sayao/Gerenciador_de_alunos/blob/main/README_EN.md)

# Sistema de Gerenciamento de Alunos 🏫

Um sistema em linha de comando (CLI) desenvolvido em Python e MySQL para gerenciar informações escolares, incluindo o cadastro e controle de turmas, alunos e notas.

---

## 🚀 Funcionalidades

O sistema oferece um menu interativo com as seguintes opções:

* **Gerenciamento de Turmas:** Cadastrar, listar, atualizar dados e deletar turmas.
* **Gerenciamento de Alunos:** Cadastrar, listar (por turma), atualizar dados (matrícula/nome) e deletar alunos.
* **Controle de Notas:** Lançar notas por matéria/unidade, atualizar notas existentes e visualizar o boletim do aluno.

> ⚠️ **Atenção:** O sistema utiliza exclusão em cascata (`ON DELETE CASCADE`) no banco de dados. Se você deletar uma turma, todos os alunos dela serão apagados automaticamente. Da mesma forma, deletar um aluno removerá todas as suas notas.

---

## 🗄️ Estrutura do Banco de Dados

O banco de dados `sistema_gerenciador_aluno` é composto por três tabelas principais:

1. **`turmas`**: Armazena as informações das salas (Série, Letra, Ano e Nível de Ensino).
2. **`alunos`**: Vinculado a uma turma, possui uma matrícula única de exatamente 9 caracteres.
3. **`notas`**: Vinculado a um aluno, armazena a matéria, a unidade e a pontuação.

---

## 🛠️ Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina:
* Python 3
* MySQL Server

---

## 🔧 Instalação e Configuração

### 1. Clonar o repositório ou extrair os arquivos
Navegue até a pasta raiz do projeto no seu terminal:
```bash
cd Gerenciador_de_alunos-main
```

### 2. Configurar o Banco de Dados
Abra o seu cliente MySQL (via terminal ou ferramentas como Workbench/DBeaver) e execute o script SQL contido em `database/schema.sql` para criar a estrutura das tabelas.

```bash
# Exemplo via linha de comando:
mysql -u seu_usuario -p < database/schema.sql
```

### 3. Ajustar as credenciais de acesso
Abra o arquivo `database/conexao.py` e altere os campos `user` e `password` com as suas credenciais locais do MySQL:

```python
def conectar():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "SEU_USUARIO",       # Altere aqui 
        password = "SUA_PASSWORD",   # Altere aqui 
        database = "sistema_gerenciador_aluno" 
    )
    return conn 
```

### 4. Instalar as dependências
Recomenda-se criar um ambiente virtual (`venv`) antes de instalar os pacotes:

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# No Windows:
venv\Scripts\activate
# No Linux/macOS:
source venv/bin/activate

# Instalar pacotes necessários
pip install -r requirements.txt
```

---

## 💻 Como Rodar o Sistema

Com o banco de dados configurado e ativo, basta executar o arquivo principal:

```bash
python main.py
```

Você verá o menu interativo no terminal. Basta digitar o número correspondente à ação que deseja realizar e seguir as instruções na tela.

---

## 📂 Estrutura de Pastas

```text
├── database/
│   ├── conexao.py  # Gerencia a conexão com o MySQL 
│   └── schema.sql  # Dump estrutural do banco de dados 
├── models/
│   ├── aluno.py    # Classe Aluno 
│   ├── nota.py     # Classe Nota 
│   └── turma.py    # Classe Turma 
├── main.py         # Interface CLI e loop do menu 
├── services.py     # Funções de CRUD e consultas ao banco de dados 
├── requirements.txt# Dependências do projeto 
└── .gitignore      # Arquivos ignorados pelo Git 
```
