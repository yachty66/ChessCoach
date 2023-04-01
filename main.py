from flask import Flask, render_template, request, jsonify
from chessdotcom import get_player_games_by_month_pgn
import requests
import openai

app = Flask(__name__, template_folder=".")

@app.route('/')
def index():
    return render_template('index.html')

#check if key exists
@app.route("/check-api-key", methods=["POST"])
def check_api_key():
    api_key = request.form.get("api_key")
    openai.api_key = api_key
    try:
        openai.Engine.list()
        return {"status": "success"}
    except openai.error.AuthenticationError:
        return {"status": "failure"}
    
#on submit call function which is getting games from username, if failure return --> no games available
@app.route('/games')
def games():
    return render_template('games.html')


@app.route('/coach')
def game():
    return render_template('coach.html')

import re

@app.route('/get_games')
def get_games():
    response = get_player_games_by_month_pgn("homooecochessicus", 2023, 3)
    response_data = response.json["pgn"]["pgn"]
    #print only the first 5 games
    #print(response_data[:5000])
    #print(response_data)

    games = []
    game_pattern = re.compile(r'\[Event .+?}\s(?:\d-\d|1/2-1/2)', re.DOTALL)
    tag_pattern = re.compile(r'\[(\w+)\s"([^"]+)"\]')
    move_pattern = re.compile(r'\d+\.\s+\S+\s+(?:\S+\s+)?')

    for game_text in game_pattern.findall(response_data):
        game = {}
        for tag, value in tag_pattern.findall(game_text):
            if tag in ["UTCTime", "White", "Black", "Result"]:
                game[tag] = value
        moves = " ".join(move_pattern.findall(game_text)).strip()
        if moves:
            game["Moves"] = moves
        games.append(game)
    print(games)

    return jsonify(games)





if __name__ == '__main__':
    app.run(debug=True)
