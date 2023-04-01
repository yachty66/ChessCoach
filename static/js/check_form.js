document.getElementById('start-form').addEventListener('submit', async (event) => {
    console.log('Form submitted');
    event.preventDefault(); // Prevent the form from submitting by default

    const apiKey = document.getElementById('api-key').value;
    const username = document.getElementById('username').value;
    const response = await fetch('/check-api-key', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `api_key=${encodeURIComponent(apiKey)}`
    });

    const result = await response.json();

    //if (result.status === 'success') {
    //TODO use comment from above
    if ('success' === 'success') {
        // API key is valid, now fetch the games
        const gamesResponse = await fetch('/games', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: `api_key=${encodeURIComponent(apiKey)}&username=${encodeURIComponent(username)}`
        });
        console.log('gamesResponse', gamesResponse);
        //const gamesPage = await gamesResponse.text();
        //document.getElementById('content').innerHTML = gamesPage;
    } else {
        alert('API Key is invalid');
    }
});

