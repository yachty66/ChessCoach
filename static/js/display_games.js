// display_games.js

console.log('display_games.js loaded 3');

function parsePgnData(pgnData) {
    const games = pgnData.split('\n\n\n').filter(game => game.trim() !== '');
    const opponents = games.map(game => {
        const lines = game.split('\n');
        const whiteLine = lines.find(line => line.startsWith('[White '));
        const blackLine = lines.find(line => line.startsWith('[Black '));
        const whitePlayer = whiteLine.split('"')[1];
        const blackPlayer = blackLine.split('"')[1];
        return whitePlayer === '{{username}}' ? blackPlayer : whitePlayer;
    });
    return opponents;
}

function createGameButton(opponent, index) {
    const button = document.createElement('button');
    button.textContent = opponent;
    button.classList.add('game-button');
    button.setAttribute('data-index', index);
    return button;
}

function displayGames(opponents) {
    opponents.forEach((opponent, index) => {
        const button = createGameButton(opponent, index);
        gamesContainer.appendChild(button);
    });
}
console.log('display_games.js loaded');
const opponents = parsePgnData(pgnData);
console.log(opponents);
displayGames(opponents);
