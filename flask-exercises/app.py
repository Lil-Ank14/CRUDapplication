from flask import Flask, render_template, request
import db


app = Flask(__name__)

@app.route('/')
def head():
    return render_template("index.html")

@app.get('/items')
def get_items():
    items = db.read_items()
    return render_template("items.html", items=items)


@app.post('/items')
def post_item():
    new_item = request.form.get('new-item') 
    db.create_item(new_item)
    items = db.read_items()

    return render_template('items.html', items=items)



@app.delete('/items/<int:item_id>')
def delete_item(item_id):
    db.delete_item(item_id)
    items = db.read_items()
    return render_template('items.html', items = items)


@app.get('/items/<int:item_id>')
def show_editForm(item_id):
    item_content = db.read_item(item_id)
    return render_template('edit.html', item_id = item_id, item_content = item_content)


@app.put('/items/<int:item_id>')
def put_item(item_id):
    updated_item = request.form.get('updated_item')

    print(updated_item)
    db.update_item(item_id, updated_item)
    
    items = db.read_items()

    return render_template('items.html', items = items)


if __name__ == '__main__':
    app.run(debug = True)   
    
    
    
