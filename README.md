# 🎲 Dice Battle: Human vs. Computer

A modular, object-oriented Python implementation of a classic dice game. This project demonstrates clean code principles by separating game logic, player management, and hardware simulation (the Die) into distinct modules.

---

## 📝 Game Rules
- Both the **Player** and the **Computer** start with a counter of **5**.
- Each round, both parties roll a 6-sided die.
- **If you win the roll:** Your counter decreases by 1, and the computer's increases by 1.
- **If you lose the roll:** Your counter increases by 1, and the computer's decreases by 1.
- **The Goal:** Be the first to reach a counter of **0** to win the game!

---

## 📂 Project Structure
```text
dice_game/
├── src/
│   ├── __init__.py    # Makes src a Python package
│   ├── die.py         # Die class (logic for rolling)
│   ├── player.py      # Player class (stores score and state)
│   └── game.py        # DiceGame class (manages game flow)
├── main.py            # The main entry point to run the game
├── requirements.txt   # Project dependencies
└── README.md          # Project documentation


🚀 Getting Started
1. Prerequisites
Ensure you have Python 3.8+ installed on your system.

2. Installation
Clone this repository or download the source code, then navigate to the project folder and install the required dependencies:

Bash

# Install the required Numpy library
pip install -r requirements.txt
3. Running the Game
To start the game, simply run the main.py file from your terminal:

Bash

python main.py
🛠️ Built With
Python - Core programming language.

NumPy - Used for high-quality random number generation.

OOP (Object-Oriented Programming) - Designed with modular classes for scalability.

🤝 Contributing
Feel free to fork this project and submit pull requests. You can add features like:

Support for multiple players.

Different types of dice (D12, D20).

A graphical user interface (GUI).

📄 License
This project is open-source and available under the MIT License.


### Quick Checklist before you paste:
1.  **File Naming:** Ensure the file is named exactly `README.md`.
2.  **numpy:** Make sure you have `numpy` listed in your `requirements.txt` as we discussed earlier.
3.  **Folder structure:** Ensure your `.py` files are inside a folder named `src` for the "Project Structure" section above to be accurate.



**Would you like me to help you write the code for the `main.py` file to make sure it imports the classes from the `src` folder correctly?**