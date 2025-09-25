let ladoA = 10
let ladoB = 20
let ladoC = 100

let ladoAB = ladoA + ladoB 
let ladoAC = ladoA + ladoC
let ladoBC = ladoB + ladoC

if (ladoAB > ladoC && ladoAC > ladoB && ladoBC > ladoA){
    console.log("LADOS VÁLIDOS PARA FORMAR UM TRIÂNGULO");
    if (ladoA == ladoB == ladoC) {
        console.log("EQUILÁTERO");
    } else if (ladoA == ladoB || ladoA == ladoC || ladoB == ladoC){
        console.log("ISÓSCELES");
    } else if (ladoA != ladoB != ladoC){
        console.log("ESCALENO");
    }
} 
else {
    console.log("NÃO FOI POSSÍVEL FORMAR UM TRIÂNGULO");
}