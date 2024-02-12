from flask import Flask, render_template, request, redirect, url_for
from bson import ObjectId  # Import ObjectId from bson module
import pymongo

app = Flask(__name__)

# MongoDB setup
client = pymongo.MongoClient("mongodb://localhost:27017/")
database_name = "todolist"
collection_name = "mylist"
db = client[database_name]
collection = db[collection_name]

# MongoDB functions (Insert and Delete)
def create_document(data):
    result = collection.insert_one(data)
    print(f"Document inserted with ID: {result.inserted_id}")

def delete_document(query):
    result = collection.delete_many(query)
    print(f"Deleted {result.deleted_count} documents")

def update_status(document_id, new_status):
    query = {"_id": ObjectId(document_id)}
    update_data = {"status": new_status}
    result = collection.update_one(query, {"$set": update_data})
    print(f"Matched {result.matched_count} document and modified {result.modified_count} document")






# Routes
@app.route('/')
def index():
    # Retrieve all documents from the collection
    # documents = list(collection.find())
    
    documents = list(collection.find({"status": "on"}))
    done = list(collection.find({"status": "off"}))

    return render_template('index.html', documents=documents, done=done)

@app.route('/insert', methods=['POST'])
def insert():
    # Get data from the form
    task = request.form['task']
    status = "on"
    print("task: ", task)
    # Insert data into MongoDB
    data_to_insert = {"task": task,"status": status}
    create_document(data_to_insert)

    return redirect(url_for('index'))

@app.route('/delete/<id>')
def delete(id):
    # Delete document from MongoDB
    delete_query = {"_id": ObjectId(id)}
    delete_document(delete_query)

    return redirect(url_for('index'))

@app.route('/edit/<id>/<new_status>')
def edit_status(id, new_status):
    # Update status in MongoDB
    update_status(id, new_status)

    return redirect(url_for('index'))






if __name__ == '__main__':
    app.run(debug=True)
