from flask import Flask, render_template_string
import logging
from configuration_db import insert_data_if_empty
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

@app.route('/home')
def home():
    # TODO: להוסיף אפשרות להניס משתמש לחיפוש פוסטים
    # TODO: להפריד HTML לקובץ נפרד
    return render_template_string('''
    <div direction="rtl">
    
        <h1>welcome to my app</h1>
            <ul>
                <li><a href="/users/">Users</a></li>
                <li><a href="/posts/">Posts</a></li>
                <li><a href="/posts/1">Posts by user ID (EX: 1)</a></li>
            </ul>
    <div>
    ''')


if __name__ == '__main__':
    app.run(debug=True)

# האם צריך גם וגם client, db
# עבור כל גישה למסד הנתונים try, except ואם יש שגיאה לודא שהמסד נסגר
