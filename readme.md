
# CLI - SISTEMA ESCOLAR

CLI: significa "Command Line Interface" (Interface de Linha de Comando). É uma interface de interação com um sistema de computador ou software que utiliza comandos de texto digitados pelo usuário, em vez de uma interface gráfica. 


Esse sistema foi feito para disciplina de Modelagem de banco de dados, e tem como base a prática dos fundamentos aprendidos em sala.

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
 python3 main.py add-professor --nome "teste" --email "email@exemplo.com" --titulacao "Doutor" --departamento "TI" --data_contratacao "2024-08-09" --ativo False
```

2. Adicionar Aluno:
```bash
python3 main.py add-aluno --nome "ruyter" --matricula "2023001" --email "xaolim@gamil.com" --data_nascimento 2004-04-14 --curso "Engenharia" --periodo 4 --status "Ativo"
```

3. Adicionar Disciplina
```bash
python3 main.py add-disciplina --nome "Matemática 2" --professor-id 1 --codigo "3" --creditos 40 --carga_horaria 50 --ementa "estudo de funcoes" --pre_requisitos "ter cursado matemática 1" --departamento "exatas"
```

4. Adicionar Turma
```bash
python3 main.py add-turma --nome "Turma A" --disciplina_id 1 --semestre "2025.1" --horario "SEX 13:00-15:00" --sala "2C" --vagas_totais 40 --vagas_ocupadas 0 --status "Ativa"
```

5. Adicionar Nota
```bash
python3 main.py add-nota --aluno_id 1 --turma_id 1 --nota 9.5 --tipo_avaliacao "Prova" --peso 1.0 --data_lancamento 2025-06-11 --observacao "aluno caiu rendimento"
```

4. Registrar Frequência:
```bash
python3 main.py add-frequencia --aluno_id 1 --turma_id 1 --data "2025-06-04" --presente True --conteudo_aula "matriz"
```
```bash
python3 main.py add-frequencia --aluno_id 1 --turma_id 1 --data "2025-06-04" --presente False --justificativa "Doente" --conteudo_aula "matriz"
```


# Adicionado por lotes(CSV)

1.
```bash
python3 main.py add-professores-batch --arquivo "csvs/professores.csv"
```
2.
```bash
python3 main.py add-alunos-batch --arquivo "csvs/alunos.csv"
```
3.
```bash
python3 main.py add-disciplinas-batch --arquivo "csvs/disciplinas.csv"
```
4.
```bash
python3 main.py add-turmas-batch --arquivo "csvs/turmas.csv"
```
5.
```bash
python3 main.py add-notas-batch --arquivo "csvs/notas.csv"
```
6.
```bash
python3 main.py add-frequencias-batch --arquivo "csvs/frequencias.csv"
```
#  Fazendo buscas 

1. Listar Alunos
```bash
python3 main.py listar-alunos
```
```bash
python3 main.py listar-alunos --matricula "2023001"
```
2. Listar Professores
```bash
python3 main.py listar-professores
```
```bash
python3 main.py listar-professores --email "professor@email.com"
```

3. Listar Turmas
```bash
python3 main.py listar-turmas
```
```bash
python3 main.py listar-turmas --disciplina-id 1
```

4. Listar Disciplinas
```bash
python3 main.py listar-disciplinas
```
```bash
python3 main.py listar-disciplinas --professor-id 1
```

5. Listar Notas
```bash
python3 main.py listar-notas --aluno-id 1
```
6. Consultar Frequência
```bash
python3 main.py frequencia-aluno --aluno-id 1 --turma-id 1
```