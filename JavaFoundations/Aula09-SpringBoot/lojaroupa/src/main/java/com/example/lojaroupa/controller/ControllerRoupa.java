package com.example.lojaroupa.controller;

import com.example.lojaroupa.model.DadosRoupa;
import com.example.lojaroupa.model.Roupa;
import com.example.lojaroupa.model.RoupaRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

// Controller - Responsável por receber as requisições em HTTP
// Rest - API Rest

// Funcionamento da API REST - Ela usa metodo HTTP para definir ações
// Metodo GET - Busca Dados
// Metodo POST - Criar Dados
// Metodo PUT - Atualizar Dados
// Metodo DELETE - Remover Dados
@RestController
// Define a URL do Controller
// Nosso controller terá o seguinte endpoint
// http://localhost:8080/roupas
@RequestMapping("/roupas")
// Liberar o acesso
@CrossOrigin(origins = "*")
public class ControllerRoupa {

    @Autowired
    private RoupaRepository roupaRepository;

    //Registrar uma roupa no banco
    @PostMapping
    public void cadastrarRoupa(@RequestBody DadosRoupa dadosRoupa) {
        System.out.println(dadosRoupa);
        roupaRepository.save(new Roupa(dadosRoupa));
    }

    @GetMapping
    public List<Roupa> listarRoupas() {
        return roupaRepository.findAll();
    }

}
