from flask import Flask, render_template


def create_app():
    from team.sqlitebp import bp as sqlitebp

    app = Flask(__name__)
    app.register_blueprint(sqlitebp)

    @app.route("/")
    def index():
        return render_template("index.tpl")

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
