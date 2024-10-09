from flask import Flask, render_template
import logging

from repository.csv_repository import init_taxi_drivers_from_csv
from repository.insert_data_db import insert_data_if_empty
from routes.post_route import post_bp
from routes.user_route import user_bp

# הגדרת פורמט הלוג כך שיכלול את הזמן, שם הקובץ ומספר השורה
logging.basicConfig(
    filename='project_logs.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s - %(filename)s:%(lineno)d'
)

app = Flask(__name__)

app.register_blueprint(user_bp)
app.register_blueprint(post_bp)

insert_data_if_empty('users', 'users')
insert_data_if_empty('posts', 'posts')
init_taxi_drivers_from_csv()

@app.route('/home')
def home():
    # TODO: להוסיף אפשרות להניס משתמש לחיפוש פוסטים
    return render_template(
        'index.html')


if __name__ == '__main__':
    app.run(debug=True)

# האם צריך גם וגם client, db
# TODO: run on docker
# TODO: make full CRUD
# TODO: add models