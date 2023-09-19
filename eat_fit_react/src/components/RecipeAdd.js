import React, { useState } from 'react';

function RecipeAdd() {
    const [ingredients, setIngredients] = useState([]);

    const handleAddIngredient = () => {
        setIngredients([...ingredients, { name: '', measure: '', quantity: '' }]);
    };

    const handleInputChange = (index, event) => {
        const newIngredients = [...ingredients];
        newIngredients[index][event.target.name] = event.target.value;
        setIngredients(newIngredients);
    };

    const handleSubmit = async () => {
        const recipeData = {
            // Tutaj Twoje pozostałe dane dotyczące przepisu
            ingredients: ingredients
        };

        try {
            let response = await fetch('/api/recipe/create/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(recipeData)
            });
            // Obsługa odpowiedzi...
        } catch (error) {
            // Obsługa błędów...
        }
    };

    return (
        <div>
            {/* ... Twoje inne pola formularza ... */}
            {ingredients.map((ingredient, index) => (
                <div key={index}>
                    <input name="name" value={ingredient.name} onChange={e => handleInputChange(index, e)} placeholder="Składnik" />
                    <input name="measure" value={ingredient.measure} onChange={e => handleInputChange(index, e)} placeholder="Miara" />
                    <input name="quantity" value={ingredient.quantity} onChange={e => handleInputChange(index, e)} placeholder="Ilość" />
                </div>
            ))}
            <button onClick={handleAddIngredient}>Dodaj składnik</button>
            <button onClick={handleSubmit}>Dodaj przepis</button>
        </div>
    );
}

export default RecipeAdd;
