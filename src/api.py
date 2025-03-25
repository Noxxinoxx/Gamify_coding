"""
This file has some api calls.
1. game state: /api/game_state
"""

class Router:
    """
    This class is used to route all the api calls from the frontend and the backend.
    """
    def __init__(self):
        """
        init function for the API class.
        """
        
    def router(self, route):
        """
        This function is ment to hadle the api routes.
        """
        match route:
            case "/api/game_state":
                return self.router_game_state();        
    

    def router_game_state(self):
        """
        Function handels the fetching of the game state.
        """
        print("get game state.");
