import csv
from datetime import datetime
from db import Session, Aluno, Professor, Disciplina, Turma, Nota, Frequencia

def load_csv(filepath):
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        return list(csv.DictReader(csvfile))

def add_professores_batch(arquivo):
    session = Session()
    for row in load_csv(arquivo):
        session.add(Professor(
            nome=row["nome"],
            email=row["email"],
            titulacao=row.get("titulacao"),
            departamento=row.get("departamento"),
            data_contratacao=datetime.strptime(row["data_contratacao"], "%Y-%m-%d").date() if row.get("data_contratacao") else None,
            ativo=row.get("ativo", "True").lower() == "true"
        ))
    session.commit()
    print("Professores adicionados em lote!")

def add_alunos_batch(arquivo):
    session = Session()
    for row in load_csv(arquivo):
        session.add(Aluno(
            nome=row["nome"],
            matricula=row["matricula"],
            email=row.get("email"),
            data_nascimento=datetime.strptime(row["data_nascimento"], "%Y-%m-%d").date() if row.get("data_nascimento") else None,
            curso=row.get("curso"),
            periodo=int(row["periodo"]) if row.get("periodo") else None,
            status=row.get("status", "ativo")
        ))
    session.commit()
    print("Alunos adicionados em lote!")

def add_disciplinas_batch(arquivo):
    session = Session()
    for row in load_csv(arquivo):
        session.add(Disciplina(
            nome=row["nome"],
            professor_id=int(row["professor_id"]),
            codigo=row["codigo"],
            creditos=int(row["creditos"]),
            carga_horaria=int(row["carga_horaria"]),
            ementa=row.get("ementa"),
            pre_requisitos=row.get("pre_requisitos"),
            departamento=row.get("departamento")
        ))
    session.commit()
    print("Disciplinas adicionadas em lote!")

def add_turmas_batch(arquivo):
    session = Session()
    for row in load_csv(arquivo):
        session.add(Turma(
            nome=row["nome"],
            disciplina_id=int(row["disciplina_id"]),
            semestre=row["semestre"],
            horario=row.get("horario"),
            sala=row.get("sala"),
            vagas_totais=int(row["vagas_totais"]),
            vagas_ocupadas=int(row["vagas_ocupadas"]),
            status=row.get("status", "ativa")
        ))
    session.commit()
    print("Turmas adicionadas em lote!")

def add_notas_batch(arquivo):
    session = Session()
    for row in load_csv(arquivo):
        session.add(Nota(
            aluno_id=int(row["aluno_id"]),
            turma_id=int(row["turma_id"]),
            nota=float(row["nota"]),
            tipo_avaliacao=row.get("tipo_avaliacao"),
            peso=float(row["peso"]) if row.get("peso") else None,
            data_lancamento=datetime.strptime(row["data_lancamento"], "%Y-%m-%d").date() if row.get("data_lancamento") else None,
            observacao=row.get("observacao")
        ))
    session.commit()
    print("Notas adicionadas em lote!")

def add_frequencias_batch(arquivo):
    session = Session()
    for row in load_csv(arquivo):
        session.add(Frequencia(
            aluno_id=int(row["aluno_id"]),
            turma_id=int(row["turma_id"]),
            data=datetime.strptime(row["data"], "%Y-%m-%d").date(),
            presente=row.get("presente", "True").lower() == "true",
            conteudo_aula=row.get("conteudo_aula"),
            justificativa=row.get("justificativa")
        ))
    session.commit()
    print("Frequências adicionadas em lote!")
