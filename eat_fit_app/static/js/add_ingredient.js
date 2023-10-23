console.log("Script loaded!");

document.addEventListener("DOMContentLoaded", function () {
    const addButton = document.getElementById('add-ingredient-btn');
    if (addButton) {
        addButton.addEventListener('click', function () {
            console.log("Button clicked!");

            const index = 0; // Na razie zakładamy, że dodajesz tylko pierwszy zestaw składników
            const ingredientElement = document.querySelector(`[name='ingredients-${index}-ingredients']`);
            const quantityElement = document.querySelector(`[name='ingredients-${index}-quantity']`);
            const measureElement = document.querySelector(`[name='ingredients-${index}-measure']`);

            if (ingredientElement && quantityElement && measureElement) {
                const ingredient = ingredientElement.options[ingredientElement.selectedIndex].text;
                const quantity = quantityElement.value;
                const measure = measureElement.options[measureElement.selectedIndex].text;

                const listContainer = document.getElementById('added-ingredients-list');
                const listItem = document.createElement('li');
                listItem.textContent = `${ingredient} - ${quantity} ${measure}`;
                listContainer.appendChild(listItem);
            }
        });
    } else {
        console.log("Button element is not found!");
    }
});
