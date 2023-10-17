import os


class TrelloConfig:
    """ Trello API Data Configuration variables """

    def __init__(self):
        self.BOARD_ID = os.environ.get('BOARD_ID')
        self.TRELLO_API_KEY = os.environ.get('TRELLO_API_KEY')
        self.TRELLO_TOKEN = os.environ.get('TRELLO_TOKEN')
        self.BASE_URL = os.environ.get('BASE_URL')
        self.TRELLO_TO_DO = os.environ.get('TRELLO_TO_DO')
        self.TRELLO_IN_PROGRESS = os.environ.get('TRELLO_IN_PROGRESS')
        self.TRELLO_DONE = os.environ.get('TRELLO_DONE')
        self.SECRET_KEY = os.environ.get('SECRET_KEY')
        if not self.SECRET_KEY:
            raise ValueError(
                "No SECRET_KEY set for Flask application. Did you follow the setup instructions?")
