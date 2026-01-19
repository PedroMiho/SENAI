package com.example.lojaroupa.model;

import jakarta.persistence.*;
import lombok.*;

// Informa qual tabela do banco se relaciona a entidade
@Table(name = "roupa")
// Informa que a classe Roupa é uma entidade JPA
// Mapea a Classe para o banco
@Entity(name = "Roupa")
// Lombok
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@EqualsAndHashCode(of = "id")
public class Roupa {

    @Id //Informe que o id é a chave primaria
    @GeneratedValue(strategy = GenerationType.IDENTITY) // Informa que o banco gera o valor do id
    private int id;
    private String marca;
    private String tipo;
    private  String tamanho;
    private int quantidade;
    private double preco;

    public Roupa(DadosRoupa dadosRoupa) {
        this.marca = dadosRoupa.marca();
        this.tipo = dadosRoupa.tipo();
        this.tamanho = dadosRoupa.tamanho();
        this.quantidade = dadosRoupa.quantidade();
        this.preco = dadosRoupa.preco();
    }
}
