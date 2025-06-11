from db import Session, Aluno, Professor, Turma, Disciplina, Nota, Frequencia

def listar_alunos():
    session = Session()
    alunos = session.query(Aluno).all()
    for a in alunos:
        print(f"{a.id}: {a.nome} - Matrícula: {a.matricula}")

def listar_professores():
    session = Session()
    profs = session.query(Professor).all()
    for p in profs:
        print(f"{p.id}: {p.nome} - Email: {p.email}")

def listar_turmas():
    session = Session()
    turmas = session.query(Turma).all()
    for t in turmas:
        print(f"{t.id}: {t.nome} - Disciplina ID: {t.disciplina_id} - Professor ID: {t.professor_id}")

def listar_disciplinas():
    session = Session()
    disc = session.query(Disciplina).all()
    for d in disc:
        print(f"{d.id}: {d.nome} - Créditos: {d.creditos}")

def listar_notas(aluno_id):
    session = Session()
    notas = session.query(Nota).filter_by(aluno_id=aluno_id).all()
    for n in notas:
        print(f"Turma ID: {n.turma_id} - Nota: {n.nota}")

def frequencia_aluno(aluno_id, turma_id):
    session = Session()
    freq = session.query(Frequencia).filter_by(aluno_id=aluno_id, turma_id=turma_id).all()
    for f in freq:
        print(f"{f.data} - {'Presente' if f.presente else 'Ausente'}")

