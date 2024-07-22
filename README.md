# Introduction

Welcome to the Wordle Solver! This Python application helps you solve Wordle puzzles by providing you with the best possible guesses based on the feedback from your previous attempts.

## Features

- Provides the best possible word guesses based on feedback.
- Handles different word lengths (default is 5 letters).
- Interactive mode for step-by-step guidance.
- Batch mode for solving multiple puzzles at once.
## Description

### Python Wordle Solver

The Wordle Solver operates through a sequence of logical steps to efficiently solve Wordle puzzles:

1. **Initialization**:
   - The system initializes with a set of predefined five-letter words.
   - It selects a target word either randomly or based on user input.
   - The solver also initializes with a comprehensive list of potential words.

2. **First Guess**:
   - The solver begins by making an initial guess from a strategically chosen starting word.

3. **Feedback and Analysis**:
   - After the first guess, the system receives feedback indicating which letters are correct and in the correct position, which letters are correct but in the wrong position, and which letters are incorrect.
   - This feedback is crucial for the solver to narrow down the list of potential words.

4. **Refinement**:
   - Based on the feedback, the solver refines its list of possible words by:
     - Eliminating words that do not have the correct letters in the specified positions.
     - Removing words that do not contain the correct letters in different positions.
     - Discarding words that contain any incorrect letters.

5. **Subsequent Guesses**:
   - The solver makes a new guess from the refined list of potential words.
   - This process of guessing, receiving feedback, and refining the list continues iteratively.

6. **Winning or Exhausting Attempts**:
   - If a correct word is guessed within the allowed number of attempts, the system declares a win.
   - If the allowed attempts are exhausted without guessing the correct word, the system indicates a loss.

7. **Completion**:
   - The target word is revealed to conclude the game session, whether the solver wins or loses.

### User Interface

1. **Initialization**:
   - The system initializes with a comprehensive list of five-letter words and sets up the GUI components.

2. **UI Setup**:
   - The main window of the application is configured with buttons and text fields corresponding to each guess and feedback score.
   - A set of buttons is designated for each letter in a guess, allowing the user to enter feedback scores.

3. **First Guess**:
   - The system begins by displaying an initial guess in the first text field.

4. **User Interaction**:
   - Users interact with the application by clicking on buttons to provide feedback for each letter in the guess (correct position, correct letter but wrong position, or incorrect letter).
   - A radio button is enabled for users to submit their feedback once they are done.

5. **Feedback Processing**:
   - Upon receiving the feedback, the system processes the input and refines the list of possible words.
   - The next guess is then displayed in the subsequent text field based on the refined list.

6. **Iteration**:
   - This process continues iteratively, with users providing feedback for each guess and the system refining the potential word list and generating new guesses.

7. **Completion**:
   - The cycle repeats until the correct word is guessed or the guesses are exhausted.
   - The final guess or result is displayed in the designated text field.


## Installation

- Install Python3
    - *Windows*
    Go to the link mentioned below and follow the steps mentioned

    [ https://phoenixnap.com/kb/how-to-install-python-3-windows ]
    - *Linux*
    Open terminal if not already and type the following commands
    ```bash
    sudo apt-get install python3
    sudo apt install python3-pip
    ```

- Install dependencies for user interface

```bash
pip3 install PyQt5==5.15.9
```

- Clone the Repository
   ```sh
   git clone https://github.com/Abiggj/WordleSolver.git
   cd WordleSolver
   ```
## Usage/Examples

### Files
- *wordle.py* : Contains the logic for the Wordle game and feedback processing.
- *solver.py* : Contains the logic for the Wordle Solver that processes feedback and refines guesses.
- *Wordle.py* : Contains the PyQt5 code for the GUI-based Wordle Solver application.

### Command Line Solver

```sh
python3 solver.py
```

This will start the command-line version of the Wordle Solver. The initial guess will be displayed, and the solver will iteratively guess until it finds the correct word or exhausts all attempts.

### Solver GUI
```sh
python3 Wordle.py
```

This will launch the GUI version of the Wordle Solver. The application will display an initial guess, and you can interact by providing feedback for each letter using the provided buttons.

### Sample

![Demo Usage of WordleSolver GUI](https://github.com/Abiggj/WordleSolver/demo.png)

## FAQ

1. **What is Wordle Solver?**
    
    Wordle Solver is a Python-based application designed to solve Wordle puzzles. It includes both a command-line solver and a graphical user interface (GUI) built with PyQt5.

2. **How do I install Wordle Solver?**

    Clone the repository, navigate to the project directory, and install the dependencies using the steps mentioned above. Detailed installation instructions are provided in the Installation section of the README.

3. **What are the system requirements for Wordle Solver?**

    You need Python 3.8 or higher and PyQt5 installed. The exact package versions are listed in the installation steps abov.

4. **How do I run the command-line solver?**

    Simply run `python3 solver.py` from your terminal within the project directory. The solver will start making guesses and provide feedback iteratively.

5. **How do I run the GUI-based solver?**

    Execute `python3 Wordle.py` from your terminal within the project directory. This will launch the GUI, allowing you to interact with the solver using buttons and text fields.

6. **Can I customize the list of words used by the solver?**

    Yes, you can customize the list of words by editing the `words.txt` file. Ensure each word is on a new line and contains exactly five letters.

7. **What if the solver runs out of attempts without guessing the correct word?**
    
    The command-line solver will print "NO!!" if it exhausts all attempts without finding the correct word. The GUI solver will display the final guess in the designated text field.

8. **How can I contribute to the project?**

    Contributions are welcome! You can submit pull requests, report issues, or suggest features. Please refer to the Contributing section in the README for more details.
