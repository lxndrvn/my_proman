from models import *
from flask import *

app = Flask(__name__)


@app.route('/')
def get_boards():
    boards = Board.select()
    return render_template('boards.html', boards=boards)


@app.route('/board', methods=['POST'])
def save_new_board():
    Board.create(title=request.form['title'])
    return redirect(url_for('get_boards'))


@app.route('/story/<board_id>', methods=['POST'])
def update_board(board_id):
    board = Board.get(Board.id == board_id)
    board.update(title=request.form['title'])
    return redirect(url_for('get_boards'))


@app.route('/delete/<board_id>', methods=['POST'])
def delete_board(board_id):
    print(board_id)
    board = Board.select().where(Board.id == board_id).get()
    print(board)
    board.delete_instance()
    return redirect(url_for('get_boards'))


@app.route('/cards')
def get_cards():
    return render_template('cards.html')


if __name__ == '__main__':
    app.run(debug=True)
