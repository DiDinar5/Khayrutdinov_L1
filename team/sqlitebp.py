import click
from flask import Blueprint, g, render_template, redirect, url_for, request, current_app
from flask.cli import with_appcontext

from .model.captain import Captain
from .model.player import Player

from .db.SQLite import SQLiteDatabase as DBHandler

bp = Blueprint('sqlitebp', __name__, template_folder='templates')


@bp.before_request
def pre_handler():
    if 'form_data' not in g:
        g.form_data = None


@bp.after_request
def post_handler(response):
    DBHandler.close_db()
    return response


@bp.route('/')
def index():
    players = DBHandler.get_records()
    return render_template("team.tpl", form_data=g.form_data, items=players)


@bp.route('/edit/<int:id>')
def edit(id):
    g.form_data = DBHandler.get_record(id)
    return index()


@bp.route('/confirm_edit', methods=['POST'])
def confirm_edit():
    record = Captain() if 'grade' in request.form else Player()
    record.input()
    DBHandler.edit_record(record)
    return redirect(url_for('.index'))


@bp.route('/add', methods=['POST'])
def add():
    player = Player()
    player.input()
    DBHandler.add_record(player)
    return redirect(url_for('.index'))


@bp.route('/add_captain', methods=['POST'])
def add_captain():
    captain = Captain()
    captain.input()
    DBHandler.add_record(captain)
    return redirect(url_for('.index'))


@bp.route("/delete/<int:id>")
def delete(id):
    DBHandler.delete_record(id)
    return redirect(url_for('.index'))


@bp.route("/clear")
def clear():
    DBHandler.reset()
    return redirect(url_for('.index'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    DBHandler.init_db()
    click.echo('Initialized the database.')


bp.cli.add_command(init_db_command)
