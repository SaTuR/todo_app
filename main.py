from flask import Flask, render_template, redirect, url_for,request
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

# /// = path relativo - //// = path absoluto
app.config["SQLALCHEMY_DATABASE_URI"] ='sqlite:///db.sqlite'
db = SQLAlchemy(app)


# Mapeo de Tabla
class Todo(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key = True)
    title =db.Column(db.String(100))
    state = db.Column(db.Boolean)



with app.app_context():
    db.create_all()



@app.route('/')
def index():
    todo_list = Todo.query.all()
    return render_template('index.html', todo_list=todo_list)

@app.route('/add',methods=['POST'])
def add():
    title = request.form.get('title')
    new_todo = Todo(title=title, state=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/update')
def update(id):
    pass

@app.route('/delete')
def delete(id):
    pass


if __name__ == '__main__':
    app.run(debug=True)