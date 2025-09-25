function mostrarResultado(){
    let nota1 = parseInt(document.querySelector("#nota1").value)
    let nota2 = parseInt(document.querySelector("#nota2").value)
    let paragrafoMedia = document.querySelector("#media")
    let paragrafoResultado = document.querySelector("#resultado")

    let media = (nota1 + nota2) / 2
    paragrafoMedia.innerHTML = "A sua média foi de " + media
    
    if (media >= 7){
        paragrafoResultado.innerHTML = "APROVADO"
        paragrafoResultado.style.color = "green"
    }
    else {
        paragrafoResultado.innerHTML = "REPROVADO"
        paragrafoResultado.style.color = "red"
    }

}