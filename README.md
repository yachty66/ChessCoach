# ChessCoach

## Workflow

- Goes on page
- Pasting key and chess.com link
- list of games is displayed
- clicks on game
- first annotation is displayed 
    - in backend game is analyzed and best move is suggested which is added to the prompt
- clicks on next button and next annotation is displayed
- no moves left = End displayed

## Goal 

People can really use this application for getting game annotations

## Notes

- [x] create sketches for the workflow 
    - [x] start site
    - [x] displaying games side
    - [x] after clicking game side 
    - [x] end of game side 
- [x] add select button with different models 
- [x] on click of submit check if key is correct otherise return wrong key
- [ ] in testfile, try to get all games from my username 
- [ ] on click of submit check if username with game exists otherwise return no games found
- [ ] if submit was success display all games of user  
- [ ] setup a deployment pipeline to gcp for testing in realtime 

Do i need a choose model button? yes.

Building everything in python. i make more progress if i have execution blogs.

This time I really should be clear about the techstack of the project before i am starting. Need to learn how to handle sessions in the backend.

- React.js --> frontend. 
- 