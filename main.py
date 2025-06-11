import argparse
from datetime import date
from insertions import add_professor, add_aluno, add_disciplina, add_turma, add_nota, add_frequencia
from batch import add_professores_batch, add_alunos_batch, add_disciplinas_batch, add_turmas_batch, add_notas_batch, add_frequencias_batch
from buscas import listar_alunos, listar_professores, listar_turmas, listar_disciplinas, listar_notas, frequencia_aluno
import sqlite3

def main():
    parser = argparse.ArgumentParser(description="Sistema Escolar - CLI")
    subparsers = parser.add_subparsers(dest="comando")
    
    # Comandos para inserção de dados
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
    parser_freq.add_argument("--presente", action="store_true", help="Indica se o aluno esteve presente")

    
    # Comandos para inserção em lote
    parser_batch_prof = subparsers.add_parser("add-professores-batch")
    parser_batch_prof.add_argument("--arquivo", required=True)

    parser_batch_aluno = subparsers.add_parser("add-alunos-batch")
    parser_batch_aluno.add_argument("--arquivo", required=True)

    parser_batch_disc = subparsers.add_parser("add-disciplinas-batch")
    parser_batch_disc.add_argument("--arquivo", required=True)

    parser_batch_turma = subparsers.add_parser("add-turmas-batch")
    parser_batch_turma.add_argument("--arquivo", required=True)

    parser_batch_nota = subparsers.add_parser("add-notas-batch")
    parser_batch_nota.add_argument("--arquivo", required=True)

    parser_batch_freq = subparsers.add_parser("add-frequencias-batch")
    parser_batch_freq.add_argument("--arquivo", required=True)
    
    # Comandos para listagem de dados
    parser_listar_alunos = subparsers.add_parser("listar-alunos", help="Lista todos os alunos")
    parser_listar_alunos.add_argument("--matricula", type=str, help="Filtra por matrícula")

    parser_listar_professores = subparsers.add_parser("listar-professores", help="Lista todos os professores")
    parser_listar_professores.add_argument("--email", type=str, help="Filtra por email")

    parser_listar_turmas = subparsers.add_parser("listar-turmas" , help="Lista todas as turmas")
    parser_listar_turmas.add_argument("--disciplina-id", type=int, help="Filtra por disciplina")

    parser_listar_disciplinas = subparsers.add_parser("listar-disciplinas" , help="Lista todas as disciplinas")
    parser_listar_disciplinas.add_argument("--professor-id", type=int, help="Filtra por professor")

    parser_listar_notas = subparsers.add_parser("listar-notas", help="Lista as notas de um aluno")
    parser_listar_notas.add_argument("--aluno-id", type=int, required=True)

    parser_frequencia = subparsers.add_parser("frequencia-aluno")
    parser_frequencia.add_argument("--aluno-id", type=int, required=True)
    parser_frequencia.add_argument("--turma-id", type=int, required=True)
   
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
        add_frequencia(args)
    
    elif args.comando == "add-professores-batch":
        add_professores_batch(args.arquivo)
    
    elif args.comando == "add-alunos-batch":
        add_alunos_batch(args.arquivo)

    elif args.comando == "add-notas-batch":
        add_notas_batch(args.arquivo)

    elif args.comando == "add-disciplinas-batch":
        add_disciplinas_batch(args.arquivo)

    elif args.comando == "add-turmas-batch":
        add_turmas_batch(args.arquivo)
    
    elif args.comando == "add-frequencias-batch":
        add_frequencias_batch(args.arquivo)
    
    elif args.comando == "listar-alunos":
        listar_alunos()
    
    elif args.comando == "listar-professores":
        listar_professores()
    
    elif args.comando == "listar-turmas":
        listar_turmas()
    
    elif args.comando == "listar-disciplinas":
        listar_disciplinas()
    
    elif args.comando == "listar-notas":
        listar_notas(args.aluno_id)
    
    elif args.comando == "frequencia-aluno":
        frequencia_aluno(args.aluno_id, args.turma_id)
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
