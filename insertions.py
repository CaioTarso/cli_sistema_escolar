from sqlalchemy.orm import Session
from db import Session, Professor, Aluno, Disciplina, Turma, Nota, Frequencia

def add_professor(args):
    session = Session()
    novo = Professor(nome=args.nome, email=args.email)
    session.add(novo)
    session.commit()
    print("Professor adicionado com sucesso.")


def add_aluno(args):
    session = Session()
    novo = Aluno(nome=args.nome, matricula=args.matricula)
    session.add(novo)
    session.commit()
    print("Aluno adicionado com sucesso.")
    session.close()


def add_disciplina(args):
    session = Session()
    novo = Disciplina(nome=args.nome, professor_id=args.professor_id)
    session.add(novo)
    session.commit()
    print("Disciplina adicionada com sucesso.")
    session.close()



def add_turma(args):
    session = Session()
    novo = Turma(nome=args.nome, disciplina_id=args.disciplina_id)
    session.add(novo)
    session.commit()
    print("Turma adicionada com sucesso.")
    session.close()


def add_nota(args):
    sessio = Session()
    novo = Nota(aluno_id=args.aluno_id, turma_id=args.turma_id, nota=args.nota)
    sessio.add(novo)
    sessio.commit()
    print("Nota adicionada com sucesso.")
    sessio.close()



def add_frequencia(aluno_id, turma_id, data, presente):
    # TODO: implementar inserção no banco
    print(f"[SIMULAÇÃO] Frequência: Aluno ID: {aluno_id}, Turma ID: {turma_id}, Data: {data}, Presente: {presente}")