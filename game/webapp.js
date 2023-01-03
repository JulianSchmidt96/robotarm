const squares = document.querySelectorAll(".square");
const resetButton = document.querySelector("#reset-button");
const aiButton = document.querySelector("#ai-button");
const message = document.querySelector("#message");



let currentPlayer = "X";

function checkWin() {
  // Check rows
  for (let i = 0; i < 3; i++) {
    if (
      squares[i * 3].textContent === currentPlayer &&
      squares[i * 3 + 1].textContent === currentPlayer &&
      squares[i * 3 + 2].textContent === currentPlayer
    ) {
      return true;
    }
  }

  // Check columns
  for (let i = 0; i < 3; i++) {
    if (
      squares[i].textContent === currentPlayer &&
      squares[i + 3].textContent === currentPlayer &&
      squares[i + 6].textContent === currentPlayer
    ) {
      resetGame()
      return true;
    }
  }

  // Check diagonals
  if (
    squares[0].textContent === currentPlayer &&
    squares[4].textContent === currentPlayer &&
    squares[8].textContent === currentPlayer
  ) {
    resetGame()
    return true;
  }
  if (
    squares[2].textContent === currentPlayer &&
    squares[4].textContent === currentPlayer &&
    squares[6].textContent === currentPlayer
    
  ) {
    resetGame()
    return true;
  }

  return false;
}

function checkDraw() {
  for (let i = 0; i < 9; i++) {
    if (squares[i].textContent === "") {
      return false;
    }
  }
  return true;
}

function switchPlayer() {
  if (currentPlayer === "X") {
    currentPlayer = "O";
  } else {
    currentPlayer = "X";
  }
}

function setSquare(x, y, symbol) {
  const index = x * 3 + y;
  if (squares[index].textContent === "") {
    squares[index].textContent = symbol;
    return true;
  }
  return false;
}

async function makeAIMove(board, player) {
  // Check if the game is over
  if (checkWin()) {
    return;
  }

  // Convert the board to a numeric representation
  const numericBoard = convertBoardToNumeric(board);

  // Add the board and player as query parameters
  const queryParams = { board: numericBoard, player };
  const searchParams = new URLSearchParams(queryParams);
  const apiUrl = `http://localhost:5000/api?${searchParams.toString()}`;

  // Make a GET request to the API to get the AI's prediction
  const response = await fetch(apiUrl);
  let data = await response.json();
  let prediction = data.prediction;

  // Print the prediction
  console.log(prediction);

  // Set the symbol on the game board
  let success = setSquare(prediction[0], prediction[1], currentPlayer);

  // If the move was successful, switch to the other player
  if (success) {
    switchPlayer();
  }

  // Check if the game is over
  checkWin();
}



function handleAiMove(prediction) {
  // Get the row and column of the predicted move
  const row = prediction[0];
  const col = prediction[1];

  // Get the square at the predicted position
  const square = squares[row * 3 + col];

  // Place the move on the board if the square is empty
  if (square.textContent === "") {
    square.textContent = currentPlayer;
  }

  // Check if the game has been won
  if (checkWin()) {
    // Display a win message
    message.textContent = `${currentPlayer} wins!`;
  } else if (checkDraw()) {
    // Display a draw message
    message.textContent = "It's a draw!";
  } else {
    // Switch to the other player
    currentPlayer = currentPlayer === "X" ? "O" : "X";
  }
}



function resetGame() {
  for (let i = 0; i < 9; i++) {
    squares[i].textContent = "";
  }
  currentPlayer = "X";
}

function updateMessage(message) {
  let messageElement = document.getElementById("message");
  messageElement.innerText = message;
}

function convertBoardToNumeric(board) {
  return board.map((symbol) => {
    if (symbol === "X") {
      return 1;
    } else if (symbol === "O") {
      return 2;
    } else {
      return 0;
    }
  }).join(",");
}


function convertPredictionToSymbol(prediction) {
  if (prediction === 1) {
    return "X";
  } else if (prediction === 2) {
    return "O";
  } else {
    return "";
  }
}

function convertBoardToString(board) {
  let boardString = "";
  for (let i = 0; i < board.length; i++) {
    if (board[i] === 1) {
      boardString += "X";
    } else if (board[i] === 2) {
      boardString += "O";
    } else {
      boardString += "";
    }
  }
  return boardString;
}





resetButton.addEventListener("click", function () {
  resetGame();
  updateMessage("X's turn");
});

aiButton.addEventListener("click", function () {
  const board = [...squares].map((square) => square.textContent);
  const player = currentPlayer;
  makeAIMove(board, player);
});

for (let i = 0; i < 9; i++) {
  squares[i].addEventListener("click", function () {
    if (setSquare(Math.floor(i / 3), i % 3, currentPlayer)) {
      if (checkWin()) {
        updateMessage(`${currentPlayer} wins!`);
        resetGame();
      } else if (checkDraw()) {
        updateMessage("Draw!");
        resetGame();
      } else {
        switchPlayer();
        updateMessage(`${currentPlayer}'s turn`);
      }
    }
  });
}

