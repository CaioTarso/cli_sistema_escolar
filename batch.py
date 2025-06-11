import csv
from db import Session, Professor, Aluno, Disciplina, Turma, Nota, Frequencia
from datetime import datetime

def load_csv(filepath):
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        return list(csv.DictReader(csvfile))

def add_professores_batch(arquivo):
    session = Session()
    for row in load_csv(arquivo):
        session.add(Professor(nome=row["nome"], email=row["email"]))
    session.commit()
    print("Professores adicionados em lote!")

def add_alunos_batch(arquivo):
    session = Session()
    for row in load_csv(arquivo):
        session.add(Aluno(nome=row["nome"], matricula=row["matricula"]))
    session.commit()
    print("Alunos adicionados em lote!")

def add_disciplinas_batch(arquivo):
    session = Session()
    for row in load_csv(arquivo):
        session.add(Disciplina(nome=row["nome"], professor_id=int(row["professor_id"])))
    session.commit()
    print("Disciplinas adicionadas em lote!")

def add_turmas_batch(arquivo):
    session = Session()
    for row in load_csv(arquivo):
        session.add(Turma(nome=row["nome"], disciplina_id=int(row["disciplina_id"])))
    session.commit()
    print("Turmas adicionadas em lote!")

def add_notas_batch(arquivo):
    session = Session()
    for row in load_csv(arquivo):
        session.add(Nota(aluno_id=int(row["aluno_id"]), turma_id=int(row["turma_id"]), nota=float(row["nota"])))
    session.commit()
    print("Notas adicionadas em lote!")

def add_frequencias_batch(arquivo):
    session = Session()
    for row in load_csv(arquivo):
        
        presente = row.get("presente") == "--presente"

        session.add(Frequencia(
            aluno_id=int(row["aluno_id"]),
            turma_id=int(row["turma_id"]),
            data=datetime.strptime(row["data"], "%Y-%m-%d").date(),
            presente=presente
        ))
    session.commit()
    print("Frequências adicionadas em lote!")
