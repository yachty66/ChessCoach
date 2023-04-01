from chessdotcom import get_player_games_by_month_pgn



response = get_player_games_by_month_pgn("homooecochessicus", 2023, 3)
response_data = response.json
games = response_data.get('games', [])
print(games)

