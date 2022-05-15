from base_agent import BaseAgent
from game_data import GameData

Up = "N"
Down = "S"
Left = "W"
Right = "E"


class Agent(BaseAgent):
    def do_move(self, game_data: GameData):
        heuristics = self.get_heuristics(game_data)
        agent_x, agent_y = game_data.agent_pos
        visits_by = {game_data.agent_pos: None}
        queue = [{"pos": (agent_x, agent_y) , "cost": 0}]
        while len(queue) > 0:
            queue.sort(key=lambda k : k["cost"] + heuristics[k['pos'][0]][k['pos'][1]],reverse=True)
            data = queue.pop()
            x, y = data['pos']
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
                queue.append({"pos": new_location , "cost": data['cost']+1})
                visits_by[new_location] = (x, y)

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


    def get_heuristics(self, game_data):
        heuristics = []
        destinations = []
        for i in range(game_data.grid_height):
            for j in range(game_data.grid_width):
                if game_data.matrix[i][j] == 'a':
                    destinations.append((i,j))

        for i in range(game_data.grid_height):
            new_line = []
            for j in range(game_data.grid_width):
                minimum = -1
                for x, y in destinations:
                    distance = abs(x-i) + abs(y-j)
                    if minimum == -1 or distance < minimum:
                        minimum = distance
                new_line.append(minimum)

            heuristics.append(new_line)


        return heuristics

if __name__ == "__main__":
    agent = Agent()
    agent.play()
