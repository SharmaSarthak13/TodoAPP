from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

app.app_context().push()

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    desc = db.Column(db.String(500), nullable = False)
    date_created = db.Column(db.DateTime, default =datetime.utcnow)
    
    def __repr__(self):
        return f"{self.sno}-{self.title}"


@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/products")
def products():
    return 'this is product page'

if __name__ =="__main__":
    app.run(debug=True)
