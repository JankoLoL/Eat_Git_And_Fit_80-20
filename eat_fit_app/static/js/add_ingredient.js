// document.addEventListener("DOMContentLoaded", function () {
//     const formSetContainer = document.getElementById('form-set');
//     const addButton = document.querySelector('.add-ingredient-btn');
//     const totalForms = document.querySelector("[name='ingredients-TOTAL_FORMS']");
//
//     const updateElementAttributes = function (element, index) {
//         const idRegex = new RegExp('id_ingredients-\\d+-');
//         const nameRegex = new RegExp('ingredients-\\d+-');
//         const replacement = `ingredients-${index}-`;
//
//         if (element.id) {
//             element.id = element.id.replace(idRegex, `id_${replacement}`);
//         }
//         if (element.name) {
//             element.name = element.name.replace(nameRegex, replacement);
//         }
//         if (element.htmlFor) {
//             element.htmlFor = element.htmlFor.replace(idRegex, `id_${replacement}`);
//         }
//     };
//
//     const addIngredientForm = function () {
//         let newForm = formSetContainer.children[0].cloneNode(true);
//         let formIndex = parseInt(totalForms.value);
//         newForm.querySelectorAll('input, select, label').forEach(function (element) {
//             updateElementAttributes(element, formIndex);
//             if (element.tagName === 'INPUT' || element.tagName === 'SELECT') {
//                 element.value = '';
//                 element.setAttribute('autocomplete', 'off');
//             }
//         });
//         formSetContainer.appendChild(newForm);
//         totalForms.value = formIndex + 1;
//     };
//
//     if (addButton) {
//         addButton.addEventListener('click', addIngredientForm);
//     }
//
//     formSetContainer.addEventListener('click', function (event) {
//         if (event.target.classList.contains('remove-ingredient-btn')) {
//             const ingredientForm = event.target.closest('.ingredient-form');
//             if (ingredientForm) {
//                 ingredientForm.remove();
//                 let index = 0;
//                 formSetContainer.querySelectorAll('.ingredient-form').forEach(function (row) {
//                     row.querySelectorAll('input, select, label').forEach(function (element) {
//                         updateElementAttributes(element, index);
//                     });
//                     index++;
//                 });
//                 totalForms.value = index;
//             }
//         }
//     });
// });


// add_recipe.js
// document.addEventListener("DOMContentLoaded", function () {
//     const addButton = document.getElementById('add-more');
//     const formSetContainer = document.getElementById('form-set');
//
//     addButton.addEventListener('click', function () {
//         let totalForms = document.querySelector("#id_ingredients-TOTAL_FORMS");
//         let formNum = formSetContainer.children.length; // Get the number of current ingredient forms
//         let newForm = formSetContainer.children[0].cloneNode(true); // Clone the first form
//
//         let newFormHTML = newForm.innerHTML.replace(/-0-/g, '-' + formNum + '-'); // Replace the form number
//         newForm.innerHTML = newFormHTML;
//         formSetContainer.appendChild(newForm);
//
//         totalForms.setAttribute('value', formNum + 1); // Increment the form count
//     });
// });

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
