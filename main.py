from flask import Flask, render_template, request, jsonify
from chessdotcom import get_player_games_by_month_pgn
import requests
import openai
from flask import send_from_directory


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
    print(response_data)

    games = []
    game_pattern = re.compile(r'\[Event .+?}\s(?:\d-\d|1/2-1/2)', re.DOTALL)
    tag_pattern = re.compile(r'\[(\w+)\s"([^"]+)"\]')
    move_pattern = re.compile(r'\d+\.\s+\S+(?:\s+\S+)?')

    for game_text in game_pattern.findall(response_data):
        if game_text:
            game = {}
            for tag, value in tag_pattern.findall(game_text):
                if tag in ["UTCTime", "White", "Black", "Result"]:
                    game[tag] = value
            moves = move_pattern.findall(game_text)

            if moves:
                moves_dict = {}
                for move in moves:
                    move_num, white_move, black_move = re.match(r'(\d+)\.\s+(\S+)(?:\s+(\S+))?', move.strip()).groups()
                    moves_dict[f"{move_num}."] = f"{white_move} {black_move}" if black_move and not black_move.startswith('{') else white_move
                game["Moves"] = moves_dict

            games.append(game)
    return jsonify(games)

#here i want to create the message which i am sending to the chat api 
def game_state_to_pgn(moves):
    pgn = ""
    for move_key in sorted(moves.keys(), key=lambda x: int(x[:-1])):
        pgn += f"{move_key} {moves[move_key]} "
    return pgn.strip()

@app.route('/analyze_move', methods=['POST'])
def analyze_move():
    print("should appear")
    openai.api_key =
    move_data = request.get_json()
    move = move_data['move']
    game_state = move_data['game_state']

    pgn = game_state_to_pgn(game_state)

    messages = [
        {
            "role": "system",
            "content": "You are chesscoach in chess grandmaster level."
        },
        {
            "role": "user",
            "content": f"Given the given state of a chess game {pgn}. Give an annotation based on the move {move}."
        }
    ]
    print(messages)
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    analysis = completion.choices[0].message["content"].strip()

    response = f"Your move was {move}. Following my annotation for you: {analysis}"
    
    return jsonify({"analysis": response})

if __name__ == '__main__':
    app.run(debug=True)
