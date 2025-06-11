from sqlalchemy import Column, Integer, String, Float, Date, Boolean, ForeignKey, create_engine, Table
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

class Aluno(Base):
    __tablename__ = 'alunos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    matricula = Column(String(20), unique=True, nullable=False)
    

class Disciplina(Base):
    __tablename__ = 'disciplinas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    professor_id = Column(Integer, ForeignKey('professores.id'))

class Turma(Base):
    __tablename__ = 'turmas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    disciplina_id = Column(Integer, ForeignKey('disciplinas.id'))
    alunos = relationship('Aluno', secondary=TurmaAluno, backref='turmas')
   


class Nota(Base):
    __tablename__ = 'notas'
    id = Column(Integer, primary_key=True)
    aluno_id = Column(Integer, ForeignKey('alunos.id'))
    turma_id = Column(Integer, ForeignKey('turmas.id'))
    nota = Column(Float, nullable=False)

class Frequencia(Base):
    __tablename__ = 'frequencias'
    id = Column(Integer, primary_key=True)
    aluno_id = Column(Integer, ForeignKey('alunos.id'))
    turma_id = Column(Integer, ForeignKey('turmas.id'))
    data = Column(Date, nullable=False)
    presente = Column(Boolean, default=True)

if __name__ == "__main__":
    Base.metadata.create_all(engine)