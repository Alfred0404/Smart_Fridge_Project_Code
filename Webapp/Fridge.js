document.addEventListener('DOMContentLoaded', () => {
    const fridgeContentsDiv = document.getElementById('fridge-contents');
    const prevPageButton = document.getElementById('prev-page');
    const nextPageButton = document.getElementById('next-page');

    const jsonFilePath = '../src/vision/utils/items_in_fridge.json';
    const ITEMS_PER_TABLE = 10;

    let fridgeData = [];
    let currentPage = 1;

    fetch(jsonFilePath)
        .then((response) => {
            if (!response.ok) {
                throw new Error(`Error: ${response.statusText}`);
            }
            return response.json();
        })
        .then((data) => {
            fridgeData = Object.entries(data).map(([name, quantity]) => ({ name, quantity }));
            updateTable();
        })
        .catch((error) => {
            console.error('Error:', error);
            fridgeContentsDiv.innerHTML = '<p>Impossible de charger les données du frigo.</p>';
        });

    // Mettre à jour l'affichage du tableau
    function updateTable() {
        fridgeContentsDiv.innerHTML = '';

        const startIndex = (currentPage - 1) * ITEMS_PER_TABLE;
        const endIndex = startIndex + ITEMS_PER_TABLE;
        const itemsToShow = fridgeData.slice(startIndex, endIndex);

        const table = document.createElement('table');
        table.className = 'ingredients-table';

        const thead = document.createElement('thead');
        thead.innerHTML = `
            <tr>
                <th>ID</th>
                <th>Quantity</th>
            </tr>
        `;
        table.appendChild(thead);

        const tbody = document.createElement('tbody');
        itemsToShow.forEach(item => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${item.name}</td>
                <td>${item.quantity}</td>
            `;
            tbody.appendChild(row);
        });
        table.appendChild(tbody);

        fridgeContentsDiv.appendChild(table);

        updatePaginationControls();
    }

    function updatePaginationControls() {
        const totalPages = Math.ceil(fridgeData.length / ITEMS_PER_TABLE);

        prevPageButton.disabled = currentPage === 1;
        nextPageButton.disabled = currentPage === totalPages;
    }

    prevPageButton.addEventListener('click', () => {
        if (currentPage > 1) {
            currentPage--;
            updateTable();
        }
    });

    nextPageButton.addEventListener('click', () => {
        if (currentPage < Math.ceil(fridgeData.length / ITEMS_PER_TABLE)) {
            currentPage++;
            updateTable();
        }
    });
});
