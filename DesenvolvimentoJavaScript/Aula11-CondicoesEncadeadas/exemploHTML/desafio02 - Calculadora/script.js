function mostrarResultado(){
    let numero1 = parseInt(document.querySelector("#num1").value)
    let numero2 = parseInt(document.querySelector("#num2").value)
    let operacao = document.getElementById("operacao").value
    let resultado = document.querySelector("#resultado")
    let resultaConta = 0

    if (operacao === "1") {
        resultaConta = numero1 + numero2
        resultado.innerHTML = `A soma entre ${numero1} e ${numero2} é igual  ${resultaConta}`
    }
    else if (operacao === "2") {
        resultaConta = numero1 - numero2
        resultado.innerHTML = `A subtração entre ${numero1} e ${numero2} é igual  ${resultaConta}`
    }
    else if (operacao === "3") {
        resultaConta = numero1 * numero2
        resultado.innerHTML = `A multiplicação entre ${numero1} e ${numero2} é igual  ${resultaConta}`
    } 
    else {
        resultaConta = numero1 / numero2
        resultado.innerHTML = `A divisão entre ${numero1} e ${numero2} é igual  ${resultaConta}`
    } 
}