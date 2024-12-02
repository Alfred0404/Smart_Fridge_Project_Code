const urlParams = new URLSearchParams(window.location.search);
const recipeId = urlParams.get('recipe'); // On récupère le nom de la recette ou son ID

fetch('../src/recipes_suggestions/recipes.json')
    .then(response => response.json())
    .then(data => {
        // Trouver la recette en fonction de l'ID ou du nom
        const recipe = data.find(recipe => recipe.name === recipeId);

        if (recipe) {
            const recipeDetailContainer = document.getElementById('recipe-detail');
            recipeDetailContainer.innerHTML = `
                <h3>${recipe.name}</h3>
                <div>
                    ${recipe.steps.map((step, index) => `
                        <div class="step">
                            <p class="step-number">Étape ${index + 1}:</p>
                            <p>${step.step}</p>
                        </div>
                    `).join('')}
                </div>
            `;
        } else {
            document.getElementById('recipe-detail').innerHTML = "<p>Recipe not found</p>";
        }
    })
    .catch(error => {
        console.error("Error:", error);
    });
