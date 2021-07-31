function addNewItem(item) {
    const newItem = document.createElement("tr");
    newItem.setAttribute("id", item.id);
    newItem.innerHTML = `
        <td class ="name" scope='row'>${item.name}</td>
        <td class ="quantity" scope='row'>${item.quantity}</td>
        <td class ="price" scope='row'>${item.price}</td>
        <td scope='row'><button class = "remove-button">REMOVE</button></td>
    `;
    document.querySelector("#cart table tbody").append(newItem);

    let removeButton = newItem.querySelector("button");
    removeButton.addEventListener('click', () => {
        let index = itemList.indexOf(item);
        itemList.splice(index, 1);
        removeButton.parentElement.parentElement.remove();
        updateTotalPrice();
    }, false);
    updateTotalPrice();
};

function updateItem(item) {
    const currentItem = document.getElementById(item.id);
    currentItem.querySelector(".quantity").innerText = item.quantity.toString();
    currentItem.querySelector(".price").innerText = (item.price).toString();
    updateTotalPrice();
}

function updateTotalPrice(item) {
    let price = 0;
    for (let i = 0; i < itemList.length; i++) {
        price += itemList[i].price;
    }
    document.getElementById("price").innerHTML = `
        TOTAL PRICE: <span>$${price}</span>
    `;
    if (itemList.length == 0) {
        document.getElementById("cart").hidden = true;
    }
}

const buttonList = document.querySelectorAll('.cart-button');
var itemList = [];

buttonList.forEach((button) => {
    button.addEventListener('click', () => {
        document.getElementById("cart").hidden = false;
        
        let itemId = parseInt(button.getAttribute("id"));
        let itemPrice = parseFloat(button.parentElement.querySelector("span").innerText.substring(1));
        let itemName = button.parentElement.parentElement.querySelector("h3").innerText;
        let item = itemList.find(x => x.id === itemId);

        if (item == undefined) {
            itemList.push({"id": itemId, "name": itemName, "quantity": 1, "price": itemPrice});
            item = itemList[itemList.length - 1];
            addNewItem(item);
        } else {
            let price_per_item = item.price / item.quantity;
            item.quantity += 1;
            item.price = price_per_item * item.quantity;
            updateItem(item);
        }
    });
});

