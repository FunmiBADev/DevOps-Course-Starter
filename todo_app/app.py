from typing import List
from flask import Flask, request, redirect, url_for, render_template
from todo_app.data.trello_items import TrelloManager
from todo_app.trello_config import TrelloConfig
from todo_app.views.view_model import ViewModel


def create_app():
    app = Flask(__name__)
    app.config.from_object(TrelloConfig())
    config = TrelloConfig()  # Create a single TrelloDataConfig instance
    trello_manager = TrelloManager(config)  # Create a single TrelloManager instance

    @app.route('/')
    def index():
        trello_items = trello_manager.get_items()
        view_model = ViewModel(trello_items)
        return render_template('index.html', view_model=view_model)

    @app.route('/additem', methods=['POST'])
    def additem():
        title = request.form.get('title')
        desc = request.form.get('description')
        trello_manager.create_card(title, desc)
        return redirect(url_for('index'))

    @app.route('/mark_complete/<card_id>', methods=['POST'])
    def mark_card_done(card_id):
        try:
            list_id_done = config.TRELLO_DONE  # Replace with the desired list ID for "Done"
            trello_manager.update_item_status(card_id, list_id_done)
            return redirect(url_for('index'))
        except Exception as e:
            return f"Failed to mark card complete {str(e)}"

    @app.route('/mark_progress/<card_id>', methods=['POST'])
    def mark_card_progress(card_id):
        try:
            # Replace with the desired list ID for "Progress"
            list_id_progress = config.TRELLO_IN_PROGRESS
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
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
