from sqlalchemy.orm import Session
from datetime import datetime
from db import Session, Professor, Aluno, Disciplina, Turma, Nota, Frequencia, TurmaAluno

def add_professor(args):
    session = Session()
    novo = Professor(
        nome=args.nome, 
        email=args.email, 
        titulacao=args.titulacao, 
        departamento=args.departamento,
        data_contratacao=datetime.strptime(args.data_contratacao, "%Y-%m-%d").date(),
        ativo=args.ativo
        )
    session.add(novo)
    session.commit()
    print("Professor adicionado com sucesso.")


def add_aluno(args):
    session = Session()
    novo = Aluno(
        nome=args.nome, 
        matricula=args.matricula,
        email=args.email,
        data_nascimento=datetime.strptime(args.data_nascimento, "%Y-%m-%d").date(),
        curso=args.curso,
        periodo=args.periodo,
        status=args.status
        )
    session.add(novo)
    session.commit()
    print("Aluno adicionado com sucesso.")
    session.close()


def add_disciplina(args):
    session = Session()
    novo = Disciplina(
        nome=args.nome, 
        professor_id=args.professor_id,
        codigo=args.codigo,
        creditos=args.creditos,
        carga_horaria=args.carga_horaria,
        ementa=args.ementa,
        pre_requisitos=args.pre_requisitos,
        departamento=args.departamento
        )
    session.add(novo)
    session.commit()
    print("Disciplina adicionada com sucesso.")
    session.close()



def add_turma(args):
    session = Session()
    novo = Turma(
        nome=args.nome, 
        disciplina_id=args.disciplina_id,
        semestre=args.semestre,
        horario=args.horario,
        sala=args.sala,
        vagas_totais=args.vagas_totais,
        vagas_ocupadas=args.vagas_ocupadas,
        status=args.status
        )
    session.add(novo)
    session.commit()
    print("Turma adicionada com sucesso.")
    session.close()


def add_nota(args):
    session = Session()
    novo = Nota(
        aluno_id=args.aluno_id, 
        turma_id=args.turma_id, 
        nota=args.nota,
        tipo_avaliacao=args.tipo_avaliacao,
        peso=args.peso,
        data_lancamento=datetime.strptime(args.data_lancamento, "%Y-%m-%d").date(),
        observacao=args.observacao
        )
    session.add(novo)

    stmt = TurmaAluno.insert().prefix_with('OR IGNORE').values(
        aluno_id=args.aluno_id, 
        turma_id=args.turma_id
    )
    session.execute(stmt)

    session.commit()
    print("Nota adicionada com sucesso.")
    session.close()



def add_frequencia(args):
    session = Session()
    data_obj = datetime.strptime(args.data, "%Y-%m-%d").date()
    novo = Frequencia(
        aluno_id=args.aluno_id, 
        turma_id=args.turma_id, 
        data=data_obj, 
        presente=args.presente,
        justificativa=args.justificativa,
        conteudo_aula=args.conteudo_aula,
        )
    session.add(novo)

    stmt = TurmaAluno.insert().prefix_with('OR IGNORE').values(
        turma_id=args.turma_id,
        aluno_id=args.aluno_id
    )
    session.execute(stmt)
    
    session.commit()
    print("Frequência registrada com sucesso.")
    session.close()