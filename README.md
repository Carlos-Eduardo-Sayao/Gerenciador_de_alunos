Markdown
# Sistema de Gerenciamento de Alunos 🏫

[cite_start]Um sistema em linha de comando (CLI) desenvolvido em Python e MySQL para gerenciar informações escolares, incluindo o cadastro e controle de turmas, alunos e notas[cite: 1].

---

## 🚀 Funcionalidades

[cite_start]O sistema oferece um menu interativo com as seguintes opções[cite: 1]:

* [cite_start]**Gerenciamento de Turmas:** Cadastrar, listar, atualizar dados e deletar turmas[cite: 1].
* [cite_start]**Gerenciamento de Alunos:** Cadastrar, listar (por turma), atualizar dados (matrícula/nome) e deletar alunos[cite: 1].
* [cite_start]**Controle de Notas:** Lançar notas por matéria/unidade, atualizar notas existentes e visualizar o boletim do aluno[cite: 1].

> [cite_start]⚠️ **Atenção:** O sistema utiliza exclusão em cascata (`ON DELETE CASCADE`) no banco de dados[cite: 1]. [cite_start]Se você deletar uma turma, todos os alunos dela serão apagados automaticamente[cite: 1]. [cite_start]Da mesma forma, deletar um aluno removerá todas as suas notas[cite: 1].

---

## 🗄️ Estrutura do Banco de Dados

[cite_start]O banco de dados `sistema_gerenciador_aluno` é composto por três tabelas principais[cite: 1]:

1. [cite_start]**`turmas`**: Armazena as informações das salas (Série, Letra, Ano e Nível de Ensino)[cite: 1].
2. [cite_start]**`alunos`**: Vinculado a uma turma, possui uma matrícula única de exatamente 9 caracteres[cite: 1].
3. [cite_start]**`notas`**: Vinculado a um aluno, armazena a matéria, a unidade e a pontuação[cite: 1].

---

## 🛠️ Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina:
* [Python 3.x](https://www.python.org/downloads/)
* [MySQL Server](https://dev.mysql.com/downloads/installer/)

---

## 🔧 Instalação e Configuração

### 1. Clonar o repositório ou extrair os arquivos
Navegue até a pasta raiz do projeto no seu terminal:
```bash
cd Gerenciador_de_alunos-main
```

### 2. Configurar o Banco de Dados
[cite_start]Abra o seu cliente MySQL (via terminal ou ferramentas como Workbench/DBeaver) e execute o script SQL contido em `database/schema.sql` para criar a estrutura das tabelas[cite: 1].

```bash
# Exemplo via linha de comando:
mysql -u seu_usuario -p < database/schema.sql
```

### 3. Ajustar as credenciais de acesso
[cite_start]Abra o arquivo `database/conexao.py` e altere os campos `user` e `password` com as suas credenciais locais do MySQL[cite: 1]:

```python
def conectar():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "SEU_USUARIO",       # Altere aqui [cite: 1]
        password = "SUA_PASSWORD",   # Altere aqui [cite: 1]
        database = "sistema_gerenciador_aluno" [cite: 1]
    )
    return conn [cite: 1]
```

### 4. Instalar as dependências
[cite_start]Recomenda-se criar um ambiente virtual (`venv`) antes de instalar os pacotes[cite: 1]:

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

[cite_start]Você verá o menu interativo no terminal[cite: 1]. [cite_start]Basta digitar o número correspondente à ação que deseja realizar e seguir as instruções na tela[cite: 1].

---

## 📂 Estrutura de Pastas

```text
├── database/
│   ├── conexao.py  # Gerencia a conexão com o MySQL [cite: 1]
│   └── schema.sql  # Dump estrutural do banco de dados [cite: 1]
├── models/
│   ├── aluno.py    # Classe Aluno [cite: 1]
│   ├── nota.py     # Classe Nota [cite: 1]
│   └── turma.py    # Classe Turma [cite: 1]
├── main.py         # Interface CLI e loop do menu [cite: 1]
├── services.py     # Funções de CRUD e consultas ao banco de dados [cite: 1]
├── requirements.txt# Dependências do projeto [cite: 1]
└── .gitignore      # Arquivos ignorados pelo Git [cite: 1]
```
