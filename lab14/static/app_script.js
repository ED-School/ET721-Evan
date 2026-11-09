console.log("Evan Dong")
const itemForm = document.querySelector('#itemForm')
itemForm.addEventListener("submit", async function(event) {
    event.preventDefault()
    const name = document.querySelector('#name').value
    const price = document.querySelector('#price').value

    try{
        const res = await fetch("http://127.0.0.1:5000/items", {method: "POST", headers: {"Content-type":"application/json"} ,
            body: JSON.stringify({name: name, price: Number(price)})
        }
        )
        const data = await res.json()
        document.querySelector('#response').innerText = "Response: " + JSON.stringify(data)
    } 
    catch(error){
        document.querySelector('#response').innerText = "Error: " + error
    }
})
async function loaditems() {
    const res = await fetch("http://127.0.0.1:5000/items")
    const data = await res.json()

    const list = document.querySelector('.itemslist')
    list.innerHTML = ""

    for(const id in data){
        const item = data[id]
        const li = document.createElement('li')
        li.innerHTML = `ID = ${id}, name = ${item.name}, price = ${item.price}
        <button onclick = "showupdatedform('${id}', '${item.name}', '${item.price}')"> Update </button>
        <button onclick = "deleteditem('${id}')"> Delete </button>
        `
        list.appendChild(li)
    }
}

function showupdatedform(id, name, price){
    document.querySelector("#updatedsection").style.display = "block"
    document.querySelector("#updateName").value = name
    document.querySelector("#updateID").value = id
    document.querySelector("#updatePrice").value = price
}
async function updateItems() {
    const id = document.querySelector("#updateID").value
    const name = document.querySelector("#updateName").value
    const price = document.querySelector("#updatePrice").value
    const res = await fetch(`http://127.0.0.1:5000/items/${id}`, {
        method: "PUT",
        headers: {"Content-type" : "application/json"},
        body: JSON.stringify({name: name, price:Number(price)})
    })
    const html = await res.text()
    document.body.innerHTML = html

}
async function deleteditem(id) {
    const res = await fetch(`http://127.0.0.1:5000/items/${id}`, {
    method: "DELETE",
    })
    const html = await res.text()
    document.body.innerHTML = html
}