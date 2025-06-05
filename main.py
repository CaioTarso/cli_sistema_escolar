import argparse
from datetime import date
from db import Session, Professor, Aluno, Disciplina, Turma, Nota, Frequencia
from insertions import add_professor, add_aluno, add_disciplina, add_turma, add_nota, add_frequencia
from batch import add_professores_batch, add_alunos_batch, add_disciplinas_batch, add_turmas_batch, add_notas_batch, add_frequencias_batch
import sqlite3

def main():
    parser = argparse.ArgumentParser(description="Sistema Escolar - CLI")
    subparsers = parser.add_subparsers(dest="comando")

    parser_prof = subparsers.add_parser("add-professor", help="Adiciona um professor")
    parser_prof.add_argument("--nome", required=True)
    parser_prof.add_argument("--email", required=True)

    parser_aluno = subparsers.add_parser("add-aluno", help="Adiciona um aluno")
    parser_aluno.add_argument("--nome", required=True)
    parser_aluno.add_argument("--matricula", required=True)

    parser_disc = subparsers.add_parser("add-disciplina", help="Adiciona uma disciplina")
    parser_disc.add_argument("--nome", required=True)
    parser_disc.add_argument("--professor-id", type=int, required=True)

    parser_turma = subparsers.add_parser("add-turma", help="Adiciona uma turma")
    parser_turma.add_argument("--nome", required=True)
    parser_turma.add_argument("--disciplina-id", type=int, required=True)

    parser_nota = subparsers.add_parser("add-nota", help="Adiciona uma nota")
    parser_nota.add_argument("--aluno-id", type=int, required=True)
    parser_nota.add_argument("--turma-id", type=int, required=True)
    parser_nota.add_argument("--nota", type=float, required=True)

    parser_freq = subparsers.add_parser("add-frequencia", help="Registra frequência")
    parser_freq.add_argument("--aluno-id", type=int, required=True)
    parser_freq.add_argument("--turma-id", type=int, required=True)
    parser_freq.add_argument("--data", type=str, default=str(date.today()))
    parser_freq.add_argument("--presente", type=bool, default=True)

    

    parser_batch_prof = subparsers.add_parser("add-professores-batch")
    parser_batch_prof.add_argument("--arquivo", required=True)

    parser_batch_aluno = subparsers.add_parser("add-alunos-batch")
    parser_batch_aluno.add_argument("--arquivo", required=True)
   
    args = parser.parse_args()
    
    if args.comando == "add-professor":
        add_professor(args)

    elif args.comando == "add-aluno":
        add_aluno(args)

    elif args.comando == "add-disciplina":
        add_disciplina(args)

    elif args.comando == "add-turma":
        add_turma(args)

    elif args.comando == "add-nota":
        add_nota(args)

    elif args.comando == "add-frequencia":
        add_frequencia(args.aluno_id, args.turma_id, args.data, args.presente)
    
    elif args.comando == "add-professores-batch":
        add_professores_batch(args.arquivo)
    
    elif args.comando == "add-alunos-batch":
        add_alunos_batch(args.arquivo)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
