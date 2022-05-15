from base_agent import BaseAgent
from game_data import GameData

Up = "N"
Down = "S"
Left = "W"
Right = "E"

class Agent(BaseAgent):
    def do_move(self, game_data: GameData):
        agent_x, agent_y = game_data.agent_pos
        visits_by = {game_data.agent_pos: None}
        queue = [(agent_x, agent_y)]
        while len(queue) > 0:
            x, y = queue.pop(0)
            if game_data.matrix[x][y] == 'a':
                break
            for new_x, new_y in [(x + 1, y), (x - 1, y), (x, y + 1), (0, y - 1)]:
                if (new_x, new_y) in visits_by:
                    continue
                if new_y < 0 or new_y >= game_data.grid_width:
                    continue
                if new_x < 0 or new_x >= game_data.grid_height:
                    continue
                if game_data.matrix[new_x][new_y] != '.' and game_data.matrix[new_x][new_y] != 'a':
                    continue
                new_location = new_x, new_y
                visits_by[new_location] = (x, y)
                queue.append(new_location)

        while True:
            if visits_by[(x, y)] == game_data.agent_pos:
                break
            else:
                x, y = visits_by[(x, y)]

        if y == agent_y + 1:
            return Up
        if y == agent_y - 1:
            return Down
        if x == agent_x + 1:
            return Right
        if x == agent_x - 1:
            return Left



if __name__ == "__main__":
    agent = Agent()
    agent.play()
