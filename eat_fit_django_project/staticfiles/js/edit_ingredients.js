document.addEventListener("DOMContentLoaded", function () {
    const addButton = document.getElementById('add-more');
    const formSetContainer = document.getElementById('form-set');

    addButton.addEventListener('click', function () {
        let totalForms = document.querySelector("input[name='recipeingredients_set-TOTAL_FORMS']");
        let formNum = parseInt(totalForms.value);

        let firstIngredientForm = formSetContainer.querySelector('.ingredient-form');
        if (!firstIngredientForm) {
            return;
        }
        let newForm = firstIngredientForm.cloneNode(true);
        newForm.innerHTML = newForm.innerHTML.replace(/-\d-/g, `-${formNum}-`);
        formSetContainer.appendChild(newForm);
        totalForms.value = formNum + 1;
    });


    formSetContainer.addEventListener('click', function (e) {
        if (e.target && e.target.classList.contains('remove-ingredient')) {
            e.preventDefault();
            e.target.closest('.ingredient-form').remove();
            let totalForms = document.querySelector("input[name='recipeingredients_set-TOTAL_FORMS']");
            totalForms.value = parseInt(totalForms.value) - 1;
        }
    });
});