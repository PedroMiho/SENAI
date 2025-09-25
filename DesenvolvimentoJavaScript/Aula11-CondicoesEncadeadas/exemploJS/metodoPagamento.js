// Valor gasto pelo usuario.
// Metodo de pagamento
//   - 1 - Boleto/Pix = 10% desconto
//   - 2 - Débito = 5% desconto
//   - 3 - Crédito
//   Método Parcelamento
//      1 - A vista = Valor Total   
//      2 - 2x - com juros 5% no valor total
//      3 - 3x - com juros 10% no valor total

let valorGasto = 1000
let metodoPagamento = 3
let valorFinal = 0

if (metodoPagamento == 1) {
    valorFinal = valorGasto * 0.9
    console.log("MÉTODO DE PAGAMENTO BOLETO/PIX")
    console.log("O valor final foi de R$ " + valorFinal); 
} else if (metodoPagamento == 2) {
    valorFinal = valorGasto * 0.95
    console.log("MÉTODO DE PAGAMENTO DÉBITO")
    console.log("O valor final foi de R$ " + valorFinal); 
}
else {
    console.log("MÉTODO DE PAGAMENTO CRÉDTIO")
    let metodoParcelamento = 1
    
    if (metodoParcelamento == 1) {
        console.log("MÉTODO DE PARCELAMENTO - A VISTA")
        console.log("O valor final foi de R$ " + valorGasto); 
    } else if (metodoParcelamento == 2){
        console.log("MÉTODO DE PARCELAMENTO - 2x")
        valorFinal = valorGasto * 1.05
        console.log("O valor final foi de R$ " + valorFinal); 
    }
    else{
        console.log("MÉTODO DE PARCELAMENTO - 3x")
        valorFinal = valorGasto * 1.1
        console.log("O valor final foi de R$ " + valorFinal); 
    }
    

}