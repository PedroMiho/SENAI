// Desenvolva um programa que pergunte a distância de uma viagem em
// Km. Calcule o preço da passagem cobrando R$ 0,50 por Km para
// viagens de até 200 Km e R$ 0,45 para viagens mais longas.

let distancia = 900
let distanciaMaxima = 200
let valor = 0

if (distancia < distanciaMaxima) {
    valor = distancia * 0.5
    console.log("A viagem ficou no valor de R$" + valor);
} else {
    valor = distancia * 0.45
    console.log("A viagem ficou no valor de R$" + valor);
}