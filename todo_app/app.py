from flask import Flask
from flask import request
from flask import redirect
from flask import url_for
from flask import render_template

from todo_app.flask_config import Config

from todo_app.data.session_items import get_items, get_item, add_item, save_item, remove_item


from operator import itemgetter, attrgetter

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_items()
    # sort the items before displaying them
    items = sorted(items, key=lambda x: x['status'], reverse=True)
    return render_template('index.html', items=items)

@app.route('/additem', methods=['POST'])
def additem():
    title = request.form.get('title')
    add_item(title)
    return redirect(url_for('index'))

@app.route('/completeitem', methods=['POST'])
def completeitem():
    id = request.form.get('id')
    item = get_item(id)
    item['status'] = "Completed"
    save_item(item)
    return redirect(url_for('index'))

@app.route('/removeitem', methods=['POST'])
def removeitem():
    id = request.form.get('id')
    # item = get_item(id)
    remove_item(id)
    return redirect(url_for('index'))
