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



