# python-day4-demo

JS Code used to mock Python console. You will need to solve exercises in Python. Do not use this code as solution code. Many places ar eintentionally different from answer solutions. Check the videos for solution code.

1. **What we Provide**:  
   - A **JavaScript code (`index.js`)** that demonstrates a particular behavior or logic.  
   - This code runs in the browser and allows you to see how the functionality works.

2. **Your Task**:  
   - Analyze and understand the behavior or functionality of the JavaScript code.  
   - Write a **Python script** that replicates the same behavior or functionality.  

3. **Goal**:  
   - The Python script you write should behave in the same way as the provided JavaScript code. For example, if the JavaScript code simulates a Rock-Paper-Scissors game, your Python code should also simulate the game with the same rules and outputs.

---

### Example for Clarity

#### JavaScript Code (Given):
```javascript
function rockPaperScissors(player1, player2) {
    const rules = {
        rock: "scissors",
        scissors: "paper",
        paper: "rock"
    };

    if (player1 === player2) {
        return "It's a tie!";
    } else if (rules[player1] === player2) {
        return "Player 1 wins!";
    } else {
        return "Player 2 wins!";
    }
}

console.log(rockPaperScissors("rock", "scissors")); // Output: Player 1 wins!
console.log(rockPaperScissors("paper", "rock"));    // Output: Player 1 wins!
console.log(rockPaperScissors("scissors", "rock")); // Output: Player 2 wins!
```

---

#### Your Python Code (To Write):
```python
def rock_paper_scissors(player1, player2):
    rules = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }

    if player1 == player2:
        return "It's a tie!"
    elif rules[player1] == player2:
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

# Test cases
print(rock_paper_scissors("rock", "scissors"))  # Output: Player 1 wins!
print(rock_paper_scissors("paper", "rock"))     # Output: Player 1 wins!
print(rock_paper_scissors("scissors", "rock"))  # Output: Player 2 wins!
```

---

### Steps to Solve the Challenge

1. **Understand the JavaScript Code**:
   - Read the code carefully to understand what it does.
   - Look for inputs, outputs, and the logic used (e.g., conditions, loops, etc.).

2. **Write the Python Equivalent**:
   - Translate the logic into Python syntax.
   - Replace JavaScript-specific constructs with Python equivalents (e.g., `console.log` → `print`, objects → dictionaries).

3. **Test the Python Code**:
   - Use the same input examples from the JavaScript code to test your Python solution.
   - Ensure the outputs match.

4. **Refine and Debug**:
   - If the behavior isn’t identical, debug your Python code until it matches the JavaScript logic.

---
