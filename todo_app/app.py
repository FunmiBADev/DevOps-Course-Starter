from flask import Flask, request, redirect, url_for, render_template
from todo_app.data.mongo_items import MongoDbManager
from todo_app.mongo_config import MongoDBConfig
from todo_app.views.view_model import ViewModel
from todo_app.data.itemStatus import ItemStatus


def create_app():
    app = Flask(__name__)
    app.config.from_object(MongoDBConfig())
    conf = MongoDBConfig() # Create a single MongoDataConfig instance
    mongodb_manager = MongoDbManager(conf) # Create a single MongoDbManager instance

    @app.route('/')
    def index():
        mongo_items = mongodb_manager.get_todo_items()
        view_model = ViewModel(mongo_items)
        return render_template('index.html', view_model=view_model)

    @app.route('/additem', methods=['POST'])
    def additem():
        title = request.form.get('title')
        desc = request.form.get('description')
        mongodb_manager.create_todo_item(title, desc)
        return redirect(url_for('index'))

    @app.route('/mark_complete/<item_id>', methods=['POST'])
    def mark_card_done(item_id):
        try:
            mongodb_manager.update_todo_item_status(item_id, ItemStatus.DONE.value)
            return redirect(url_for('index'))
        except Exception as e:
            return f"Failed to mark item complete {str(e)}"

    @app.route('/mark_progress/<item_id>', methods=['POST'])
    def mark_card_progress(item_id):
        try:
            mongodb_manager.update_todo_item_status(item_id, ItemStatus.PROGRESS.value)
            return redirect(url_for('index'))
        except Exception as e:
            return f"Failed to progress item status: {str(e)}"

    @app.route('/removeitem/<item_id>', methods=['POST'])
    def removeitem(item_id):
        try:
            mongodb_manager.delete_todo_item(item_id)
            return redirect(url_for('index'))
        except Exception as e:
            return f"Failed to delete card: {str(e)}"
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
