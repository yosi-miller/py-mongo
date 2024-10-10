from flask import Flask, render_template
import logging

from repository.csv_repository import init_crash_information_from_csv
from routes.crash_route import crash_bp


# הגדרת פורמט הלוג כך שיכלול את הזמן, שם הקובץ ומספר השורה
logging.basicConfig(
    filename='project_logs.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s - %(filename)s:%(lineno)d'
)

app = Flask(__name__)

app.register_blueprint(crash_bp)

init_crash_information_from_csv()

@app.route('/home')
def home():
    # TODO: להוסיף אפשרות להניס משתמש לחיפוש פוסטים
    return render_template(
        'index.html')


if __name__ == '__main__':
    app.run(debug=True)

# TODO: run on docker
# TODO: add readme