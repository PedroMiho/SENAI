function mostrarResultado(){
    let velocidade = parseInt(document.getElementById("velocidade").value)
    let resultado = document.getElementById("resultado")
    let velocidadeMaxima = 80
    let valorMultaKm = 7

    if (isNaN(velocidade)) {
        resultado.innerHTML = "INFORME UM VALOR VÁLIDO"
        return
    }

    if (velocidade > velocidadeMaxima){
        let diferencaVelocidade = velocidade - velocidadeMaxima
        let multa = diferencaVelocidade * valorMultaKm
        resultado.innerHTML = "Você foi multado<br><br>O valor da sua multa foi de R$" + multa.toFixed(2).replace(".",".")
    }
    else {
        resultado.innerHTML = "Você não foi multado"
    }
}