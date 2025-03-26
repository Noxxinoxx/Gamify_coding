"""
This file has some api calls.
1. game state: /api/game_status
2. current game time : /api/current_time
"""
import tools;
class Router:
    """
    This class is used to route all the api calls from the frontend and the backend.
    """
    def __init__(self,timer, game_class):
        """
        init function for the API class.
        """
        self.game = game_class;
        self.timer = timer;

    def router(self, route):
        """
        This function is ment to hadle the api routes.
        """
        match route:
            case b"/api/game_status":
                return self.router_game_status();        
            case b"/api/current_time": 
                return self.router_game_timer();
            case _:
                return "Error : Api call unknown!"

    def router_game_status(self):
        """
        Function handels the fetching of the game state.
        """
        return tools.tranfrom_into_string(self.game.game_status());
    def router_game_timer(self): 
        """
        Get the game timer.
        """
        return tools.tranfrom_into_string(self.timer.current_time);


