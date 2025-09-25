// Escreva um programa que pegue a velocidade de um carro.

// Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.

// A multa vai custar R$ 7,00 por cada Km acima do limite.

let velocidade = 90
let velocidadeMaxima = 80
let valorKm = 7

if (velocidade > velocidadeMaxima){
  let kmUltrapassado = velocidade - velocidadeMaxima
  let multa = kmUltrapassado * valorKm
  console.log("VOCÊ FOI MULTADO E TERÁ QUE PAGAR R$" + multa.toFixed(2));
} else {
  console.log("VOCÊ ESTÁ DENTRO DO LIMITE PERMITIDO");
}