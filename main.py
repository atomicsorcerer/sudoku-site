from flask import Flask, render_template
from lib.utils import generate_board

app = Flask(__name__)

@app.route("/")
def index():
    sudoku_board = generate_board(print_final_result=False)[0]
    return render_template('index.html', board=sudoku_board)
