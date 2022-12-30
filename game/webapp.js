// Array to store the state of the game board
// 0 means unoccupied, 1 means X, 2 means O
let board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]];


// Get the reset button
let resetButton = document.getElementById("reset-button");

// Add a click event listener to the reset button
resetButton.addEventListener("click", function() {
// Call the reset game function
resetGame();
});
    
// Function to set a symbol on the game board
function setSquare(x, y, player) {
  // Check if the square is already occupied
  if (board[x][y] !== 0) {
    return false;
  }

  // Set the symbol on the game board
  board[x][y] = player;

  // Set the symbol on the HTML element
  let square = document.getElementById(`square-${x}-${y}`);
  square.innerHTML = (player === 1) ? "X" : "O";

  return true;
}

// Current player (1 for X, 2 for O)
let currentPlayer = 1;

// Function to switch to the other player
function switchPlayer() {
  currentPlayer = (currentPlayer === 1) ? 2 : 1;
}

// Function to display a message to the user
function showMessage(message) {
  let messageElement = document.getElementById("message");
  messageElement.innerHTML = message;
}

// Function to check for a win condition
function checkWin() {
    // Check rows
    for (let i = 0; i < 3; i++) {
      if (board[i][0] === board[i][1] && board[i][1] === board[i][2] && board[i][0] !== 0) {
        let playerName = (board[i][0] === 1) ? "X" : "O";
        showMessage(`Player ${playerName} wins!`);
        return true;
      }
    }
  
    // Check columns
    for (let i = 0; i < 3; i++) {
      if (board[0][i] === board[1][i] && board[1][i] === board[2][i] && board[0][i] !== 0) {
        let playerName = (board[0][i] === 1) ? "X" : "O";
        showMessage(`Player ${playerName} wins!`);
        return true;
      }
    }
  
    // Check diagonals
    if (board[0][0] === board[1][1] && board[1][1] === board[2][2] && board[0][0] !== 0) {
      let playerName = (board[0][0] === 1) ? "X" : "O";
      showMessage(`Player ${playerName} wins!`);
      return true;
    }
    if (board[0][2] === board[1][1] && board[1][1] === board[2][0] && board[0][2] !== 0) {
      let playerName = (board[0][2] === 1) ? "X" : "O";
      showMessage(`Player ${playerName} wins!`);
      return true;
    }
  
    return false;
  }
  
  
  

// Function to reset the game
function resetGame() {
  // Reset game board
  board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]];

  // Reset HTML elements
  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
      let square = document.getElementById(`square-${i}-${j}`);
      square.innerHTML = "";
    }
  }

  // Reset current player
  currentPlayer = 1;

  // Clear message
  showMessage("");
}

// Add click event listeners to each square to set a symbol when

  
  // Add click event listeners to each square to set a symbol when clicked
for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
      let square = document.getElementById(`square-${i}-${j}`);
      square.addEventListener("click", function() {
        // Set the current player's symbol on the square
        let success = setSquare(i, j, currentPlayer);
  
        // If the move was successful (i.e., the square was not already occupied)
        if (success) {
          // Check for a win condition
          if (checkWin()) {
            // Display win message
            let playerName = (currentPlayer === 1) ? "X" : "O";
            showMessage(`Player ${playerName} wins!`);
  
            // Reset the game
            
          } else {
            // Switch to the other player
            switchPlayer();
          }
        }
      });
    }
  }
  
  square.addEventListener("click", function() {
    // Set the current player's symbol on the square
    let success = setSquare(i, j, currentPlayer);
  
    // If the move was successful (i.e., the square was not already occupied)
    if (success) {
      // Check for a win condition
      if (checkWin()) {
        // Reset the game
        resetGame();
      } else {
        // Switch to the other player
        switchPlayer();
      }
    }
  });

