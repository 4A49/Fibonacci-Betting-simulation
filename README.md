# Fibonacci Betting Simulator

This is a simple Python script that simulates a betting strategy based on the Fibonacci sequence. The player starts with a total of 100 dollars and wagers 10 dollars on each bet. If the player loses a bet, the wager amount increases by adding the two previous wagers in the sequence. If the player wins a bet, the wager amount is reset to 10 dollars.

The code also takes into account a tax percentage that is applied to any winnings, and logs the outcome of each bet in a pandas DataFrame. Finally, the code plots the outcome of each bet as a line chart.

## Installation

To use this script, you will need to have Python 3.x installed on your machine. You can download the latest version of Python [here](https://www.python.org/downloads/).

You will also need to install the following libraries:

- pandas
- matplotlib

You can install these libraries by running the following command in your terminal:
```pip install pandas matplotlib```



## Usage

To use this script, simply run the `fibonacci_betting_simulator.py` file in your Python environment. The script will prompt you for input as it runs, asking you to enter the odds for each bet and the outcome of each bet (win or loss).

The script will output the results of each bet as it runs, and will continue running until you have no money left.

The script will also generate a pandas DataFrame that logs the outcome of each bet, and will generate a line chart that shows the results of each bet.

## License

This script is released under the [MIT License](https://github.com/<username>/<repository>/blob/main/LICENSE). Feel free to use, modify, and distribute it as you see fit.
