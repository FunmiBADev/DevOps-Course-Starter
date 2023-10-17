from typing import List
import requests
from todo_app.data.itemStatus import ItemStatus
from todo_app.data.todo_item import TodoItem
from todo_app.trello_config import TrelloConfig


class TrelloManager:

    def __init__(self, config):
        self.config = config
        self.base_url = config.BASE_URL
        self.board_id = config.BOARD_ID
        self.api_key = config.TRELLO_API_KEY
        self.api_token = config.TRELLO_TOKEN

    def create_card(self, name, desc):
        """
        Create a new Trello card.

        Args:
          name: The name of the item.
          desc: The description of the item.
        """
        params = {
            'idList': self.config.TRELLO_TO_DO,
            'name': name,
            'desc': desc,
            "key": self.api_key,
            "token": self.api_token
        }

        new_card_endpoint = "cards"
        response = requests.post(
            self.base_url + new_card_endpoint, params=params)
        if response.ok:
            print(f"Card created")
        else:
            print(
                f"Failed to create card, Status code: {response.status_code}")

    def update_item_status(self, card_id, list_id):
        """
        Update the status of a Trello card.

        Args:
          card_id: The id of the item to be updated.
          list_id: The id of the respective status list.
        """
        params = {
            'idList': list_id,
            "key": self.api_key,
            "token": self.api_token
        }
        card_endpoint = f"cards/{card_id}"
        response = requests.put(self.base_url + card_endpoint, params=params)
        if response.status_code != 200:
            raise Exception(
                f"Failed to update item status. Status code: {response.status_code}")

    def delete_card(self, card_id):
        """
        Delete a Trello card.

        Args:
          card_id: The id of the item to be deleted.
        """
        params = {
            "key": self.api_key,
            "token": self.api_token
        }
        card_endpoint = f"cards/{card_id}"
        response = requests.delete(
            self.base_url + card_endpoint, params=params)
        if response.ok:
            print(f"Deleted card with ID: {card_id}")
        else:
            print(
                f"Failed to delete card with ID: {card_id}, Status code: {response.status_code}")

    def get_items(self):
        """
        Get Trello items and sort by status in descending order.

        Returns:
          list: The list of saved items.
        """
        board_list_endpoint = f"boards/{self.board_id}/lists"

        params = {
            "key": self.api_key,
            "token": self.api_token,
            "cards": "open"
        }

        response = requests.get(
            self.base_url + board_list_endpoint, params=params)

        if response.status_code != 200:
            raise Exception(
                f"Failed to retrieve data from Trello API. Status code: {response.status_code}")

        response_json = response.json()

        items = []

        for trello_list in response_json:
            for card in trello_list['cards']:
                card['status'] = trello_list['name']
                item = TodoItem.from_trello_card(card, trello_list)
                items.append(item)

        # Sort items by status in descending order
        sorted_items = sorted(items, key=lambda x: x.status, reverse=True)

        return sorted_items
