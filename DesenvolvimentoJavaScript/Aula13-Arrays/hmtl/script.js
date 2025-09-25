let tarefas = []

function adicionarTarefa(){
    let tarefa = document.getElementById("nova-tarefa").value
    if (tarefa) {
        tarefas.push(tarefa)
        exibeTarefas()
        tarefa = ""
    }
    console.log(tarefas);
}

function exibeTarefas(){
    let listaTarefas = document.getElementById("lista-tarefas")
    listaTarefas.innerHTML = ""
    tarefas.forEach((tarefa) => {
        let li = document.createElement("li")
        li.innerHTML = tarefa
        listaTarefas.appendChild(li)
    })

    
}