from flask import Flask, request, redirect, url_for, render_template
from todo_app.data.trello_items import  TrelloManager
from todo_app.trello_config import TrelloStaticDataConfig

app = Flask(__name__)
trello_manager = TrelloManager()  # Create a single TrelloManager instance

@app.route('/')
def index():
    items = trello_manager.get_items()
    return render_template('index.html', items=items)

@app.route('/additem', methods=['POST'])
def additem():
    title = request.form.get('title')
    desc = request.form.get('description')
    trello_manager.create_card(title, desc)
    # add_item(title, description)
    return redirect(url_for('index'))

@app.route('/mark_complete/<card_id>', methods=['POST'])
def mark_card_done(card_id):
    try:
        list_id_done = TrelloStaticDataConfig.TRELLO_DONE  # Replace with the desired list ID for "Done"
        trello_manager.update_item_status(card_id, list_id_done)
        return redirect(url_for('index'))
    except Exception as e:
        return f"Failed to mark card complete {str(e)}"

@app.route('/mark_progress/<card_id>', methods=['POST'])
def mark_card_progress(card_id):
    try:
        list_id_progress = TrelloStaticDataConfig.TRELLO_IN_PROGRESS  # Replace with the desired list ID for "Progress"
        trello_manager.update_item_status(card_id, list_id_progress)
        return redirect(url_for('index'))
    except Exception as e:
        return f"Failed to progress card status: {str(e)}"

@app.route('/removeitem/<card_id>', methods=['POST'])
def removeitem(card_id):
    try:
        trello_manager.delete_card(card_id)
        return redirect(url_for('index'))
    except Exception as e:
        return f"Failed to delete card: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
