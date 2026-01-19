package entidades;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;

public class GerenciarAlunos {
    private ArrayList<Aluno> alunos = new ArrayList<Aluno>();

    public void adicionarAluno(Aluno aluno) {
        alunos.add(aluno);
        System.out.println("Aluno adicionado com sucesso!");
    }

    public void listarAlunos() {
        if (alunos.isEmpty()) {
            System.out.println("Nenhum aluno encontrado!");
        } else {
            System.out.println("| id | nome | nota | nota | media |");
            for(int i = 0; i < alunos.size(); i++) {
                System.out.println("| " + i + alunos.get(i).toString());
            }
        }
    }

    public void atualizarAluno(int id, String nome, double nota, double nota2) {
        var aluno = alunos.get(id);
        aluno.setNome(nome);
        aluno.setNota(nota);
        aluno.setNota2(nota2);
        System.out.println("Aluno atualizado com sucesso!");
    }

    public void excluirAluno(int id) {
        alunos.remove(id);
        System.out.println("Aluno removido com sucesso!");
    }

    public void exportarParaTxt() {
        try (PrintWriter writer = new PrintWriter(new FileWriter("alunos.txt"))) {
            for (Aluno aluno : alunos) {
                writer.println("ID: " + alunos.indexOf(aluno));
                writer.println("Nome: " + aluno.getNome());
                writer.println("Nota 1: " + aluno.getNota());
                writer.println("Nota 2: " + aluno.getNota2());
                writer.println("-----------------------------------");
            }
            System.out.println("Arquivo 'alunos.txt' salvo com sucesso!");
        } catch (IOException e) {
            System.out.println("Erro ao salvar o arquivo: " + e.getMessage());
        }
    }





}
