# Basic Setup
import pymongo

# Connect to MongoDB (make sure it's running)
client = pymongo.MongoClient("mongodb://localhost:27017/")
database_name = "todolist"
collection_name = "mylist"
db = client[database_name]
collection = db[collection_name]

# Create (Insert) function
def create_document(data):
    result = collection.insert_one(data)
    print(f"Document inserted with ID: {result.inserted_id}")

# Read function
def read_document(query):
    result = collection.find(query)
    for doc in result:
        print(doc)

# Update (Modify) function
def update_document(query, update_data):
    result = collection.update_many(query, {"$set": update_data})
    print(f"Matched {result.matched_count} documents and modified {result.modified_count} documents")

# Delete function
def delete_document(query):
    result = collection.delete_many(query)
    print(f"Deleted {result.deleted_count} documents")

# Test Code
if __name__ == "__main__":
    # Test Create (Insert)
    data_to_insert = {"Task": "task1 is to bring apple", "status": "on"}
    create_document(data_to_insert)

#     # Test Read
#     read_query = {"name": "John"}
#     print("Read Result:")
#     read_document(read_query)

    # # Test Update (Modify)
    # update_query = {"name": "John"}
    # update_data = {"age": 26}
    # print("Update Result:")
    # update_document(update_query, update_data)
    # read_document(read_query)  # Check if the update was successful

    # # Test Delete
    # print("Delete Result:")
    # delete_query = {"name": "John"}
    # delete_document(delete_query)
    # read_document(read_query)  # Check if the delete was successful
