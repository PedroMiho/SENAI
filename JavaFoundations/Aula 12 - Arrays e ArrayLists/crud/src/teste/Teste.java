package teste;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Scanner;

public class Teste {

	public static void main(String[] args) {
		ArrayList<String> listaLanches = new ArrayList<>();
		ArrayList<Double> listaPreco = new ArrayList<>();
		
		ArrayList<String> lanches = new ArrayList<>();
		ArrayList<Double> preco = new ArrayList<>();
		
		listaLanches.add("X-Burguer");
		listaLanches.add("X-Egg");
		listaLanches.add("X-Bacon");
		listaLanches.add("X-Tudo");
		
		listaPreco.add(15.99);
		listaPreco.add(17.90);
		listaPreco.add(22.90);
		listaPreco.add(25.90);
		
		
		
		
		Scanner sc = new Scanner(System.in);
		
		while (true) {
			
			exibirMenu();
			String opcao = sc.nextLine();
			
			
			switch (opcao) {
			case "1":
				
				mostrarLanches(listaLanches, listaPreco);
				System.out.println("Informe a posicao do lanche desejado");
				int opcaoLanche = sc.nextInt();
				sc.nextLine();
				String escolhaLanche = listaLanches.get(opcaoLanche);
				double precoLanche = listaPreco.get(opcaoLanche);
				
				lanches.add(escolhaLanche);
				preco.add(precoLanche);
				System.out.println("O lanche " + escolhaLanche + " foi adicionado com sucesso");
				break;
			case "2":
				listasLanches(lanches, preco);
				System.out.println("Informe a posição que deseja alterar: ");
				int alteraLanche = sc.nextInt();
				sc.nextLine();
				exluirLanche(lanches, preco, alteraLanche);
				mostrarLanches(listaLanches, listaPreco);
				System.out.println("Informe qual lanche deseja inserir: ");
				int opcao1 = sc.nextInt();
				sc.nextLine();
				String escolha = listaLanches.get(opcao1);
				double preco1 = listaPreco.get(opcao1);
				lanches.add(escolha);
				preco.add(preco1);
				break;



			case "3":
				listasLanches(lanches, preco);
				break;
			default:
				break;
			}
			
			
			
		}
		
	}
	
	static void mostrarLanches(ArrayList<String> listaLanches, ArrayList<Double> listaPreco) {
		for(int i = 0; i < listaPreco.size(); i++ ) {
			System.out.println(i + " - Lanche - " + listaLanches.get(i) + " - Preco R$ " + listaPreco.get(i) );
		}
	}
	
	static void exibirMenu() {
		
		System.out.println("ESCOLHA UMA OPCAO");
		System.out.println("1 - Adicionar Lanche");
		System.out.println("2 - Atualizar Lanche");
		System.out.println("3 - Listar Lanches");
		System.out.println("4 - Excluir Lanche");
		System.out.println("5 - Sair do Programa");
		
	}

	static void exluirLanche(ArrayList<String> lanches,ArrayList<Double> preco, int opcao) {
		lanches.remove(opcao);
		preco.remove(opcao);

	}

	static void listasLanches(ArrayList<String> lanches,ArrayList<Double> preco) {
		System.out.println("OS LANCHES ESCOLHIDOS FORAM");
		for(int i = 0; i < lanches.size(); i++ ) {
			System.out.println(i + " - Lanche - " + lanches.get(i) + " - Preco R$ " + preco.get(i) );
		}
		
	}



}
