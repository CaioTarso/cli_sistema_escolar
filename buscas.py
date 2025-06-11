from db import Session, Aluno, Professor, Turma, Disciplina, Nota, Frequencia

def listar_alunos():
    session = Session()
    alunos = session.query(Aluno).all()
    for a in alunos:
        print(f"{a.id}: {a.nome} - Matrícula: {a.matricula} - Email: {a.email} - Data de nascimento: {a.data_nascimento} - Curso: {a.curso} - Período: {a.periodo} - Status: {a.status}")
    session.close()

def listar_professores():
    session = Session()
    profs = session.query(Professor).all()
    for p in profs:
        print(f"{p.id}: {p.nome} - Email: {p.email} - Titulação: {p.titulacao} - Departamento: {p.departamento} - Data de Contratação: {p.data_contratacao} - Ativo: {p.ativo}")
    session.close()

def listar_turmas():
    session = Session()
    turmas = session.query(Turma).all()
    for t in turmas:
        print(f"{t.id}: {t.nome} - Disciplina ID: {t.disciplina_id} - Semestre: {t.semestre} - Horário: {t.horario} - Sala: {t.sala} - Vagas Totais: {t.vagas_totais} - Vagas Ocupadas: {t.vagas_ocupadas} - Status: {t.status}")
    session.close()

def listar_disciplinas():
    session = Session()
    disc = session.query(Disciplina).all()
    for d in disc:
        print(f"{d.id}: {d.nome} - Código: {d.codigo} - Créditos: {d.creditos} - Carga Horária: {d.carga_horaria}h - Ementa: {d.ementa} - Pré-requisitos: {d.pre_requisitos} - Departamento: {d.departamento} - Professor ID: {d.professor_id}")
    session.close()

def listar_notas(aluno_id):
    session = Session()
    notas = session.query(Nota).filter_by(aluno_id=aluno_id).all()
    for n in notas:
        print(f"Turma ID: {n.turma_id} - Nota: {n.nota} - Tipo: {n.tipo_avaliacao} - Peso: {n.peso} - Data Lançamento: {n.data_lancamento} - Observação: {n.observacao}")
    session.close()

def frequencia_aluno(aluno_id, turma_id):
    session = Session()
    freq = session.query(Frequencia).filter_by(aluno_id=aluno_id, turma_id=turma_id).all()
    for f in freq:
        print(f"Data: {f.data} - {'Presente' if f.presente else 'Ausente'} - Conteúdo: {f.conteudo_aula} - Justificativa: {f.justificativa}")
    session.close()
