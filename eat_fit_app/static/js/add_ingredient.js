document.addEventListener("DOMContentLoaded", function () {
    const addButton = document.querySelector('.add-ingredient-btn');
    const formSetContainer = document.getElementById('form-set');

    if (addButton) {
        addButton.addEventListener('click', function () {
            const totalForms = document.querySelector("[name='ingredients-TOTAL_FORMS']");
            const index = parseInt(totalForms.value);

            const newIngredientForm = formSetContainer.children[0].cloneNode(true);

            for (let element of newIngredientForm.querySelectorAll("[name^='ingredients-']")) {
                element.name = element.name.replace('-0-', `-${index}-`);
            }

            formSetContainer.appendChild(newIngredientForm);

            totalForms.value = index + 1;
        });
    } else {
        console.log("Button element is not found!");
    }
     document.body.addEventListener('click', function(event) {
        if (event.target.classList.contains('remove-ingredient-btn')) {
            const ingredientForm = event.target.closest('.ingredient-form');
            ingredientForm.remove();

            const totalForms = document.querySelector("[name='ingredients-TOTAL_FORMS']");
            totalForms.value = parseInt(totalForms.value) - 1;
        }
    });
});
