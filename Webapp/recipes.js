fetch('../src/recipes_suggestions/recipes.json')
    .then(response => response.json())
    .then(data => {
        const recipeList = document.getElementById('recipe-list');

        data.forEach(recipe => {
            const row = document.createElement('tr');

            const nameCell = document.createElement('td');
            nameCell.textContent = recipe.name;
            row.appendChild(nameCell);

            const buttonCell = document.createElement('td');
            const viewButton = document.createElement('button');
            viewButton.textContent = 'See the steps';
            viewButton.onclick = () => {
                const recipeId = recipe.name;
                window.location.href = `RecipeDetail.html?recipe=${encodeURIComponent(recipeId)}`;
            };
            buttonCell.appendChild(viewButton);
            row.appendChild(buttonCell);

            recipeList.appendChild(row);
        });
    })
    .catch(error => {
        console.error("Error", error);
    });
