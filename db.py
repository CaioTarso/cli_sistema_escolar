from sqlalchemy import Column, Integer, String, Float, Date, Boolean, ForeignKey, create_engine, Table, Text
from sqlalchemy.orm import sessionmaker, declarative_base, Session, relationship

engine = create_engine('sqlite:///meubanco.db')

Base = declarative_base()

Session = sessionmaker(bind=engine)

session = Session()

TurmaAluno = Table(
    'turma_aluno',
    Base.metadata,
    Column('turma_id', Integer, ForeignKey('turmas.id'), primary_key=True),
    Column('aluno_id', Integer, ForeignKey('alunos.id'), primary_key=True)
)

class Professor(Base):
    __tablename__ = 'professores'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    titulacao = Column(String(50))  # Mestre, Doutor, etc
    departamento = Column(String(100))
    data_contratacao = Column(Date)
    ativo = Column(Boolean, default=True)


class Aluno(Base):
    __tablename__ = 'alunos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    matricula = Column(String(20), unique=True, nullable=False)
    email = Column(String(100), unique=True)
    data_nascimento = Column(Date)
    curso = Column(String(100))
    periodo = Column(Integer)  # Semestre atual do aluno
    status = Column(String(20))  # Ativo, Trancado, etc
    

class Disciplina(Base):
    __tablename__ = 'disciplinas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    codigo = Column(String(20), unique=True)
    creditos = Column(Integer, nullable=False)
    carga_horaria = Column(Integer)  # Em horas
    ementa = Column(Text)
    pre_requisitos = Column(String(200))
    professor_id = Column(Integer, ForeignKey('professores.id'))
    departamento = Column(String(100))

class Turma(Base):
    __tablename__ = 'turmas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    disciplina_id = Column(Integer, ForeignKey('disciplinas.id'))
    semestre = Column(String(6))  # Ex: 2023.1
    horario = Column(String(100))  # Ex: SEG 14:00-16:00
    sala = Column(String(50))
    vagas_totais = Column(Integer)
    vagas_ocupadas = Column(Integer, default=0)
    status = Column(String(20))  # Ativa, Cancelada, Concluída
   


class Nota(Base):
    __tablename__ = 'notas'
    id = Column(Integer, primary_key=True)
    aluno_id = Column(Integer, ForeignKey('alunos.id'))
    turma_id = Column(Integer, ForeignKey('turmas.id'))
    nota = Column(Float, nullable=False)
    tipo_avaliacao = Column(String(50))  # Prova 1, Trabalho, etc
    peso = Column(Float, default=1.0)
    data_lancamento = Column(Date)
    observacao = Column(Text)

class Frequencia(Base):
    __tablename__ = 'frequencias'
    id = Column(Integer, primary_key=True)
    aluno_id = Column(Integer, ForeignKey('alunos.id'))
    turma_id = Column(Integer, ForeignKey('turmas.id'))
    data = Column(Date, nullable=False)
    presente = Column(Boolean, default=True)
    justificativa = Column(Text)  # Para casos de ausência justificada
    conteudo_aula = Column(String(200))  # Tópico dado na aula

if __name__ == "__main__":
    Base.metadata.create_all(engine)