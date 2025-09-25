let times = ["Santos", "Palmeiras", "Corinthians", "São Paulo"]

//Verificar o valor de um item a partir da posição
console.log(times[0]);
console.log(times[3]);

//Adicionando itens no array
times.push("Flamengo")
times.push("Gremio")
times.push("Botafogo")
times.push("Vasco")
console.log(times);

//Verificando o tamanho do array
console.log(times.length);

//Adicionando na primeira posição
times.unshift("Fluminense")
console.log(times);

//Remove item no começo da lista
times.shift()

//Remove item no final da lista
times.pop()
console.log(times);

//Encontra a posição de um item
console.log(times.indexOf("São Paulo"))

let times2 = ["Santos", "São Paulo", "Palmeiras"]

//.splice

//Remover elemento
times2.splice(1,1) // ["Santos" , "// ["Santos" , "São Paulo", "Corinthians", "Palmeiras"]Palmeiras"]
console.log(times2);

//Substituir elementos
times2.splice(1, 0, "São Paulo", "Corinthians") 
// ["Santos" , "São Paulo", "Corinthians", "Palmeiras"]
console.log(times2);