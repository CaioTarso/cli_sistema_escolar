
# CLI - SISTEMA ESCOLAR

Esse sistema foi feito para disciplina de Modelagem de bano de dados, e tem como base a prática dos fundamentos aprendidos em sala.

# para rodar o sistema siga esse passos abaixo:

### Requisitos

1. **Python**
   - Python 3.8 ou superior
   - Gerenciador de pacotes pip

2. **Dependências**
   - SQLAlchemy
   - datetime

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/CaioTarso/cli_sistema_escolar.git
cd cli_sistema_escolar
```

2. Instale as dependências:
```bash
pip install sqlalchemy
```

3. Configure o banco de dados:
```bash
python3 db.py
```

### Como Usar

Exemplos de comandos disponíveis:

1. Adicionar Professor:
```bash
python3 main.py add-professor --nome "Nome Professor" --email "email@exemplo.com"
```

2. Adicionar Aluno:
```bash
python3 main.py add-aluno --nome "Nome Aluno" --matricula "2023001"
```

3. Registrar Frequência:
```bash
python3 main.py add-frequencia --aluno-id 1 --turma-id 1 --data "2025-06-04" --presente 
```
## atenção: em frequência, se você quiser registrar um aluno com "falta" repita o comando anterior, porém, sem o "--presente"
```bash
python3 main.py add-frequencia --aluno-id 1 --turma-id --data "2025-06-04" 
```