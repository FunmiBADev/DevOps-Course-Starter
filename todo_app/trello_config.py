import os

class TrelloStaticDataConfig:
    """ Trello API Static Data Configuration variables """
    BOARD_ID = os.environ.get('BOARD_ID')
    TRELLO_API_KEY = os.environ.get('TRELLO_API_KEY')
    TRELLO_TOKEN = os.environ.get('TRELLO_TOKEN')
    BASE_URL = os.environ.get('BASE_URL')
    TRELLO_TO_DO = os.environ.get('TRELLO_TO_DO')
    TRELLO_IN_PROGRESS = os.environ.get('TRELLO_IN_PROGRESS')
    TRELLO_DONE = os.environ.get('TRELLO_DONE')