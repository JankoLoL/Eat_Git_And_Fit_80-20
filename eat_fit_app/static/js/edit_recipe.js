document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('add-ingredient-btn').addEventListener('click', addIngredient);
    document.getElementById('ingredients-container').addEventListener('click', removeIngredient);

    function addIngredient(e) {
        e.preventDefault();
        let formContainer = document.getElementById('ingredients-container');
        let totalForms = document.getElementById('id_recipeingredients_set-TOTAL_FORMS');
        let formNum = formContainer.getElementsByClassName('ingredient-form').length;
        let newForm = document.querySelector('#ingredient-form-template').content.cloneNode(true).firstElementChild;

        // Update new form attributes
        newForm.innerHTML = newForm.innerHTML.replace(/__prefix__/g, formNum);
        totalForms.setAttribute('value', parseInt(totalForms.getAttribute('value')) + 1);

        formContainer.appendChild(newForm);
    }

    function removeIngredient(e) {
        if (e.target.classList.contains('remove-ingredient-btn')) {
            e.preventDefault();
            let form = e.target.closest('.ingredient-form');
            let totalForms = document.getElementById('id_recipeingredients_set-TOTAL_FORMS');
            let formNum = document.querySelectorAll('.ingredient-form').length - 1; // Decrement before removing the form
            form.remove();
            totalForms.setAttribute('value', formNum);
        }
    }
});
