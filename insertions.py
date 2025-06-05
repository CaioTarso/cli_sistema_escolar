from sqlalchemy.orm import Session
from datetime import datetime
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
    session = Session()
    novo = Nota(aluno_id=args.aluno_id, turma_id=args.turma_id, nota=args.nota)
    session.add(novo)
    session.commit()
    print("Nota adicionada com sucesso.")
    session.close()



def add_frequencia(args):
    session = Session()
    data_obj = datetime.strptime(args.data, "%Y-%m-%d").date()
    nova_freq = Frequencia(aluno_id=args.aluno_id, turma_id=args.turma_id, data=data_obj, presente=args.presente)
    session.add(nova_freq)
    session.commit()
    print("Frequência registrada com sucesso.")
    session.close()