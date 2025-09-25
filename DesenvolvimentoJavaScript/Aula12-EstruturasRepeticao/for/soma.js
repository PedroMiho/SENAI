const input = require("prompt-sync")();
let soma = 0

for(let i = 1; i <= 3; i++){
    let numero = parseInt(input("Digite um valor: "))
    let impar = numero % 2
    let multiplo3 = numero % 3

    if (impar === 1 && multiplo3 === 0) {
        soma = numero + soma
        console.log("ESSE NÚMERO ATENDE AOS REQUISITOS");
    } else {
        console.log("ESSE NÚMERO NÃO ATENDE AOS REQUISITOS");
    }

}

console.log(soma);