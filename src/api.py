"""
This file has some api calls.
1. game state: /api/game_state
"""

class Router:
    """
    This class is used to route all the api calls from the frontend and the backend.
    """
    def __init__(self, game_class):
        """
        init function for the API class.
        """
        self.game = game_class;
        
    def router(self, route):
        """
        This function is ment to hadle the api routes.
        """
        match route:
            case "/api/game_status":
                return self.router_game_state();        
            case _:
                return "Error : Api call unknown!"

    def router_game_state(self):
        """
        Function handels the fetching of the game state.
        """
        print(self.game.game_status());
        print("get game state.");
