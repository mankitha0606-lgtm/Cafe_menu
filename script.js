fetch("http://127.0.0.1:5000/menu")
  .then(res => res.json())
  .then(data => {
    renderMenu(data.coffee, "coffeeMenu");
    renderMenu(data.snacks, "snacksMenu");
  })
  .catch(err => console.error(err));



let order = [];

function renderMenu(menu, elementId) {
  const container = document.getElementById(elementId);
  container.innerHTML = "";

  menu.forEach(item => {
    const card = document.createElement("div");
    card.className = "card";

    card.innerHTML = `
      <img src="images/${item.image}" alt="${item.name}">
      <h3>${item.name}</h3>
      <p>$${item.price}</p>
      <button onclick="addToOrder('${item.name}', ${item.price})">Add</button>
    `;

    container.appendChild(card);
  });
}





function addToOrder(name, price) {
  fetch("http://127.0.0.1:5000/add-item", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, price })
  });
}


function updateOrder() {
  fetch("http://127.0.0.1:5000/order")
    .then(res => res.json())
    .then(data => {
      const list = document.getElementById("orderList");
      const total = document.getElementById("total");

      list.innerHTML = "";
      data.items.forEach(item => {
        const li = document.createElement("li");
        li.textContent = `${item.name} - $${item.price}`;
        list.appendChild(li);
      });

      total.textContent = data.total.toFixed(2);
    })
    .catch(err => console.error(err));
}


function checkout() {
  fetch("http://127.0.0.1:5000/checkout", {
    method: "POST"
  })
  .then(res => res.json())
  .then(data => {
    alert(`Order confirmed! Total: $${data.total}`);
    updateOrder();
  })
  .catch(err => console.error(err));
}


function clearOrder() {
  order = [];
  updateOrder();
}

renderMenu(coffeeMenu, "coffeeMenu");
renderMenu(snacksMenu, "snacksMenu");
      
