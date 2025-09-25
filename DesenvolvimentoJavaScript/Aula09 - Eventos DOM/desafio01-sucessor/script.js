function mostrarResultado(){
    //Captura o valor do input
    let numero = parseInt(document.getElementById("numero").value)
    
    //Calcula o sucessor e o antecessor
    let antecessor = numero - 1
    let sucessor = numero + 1

    //Captura o paragrafo
    let resultadoAntecessor = document.querySelector("#antecessor")
    let resultadoSucessor = document.querySelector("#sucessor")

    //Alterando o texto do paragrafo
    resultadoAntecessor.innerHTML = "O antecessor é igual a " + antecessor
    resultadoSucessor.innerHTML = "O sucessor é igual a " + sucessor
}