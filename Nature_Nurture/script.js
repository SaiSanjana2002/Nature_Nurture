const crops = [
    { name: "Rubber", image: "rubber.png", price: 150 },
    { name: "Maize", image: "maize.png", price: 30 },
    { name: "Arecanut", image: "arecanut.png", price: 200 },
    { name: "Coffee", image: "coffee.png", price: 250 },
    { name: "Paddy", image: "paddy.png", price: 25 }
];

const cropList = document.getElementById("crop-list");

crops.forEach(crop => {
    const cropItem = document.createElement("div");
    cropItem.className = "crop-item";

    const image = document.createElement("img");
    image.src = crop.image;
    image.alt = crop.name;

    const name = document.createElement("div");
    name.textContent = crop.name;

    const price = document.createElement("div");
    price.textContent = `Price: ₹${crop.price}/kg`;

    const buyButton = document.createElement("button");
    buyButton.className = "button";
    buyButton.textContent = "Buy";
    buyButton.addEventListener("click", () => {
        alert(`You bought ${crop.name} for ₹${crop.price}/kg.`);
    });

    cropItem.appendChild(image);
    cropItem.appendChild(name);
    cropItem.appendChild(price);
    cropItem.appendChild(buyButton);

    cropList.appendChild(cropItem);
});
