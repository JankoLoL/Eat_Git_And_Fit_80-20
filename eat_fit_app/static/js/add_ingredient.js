document.addEventListener("DOMContentLoaded", function () {
    const addButton = document.querySelector('.add-ingredient-btn');
    const formSetContainer = document.getElementById('form-set');

    if (addButton) {
        addButton.addEventListener('click', function () {
            const totalForms = document.querySelector("[name='ingredients-TOTAL_FORMS']");
            const index = parseInt(totalForms.value);
            const newIngredientForm = formSetContainer.children[0].cloneNode(true);

            // Update id and name for each form field in the cloned form
            for (let element of newIngredientForm.querySelectorAll("[id^='ingredients-']")) {
                const newName = element.name.replace('-0-', `-${index}-`);
                element.name = newName;
                element.id = element.id.replace('-0-', `-${index}-`);

                // Update 'for' attribute for labels
                const label = newIngredientForm.querySelector(`label[for='${element.id}']`);
                if (label) {
                    label.setAttribute('for', element.id);
                }
            }

            formSetContainer.appendChild(newIngredientForm);
            totalForms.value = index + 1;
        });
    } else {
        console.log("Add Ingredient Button not found!");
    }

    // Handle removal of ingredient forms
    document.body.addEventListener('click', function (event) {
        if (event.target.classList.contains('remove-ingredient-btn')) {
            const ingredientForm = event.target.closest('.ingredient-form');
            if (ingredientForm) {
                ingredientForm.remove();

                const totalForms = document.querySelector("[name='ingredients-TOTAL_FORMS']");
                totalForms.value = parseInt(totalForms.value) - 1;
            }
        }
    });
});
