//load all tasks
function loadtasks(){
    fetch("/get_tasks")
        .then(response => response.json())
        .then(tasks => {
            const list = document.querySelector("#taskList");
            list.innerHTML = "";

            tasks.forEach(task => {
                const li = document.createElement("li");
                li.textContent = task.task;
                li.classList.add("task_item");
                list.appendChild(li);   
                
                const btn = document.createElement("Button");
                btn.innerHTML = "&#10060;";
                btn.classList.add("btndeletetask");
                btn.onclick = () => {
                    fetch("/delete_task", {
                        method: "POST",
                        headers: {"Content-Type":"application/json"},
                        body: JSON.stringify({id: task.id})
                    })
                    .then(() => loadtasks());
                };
                li.appendChild(btn);
            });
        });
}

window.onload = loadtasks;

function addtask(){
    const inputtask = document.querySelector("#taskinput")
    const task = inputtask.value.trim()

    if (task === "") return;

    fetch("/add_task", {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({task:task})
    })
    .then(()=>{
        inputtask.value = ""
        loadtasks()
    })
}