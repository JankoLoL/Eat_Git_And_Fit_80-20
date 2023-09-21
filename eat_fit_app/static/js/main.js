// document.addEventListener("DOMContentLoaded", function (){
//
//     const ingredientsContainer = document.getElementById('ingredients-container');
//     const addIngredientBtn = document.getElementById('add-ingredient-btn');
//
//     function updateIngredientFormset(){
//         const totalForms = ingredientsContainer.querySelectorAll('.ingredient-form').length;
//         const managementForm = document.querySelector('input[name="ingredients-TOTAL_FORMS"]');
//         managementForm.value = totalForms;
//     }
//     addIngredientBtn.addEventListener('click', function() {
//         // Pobierz pierwszy formularz składnika jako wzór
//         const sampleForm = ingredientsContainer.querySelector('.ingredient-form').cloneNode(true);
//
//         // Zaktualizuj indeks formularza w jego atrybutach name
//         const newFormIndex = ingredientsContainer.querySelectorAll('.ingredient-form').length;
//         sampleForm.innerHTML = sampleForm.innerHTML.replace(/__prefix__/g, newFormIndex);
//
//         // Dodaj nowy formularz składnika do kontenera
//         ingredientsContainer.appendChild(sampleForm);
//
//         updateIngredientFormset();
//     });
// });

document.addEventListener("DOMContentLoaded", function () {
    let formIdx = parseInt(document.getElementById('ingredients-container').getAttribute('data-formset-count'), 10);

    document.getElementById('add-ingredient-btn').addEventListener('click', function() {
        let container = document.getElementById('ingredients-container');
        let newElement = document.getElementById('empty-form').innerHTML.replace(/__prefix__/g, formIdx);

        container.insertAdjacentHTML('beforeend', newElement);

        let totalForms = document.getElementById('id_ingredients-TOTAL_FORMS');
        totalForms.value = formIdx + 1;

        formIdx++;
    });
});
