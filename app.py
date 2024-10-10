from flask import Flask, render_template
import logging

from repository.csv_repository import init_taxi_drivers_from_csv
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

init_taxi_drivers_from_csv()

@app.route('/home')
def home():
    # TODO: להוסיף אפשרות להניס משתמש לחיפוש פוסטים
    return render_template(
        'index.html')


if __name__ == '__main__':
    app.run(debug=True)

# TODO: run on docker
# TODO: add readme