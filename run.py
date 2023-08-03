import os
from taskmanager import app


def create_tables(self):
    with app.app_context():
        db.create_all()


create_tables(db)

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )
