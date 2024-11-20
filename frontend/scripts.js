async function loadTables() {
    const response = await fetch('<API_GATEWAY_URL>/tables');
    const tables = await response.json();
    const tableList = document.getElementById('tables');
    tableList.innerHTML = '';
    tables.forEach(table => {
        const li = document.createElement('li');
        li.textContent = `Table ID: ${table.table_id}, Booked By: ${table.user || 'Available'}`;
        tableList.appendChild(li);
    });
}

document.getElementById('booking-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const table_id = document.getElementById('table_id').value;
    const game_system = document.getElementById('game_system').value;
    const user = document.getElementById('user').value;

    await fetch('<API_GATEWAY_URL>/book', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ table_id, game_system, user })
    });

    alert('Table booked successfully!');
    loadTables();
});

loadTables();

