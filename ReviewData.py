#Name:  Jennifer Henriquez
#Date:  12/23/2025
#Assigment: 2.5 Performance
#Objective: Create a python application that allows
#a user to manipulate data within a MongoDB document database.
#Class: SDC435

from pymongo import MongoClient
from bson import ObjectId

#Connect to Mongodb and select the amazon databse
User = MongoClient("mongodb://localhost:27017/")
db = User["Amazon"]
collection = db["ReviewData"]
print("importing data from file..")
print("data imported sucessfully!\n")

#Create new review doc
def create_review():
    print("\nCreate new review document...")
    review = {
        "review_id": input("Enter review_id: "),
        "product_id": input("Enter product_id: "),
        "revierwer_id": input("Enter reviewer_id: "),
        "starts": input("Enter start: "),
        "review_body": input("Enter review_body: "),
        "review_title": input("Enter review_title:"),
        "language": input("Enter language:"),
        "product_category": input("Enter product_category:")
        }
    result = collection.insert_one(review)
    print("Document created with _id: {result.insert_id}")

def read_review():
    print("\nPlease type in a number and press enter to execute the menu option:")
    print("1. Query by reviewID")
    print("2. Filter for a numeber of start and greater")
    print("3. filter for a less than a number of starts")
    print("4. Filter for a word in the title")
    print("5. Filter for a word in the review body content")
    choice = input("")
    if choice == "1":
        review_id = input("Enter review_id")
        result = collection.find_one({"review_id": review_id})

        print(result if result else "No document found")

    elif choice == "2":
        starts = input("Enter minimum starts: ")
        for doc in collection.find({"starts": {"$gte": starts}}):
            print(doc)

    elif choice == "3":
        starts = input("Enter maximum starts: ")
        for doc in collection.find({"starts": {"$lt": starts}}):
             print(doc)
            
    elif choice == "4":
        word = input("Search the title for: \n")
        for doc in collection.find({"review_title": {"$regex": word}}):
            print(doc)

    elif choice == "5":
        word = input("Search the title for: \n")
        for doc in collection.find({"review_body": {"$regex": word}}):
            print(doc)

    else:
        print("Invalid choice..Try again")
        
#Update a field in document...
        
def update_review():
    print("\nUpdate Fields of a document")
    review_id = input("Enter review_id of the document to update: \n")
    field = input("Enter the field to update: \n")
    new_value = input("Enter the new value: \n")

    result = collection.update_one({"review_id": review_id}, {"$set": {field: new_value}})
    print("Document update." if result.modified_count > 0 else "No document Updated.")
    

#Delete a specific document by _id

def delete_Menu_option():
    print("\n Delete a document")
    review_id = input(" Enter the review_id: \n")
    result = collection.delete_one({"review_id": review_id})
    print("Document deleted." if result.deleted_count > 0 else "No document found.")

#Delete all documents in the collection
def delete_all_doc():
    print("\nDelete all document in the collection.")
    confirm = input("type yes to confirm:\n ").upper()
    if confirm == "YES":
        collection.delete_many({})
        print("All documents have been deleted.")
    else:
        print("You have been disconected.")

#Delete the review collection

def delete_all_collection():
    print("Delete all colection.")
    confirm = input ("type DELETE to delete all the collection: \n").upper()
    if confirm == "DELETE":
        collection.drop()
        print("ReviewData collection deleted.")
    else:
        print("You choose to cancelled.")

#Main Menu

def main_menu():
  while True:
      print("Main Menu")
      print("1. query for document")
      print("2. Add new document")
      print("3. Update fields of a document")
      print("4. Delete a document")
      print("5. Delete all documents from collection")
      print("6. Delete a collection")
      print("7. Exit program")
      choice = input(" ")
      if choice == "1":
          read_review()
      elif choice == "2":
          create_review()
      elif choice == "3":
          update_review()
      elif choice == "4":
          delete_Menu_option()
      elif choice == "5":
          delete_all_doc()
      elif choice == "6":
          delete_all_collection()
      elif choice == "7":
         print("Exiting program...")
         break
      else:
         print("Invalid choice...")
        
main_menu()
