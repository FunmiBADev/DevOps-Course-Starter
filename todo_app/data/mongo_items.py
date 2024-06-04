from typing import List
from pymongo import ASCENDING
import pymongo
from todo_app.data.itemStatus import ItemStatus
from todo_app.data.todo_item import TodoItem
from todo_app.mongo_config import MongoDBConfig
from pymongo.errors import PyMongoError

class MongoDbManager:

    def __init__(self, config):
        self.config = config
        self.client = pymongo.MongoClient(config.PRIMARY_CONNECTION_STRING)
        self.db = self.client[config.MONGO_DB_NAME]
        self.collection = self.db[config.COLLECTION_NAME]
        
    def create_todo_item(self, name, description):
        """
        Create a new MongoDB document.

        Args:
          name: The name of the item.
          description: The description of the item.
        """
        document = {
            'name': name,
            'description': description,
            'status': ItemStatus.TODO.value
        }
        
        result = self.collection.insert_one(document)
        if result.acknowledged:
            print(f"Document created with ID: {result.inserted_id}")
        else:
            print("Failed to create document")
            
    def get_todo_items(self) -> List[TodoItem]:
        """
        Get MongoDB documents and sort by status in ascending order.

        Returns:
          list: The list of saved items.
        """
        try:
          # Check if an index exists on 'status' field 
          if not self.collection.index_information().get("status_1"):
            self.collection.create_index([("status", ASCENDING)])  # Create ascending index on 'status'
            
          # Retrieve and sort documents by 'status' in ascending order
          documents = self.collection.find().sort('status', ASCENDING)
          items = [TodoItem.from_mongodb_doc(doc) for doc in documents]
          return items
        except PyMongoError as e:
          print(f"Error retrieving items or creating index: {e}")
          return []

    def update_todo_item_status(self, item_id, status):
        """
        Update the status of a MongoDB document.

        Args:
          item_id: The id of the item to be updated.
          status: The new status of the item.
        """
        result = self.collection.update_one(
            {'_id': item_id},
            {'$set': {'status': status}}
        )
        if result.modified_count == 1:
            print(f"Updated item with ID: {item_id}")
        else:
            print(f"Failed to update item with ID: {item_id}")  

    def delete_todo_item(self, item_id):
        """
        Delete a MongoDB document.

        Args:
          item_id: The id of the item to be deleted.
        """
        result = self.collection.delete_one({'_id': item_id})
        if result.deleted_count == 1:
            print(f"Deleted item with ID: {item_id}")
        else:
            print(f"Failed to delete item with ID: {item_id}")