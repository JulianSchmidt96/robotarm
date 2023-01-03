# Tic-Tac-Toe Webapp

This is a webapp that allows two players to play the classic strategy game Tic-Tac-Toe. Players take turns placing a symbol (X or O) on a 3x3 game board. The first team to get three symbols in a row (horizontal, vertical, or diagonal) wins the game.

In this version of the webapp, you can play against another human or against an AI. You can make your move manually or have the AI's move made automatically.


## Requirements

- A web browser with support for HTML, CSS, and JavaScript
- Python 3.x
- PyTorch

## Setup

1. Open the repository on GitHub and click "Code" then "Download ZIP"
2. Unpack the downloaded ZIP archive
3. Install the required Python dependencies:
```bash
pip install -r requirements.txt`
```
## Running the app

1. Open the file "main.html" in a web browser by either opening the file from your local computer or by entering the URL of the file into the address bar of your web browser.
2. Play the game by clicking on one of the empty squares to make your move. You can also click the "Make AI move" button to have the AI make its move automatically. The game ends when one player wins or the game ends in a draw. You can reset the game at any time by clicking the "Reset game" button.

## Playing against the AI

To play against the AI, you will need to run the "api.py" file in parallel with the webapp. To do this, open a terminal window, navigate to the directory where you unpackaged the repository, and run the following command:

```bash
python api.py
```