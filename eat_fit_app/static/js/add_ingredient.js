

document.addEventListener("DOMContentLoaded", function () {
    const addButton = document.getElementById('add-more');
    const formSetContainer = document.getElementById('form-set');

    addButton.addEventListener('click', function () {
        let totalForms = document.querySelector("input[name='recipeingredients_set-TOTAL_FORMS']");
        if (totalForms) {
            let formNum = parseInt(totalForms.value); // Get the current number of forms
            let newForm = formSetContainer.children[0].cloneNode(true); // Clone the first form

            newForm.innerHTML = newForm.innerHTML.replace(/-0-/g, `-${formNum}-`); // Replace the form number
            formSetContainer.appendChild(newForm);

            totalForms.value = formNum + 1; // Increment the form count
        } else {
            console.error("Total forms input not found");
        }
    });
});
