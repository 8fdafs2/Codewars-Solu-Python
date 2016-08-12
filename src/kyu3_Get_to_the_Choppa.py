from math import sqrt
from collections import deque
from queue import PriorityQueue


class Position(tuple):
    def __new__(cls, x, y):
        return super().__new__(cls, (x, y))

    def __init__(self, x, y):
        self.x, self.y = x, y


class Node():
    def __init__(self, position, passable):
        self.position = position
        self.passable = passable
        self.hashval = position.__hash__()

    def __hash__(self):
        return self.hashval

    def __lt__(self, other):
        return True  # return self.position < other.position

    def __eq__(self, other):
        return True  # return self.position == other.position


def make_grid(grid_blueprint):
    grid = []
    start_node, end_node = None, None
    path = []
    rows = grid_blueprint.split('\n')
    n_rows, n_cols = len(rows), len(rows[0])
    for x in range(n_rows):
        grid.append([])
        row = rows[x]
        for y in range(n_cols):
            node_blueprint = row[y]
            if node_blueprint in 'SE0*':
                node = Node(Position(x, y), True)
                if node_blueprint == 'S':
                    start_node = node
                    path.append(node)
                elif node_blueprint == 'E':
                    end_node = node
                    path.append(node)
                elif node_blueprint == '*':
                    path.append(node)
            else:
                node = Node(Position(x, y), False)
            grid[-1].append(node)

    return grid, start_node, end_node, path


def print_grid(grid, start_node=None, end_node=None, path=[]):
    grid_blueprint = []
    for row in grid:
        grid_blueprint.append([])
        for node in row:
            if node is start_node:
                grid_blueprint[-1].append('S')
            elif node is end_node:
                grid_blueprint[-1].append('E')
            elif path and node in path:
                grid_blueprint[-1].append('#')
            elif node.passable:
                grid_blueprint[-1].append('0')
            else:
                grid_blueprint[-1].append('1')

    return '\n'.join([''.join(row) for row in grid_blueprint])


class Solution():
    """
    https://www.codewars.com/kata/5573f28798d3a46a4900007a

    GET TO THE CHOPPA! DO IT NOW!

    For this kata you must create a function that
    will find the shortest possible path between two nodes in a 2D grid of nodes.

    Details:

        Your function will take three arguments: a grid of nodes, a start node, and an end node.
        Your function will return a list of nodes that represent, in order,
        the path that one must follow to get from the start node to the end node.
        The path must begin with the start node and end with the end node.
        No single node should be repeated in the path (ie. no backtracking).

        def find_shortest_path(grid, start_node, end_node):
          pass

        The grid is a list of lists of nodes.
        Each node object has a position that indicates where in the grid the node is (it's indices).

        node.position.x  # 2
        node.position.y  # 5
        node.position  # (2,5)
        node is grid[2][5]  # True

        Each node may or may not be 'passable'. All nodes in a path must be passable.
        A node that is not passable is effectively a wall that the shortest path must go around.

        a_node.passable  # True

        Diagonal traversals between nodes are NOT allowed in this kata.
        Your path must move in one of 4 directions at any given step along the path: left, right, up, or down.
        Grids will always be rectangular (NxM), but they may or may not be square (NxN).
        Your function must return a shortest path for grid widths and heights ranging between 0 and 200.
        This includes 0x0 and 200x200 grids.
        When more than one shortest path exists (different paths, all viable, with the same number of steps)
        then any one of these paths will be considered a correct answer.
        Your function must be efficient enough (in terms of time complexity)
        to pass all the included tests within the allowed timeframe (6 seconds).
        For your convenience, a print_grid function exists that you can use to print a grid.
        You can also use print_grid to visualize a given path on the given grid.
        The print_grid function has the following signature:

    def print_grid(grid, start_node=None, end_node=None, path=None)
    # output without a path
    S0110
    01000
    01010
    00010
    0001E

    # output with a path
    S0110
    #1###
    #1#1#
    ###1#
    0001E
    """

    def __init__(self):
        pass

    def find_shortest_path_01(self, grid, start_node, end_node):
        """
        depth-first, recursion, move priority
        """
        if not grid:
            return []
        s_x, s_y = start_node.position.x, start_node.position.y
        e_x, e_y = end_node.position.x, end_node.position.y
        n_rows, n_cols = len(grid), len(grid[0])
        x_max, y_max = n_rows - 1, n_cols - 1

        class G:
            paths = []
            len_path = 0
            len_path_min = 0
            len_path_max = 0
            n_iter = 0
            n_iter_resto = 0
            flag_ret = False

        def recur_mov_l(path):
            s_x, s_y = path[-1]
            if s_x < x_max:
                node = grid[s_x + 1][s_y]
                if node.passable and (s_x + 1, s_y) not in path:
                    recur(path + [(s_x + 1, s_y), ])

        def recur_mov_r(path):
            s_x, s_y = path[-1]
            if s_x > 0:
                node = grid[s_x - 1][s_y]
                if node.passable and (s_x - 1, s_y) not in path:
                    recur(path + [(s_x - 1, s_y), ])

        def recur_mov_d(path):
            s_x, s_y = path[-1]
            if s_y < y_max:
                node = grid[s_x][s_y + 1]
                if node.passable and (s_x, s_y + 1) not in path:
                    recur(path + [(s_x, s_y + 1), ])

        def recur_mov_u(path):
            s_x, s_y = path[-1]
            if s_y > 0:
                node = grid[s_x][s_y - 1]
                if node.passable and (s_x, s_y - 1) not in path:
                    recur(path + [(s_x, s_y - 1), ])

        def recur(path):
            if G.flag_ret:
                return
            s_x, s_y = path[-1]
            if (s_x, s_y) == (e_x, e_y):
                G.paths.append(path)
                G.len_path = len(path) - 1
                G.n_iter = G.n_iter_resto
                return
            if G.n_iter == 0:
                G.len_path -= 1
                G.n_iter = G.n_iter_resto
            else:
                G.n_iter -= 1
            if G.len_path < len(path) + 1:
                return
            if G.len_path < G.len_path_min:
                G.flag_ret = True
                return

            d_x = e_x - s_x
            d_y = e_y - s_y

            if d_x > 0:  # l > r
                if d_y > 0:  # d > u
                    if d_x > d_y:  # l > d > u > r
                        movs = [recur_mov_l, recur_mov_d, recur_mov_u, recur_mov_r]
                    else:  # d > l > r > u
                        movs = [recur_mov_d, recur_mov_l, recur_mov_r, recur_mov_u]
                else:  # u > d
                    if d_x > -d_y:  # l > u > d > r
                        movs = [recur_mov_l, recur_mov_u, recur_mov_d, recur_mov_r]
                    else:  # u > l > r > d
                        movs = [recur_mov_u, recur_mov_l, recur_mov_r, recur_mov_d]
            else:  # r > l
                if d_y > 0:  # d > u
                    if -d_x > d_y:  # r > d > u > l
                        movs = [recur_mov_r, recur_mov_d, recur_mov_u, recur_mov_l]
                    else:  # d > r > l > u
                        movs = [recur_mov_d, recur_mov_r, recur_mov_l, recur_mov_u]
                else:  # u > d
                    if -d_x > -d_y:  # r > u > d > l
                        movs = [recur_mov_r, recur_mov_u, recur_mov_d, recur_mov_l]
                    else:  # u > r > l > d
                        movs = [recur_mov_u, recur_mov_r, recur_mov_l, recur_mov_d]

            for recur_mov in movs:
                if G.flag_ret:
                    return
                recur_mov(path)

        n_max, n_min = (n_rows, n_cols) if n_rows > n_cols else (n_cols, n_rows)
        n_nodes_passable = sum([node.passable for row in grid for node in row])

        G.len_path_min = abs(e_x - s_x) + abs(e_y - s_y) + 1
        G.len_path = G.len_path_max = min(n_max * n_min // 2 + n_min - n_min // 2, n_nodes_passable)

        G.n_iter_resto = G.n_iter = G.len_path_max * 10

        recur([(start_node.position.x, start_node.position.y), ])

        if G.paths:
            return [grid[x][y] for (x, y) in G.paths[-1]]

        return []

    def find_shortest_path_02(self, grid, start_node, end_node):
        """
        while-loop, neighbour scan & link
        """
        if not grid:
            return []
        nodes = {(node.position.x, node.position.y): node for row in grid for node in row}
        offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        play = [[start_node, []]]
        visited = {(start_node.position.x, start_node.position.y), }
        while play:
            next_play = []
            for node, path in play:
                child_nodes = [
                    nodes.get((x, y), None) for x, y in
                    [(node.position.x + o_x, node.position.y + o_y) for o_x, o_y in offsets]
                    if (x, y) not in visited]
                for child_node in child_nodes:
                    if not child_node or not child_node.passable:
                        continue
                    if child_node is end_node:
                        return path + [node, end_node]
                    visited.add((child_node.position.x, child_node.position.y))
                    next_play.append([child_node, path + [node]])
            play = next_play
        return []

    def find_shortest_path_03(self, grid, node_start, node_end):
        """
        while-loop, neighbour scan & link
        """
        if not grid:
            return []
        x_max, y_max = len(grid) - 1, len(grid[0]) - 1
        if node_start.position == node_end.position:
            return [node_start]

        def build_path(node_end, node_start):
            if node_end is node_start:
                return [node_start]
            return build_path(node_end.parent, node_start) + [node_end]

        que = deque([node_start, ])
        while que:
            node = que.pop()
            x, y = node.position.x, node.position.y
            nodes_adj = []
            if x > 0:
                nodes_adj.append(grid[x - 1][y])
            if x < x_max:
                nodes_adj.append(grid[x + 1][y])
            if y > 0:
                nodes_adj.append(grid[x][y - 1])
            if y < y_max:
                nodes_adj.append(grid[x][y + 1])
            for node_adj in nodes_adj:
                if node_adj is node_end:
                    node_end.parent = node
                    return build_path(node_end, node_start)
                if node_adj.passable and not hasattr(node_adj, 'visited'):
                    node_adj.visited = True
                    node_adj.parent = node
                    que.appendleft(node_adj)
        return []

    def find_shortest_path_04(self, grid, start_node, end_node):
        """
        while-loop, global scan & link
        """
        if not grid:
            return []
        s_x, s_y = start_node.position.x, start_node.position.y
        e_x, e_y = end_node.position.x, end_node.position.y
        n_rows, n_cols = len(grid), len(grid[0])
        x_max, y_max = n_rows - 1, n_cols - 1

        paths = [[None for _ in range(n_cols)] for _ in range(n_rows)]
        paths[s_x][s_y] = [start_node]

        rng_rows, rng_cols = list(range(n_rows)), list(range(n_cols))

        while True:
            for x in rng_rows:
                for y in rng_cols:
                    node = grid[x][y]
                    if not paths[x][y] and node.passable:
                        if 0 < x and paths[x - 1][y]:
                            paths[x][y] = paths[x - 1][y] + [node]
                        elif x < x_max and paths[x + 1][y]:
                            paths[x][y] = paths[x + 1][y] + [node]
                        elif 0 < y and paths[x][y - 1]:
                            paths[x][y] = paths[x][y - 1] + [node]
                        elif y < y_max and paths[x][y + 1]:
                            paths[x][y] = paths[x][y + 1] + [node]
            if paths[e_x][e_y]:
                return paths[e_x][e_y]

        return []

    def find_shortest_path_05(self, grid, start_node, end_node):
        """
        A* search, hashtab
        """
        if not grid:
            return []

        n_rows, n_cols = len(grid), len(grid[0])
        x_max, y_max = n_rows - 1, n_cols - 1
        closed_set = set()
        open_set = {start_node, }
        parents = dict()
        g_scores = dict()
        f_scores = dict()

        def distance(node1, node2):
            return abs(node1.position.x - node2.position.x) + abs(node1.position.y - node2.position.y)
            # return sqrt((node1.position.x - node2.position.x) ** 2 + (node1.position.y - node2.position.y) ** 2)

        def get_path(current):
            path = [current, ]
            while current in parents:
                current = parents[current]
                path.append(current)
            path.reverse()  # We want start -> end path
            return path

        def neighbors(node):
            x, y = node.position.x, node.position.y
            if y > 0:
                neighbor = grid[x][y - 1]
                if neighbor.passable and neighbor not in closed_set:
                    yield neighbor
            if y < y_max:
                neighbor = grid[x][y + 1]
                if neighbor.passable and neighbor not in closed_set:
                    yield neighbor
            if x > 0:
                neighbor = grid[x - 1][y]
                if neighbor.passable and neighbor not in closed_set:
                    yield neighbor
            if x < x_max:
                neighbor = grid[x + 1][y]
                if neighbor.passable and neighbor not in closed_set:
                    yield neighbor

        # pre-set h_score (distance to end node) and g_score (distance to start node) for all nodes
        for row in grid:
            for node in row:
                g_scores[node] = f_scores[node] = 99999

        g_scores[start_node] = 0
        f_scores[start_node] = distance(start_node, end_node)

        que = PriorityQueue()
        que.put((f_scores[start_node], start_node))

        while open_set:
            _, current = que.get()
            if current is end_node:
                return get_path(end_node)
            open_set.remove(current)
            closed_set.add(current)

            for neighbour in neighbors(current):
                g_score = g_scores[current] + 1
                f_score = g_score + distance(neighbour, end_node)

                if neighbour not in open_set:
                    open_set.add(neighbour)
                    que.put((f_score, neighbour))
                elif g_score > g_scores[neighbour]:
                    continue

                parents[neighbour] = current
                g_scores[neighbour] = g_score
                f_scores[neighbour] = f_score

        return []

    def find_shortest_path_06(self, grid, start_node, end_node):
        """
        A* search, object wrap
        """
        if not grid:
            return []

        class SearchNode(Node):
            """Wraps the problem's node objects with extra info needed for the search."""

            def __init__(self, node):
                super().__init__(node.position, node.passable)
                self.node = node
                self.x, self.y = self.position
                self.f_score = self.g_score = 99999
                self.parent = None

            def distance_to(self, other):
                return abs(other.x - self.x) + abs(other.y - self.y)

            def get_path(self):
                path = [self.node]
                current = self
                while current.parent:
                    path.append(current.parent.node)
                    current = current.parent
                path.reverse()
                return path

            def neighbours(self):
                for x_offset, y_offset in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    pos = (self.x + x_offset, self.y + y_offset)
                    if pos in pos_lookup:
                        search_node = pos_lookup[pos]
                        if search_node.passable and search_node not in closed_set:
                            yield search_node

        search_nodes = {node: SearchNode(node) for row in grid for node in row}

        start_node = search_nodes[start_node]
        end_node = search_nodes[end_node]
        start_node.g_score = 0
        start_node.f_score = start_node.distance_to(end_node)

        pos_lookup = {(search_node.x, search_node.y): search_node
                      for search_node in search_nodes.values()}

        closed_set = set()
        open_set = {start_node, }
        que = PriorityQueue()
        que.put((start_node.f_score, start_node))

        while que:
            _, current = que.get()
            if current is end_node:
                return current.get_path()
            open_set.remove(current)
            closed_set.add(current)

            for neighbour in current.neighbours():
                g_score = current.g_score + 1  # All neighbours are distance 1 from current
                f_score = g_score + neighbour.distance_to(end_node)

                if neighbour not in open_set:
                    open_set.add(neighbour)
                    que.put((f_score, neighbour))
                elif g_score > neighbour.g_score:
                    continue

                neighbour.parent = current
                neighbour.g_score = g_score
                neighbour.f_score = f_score

        return []


def sets_gen(find_shortest_path):
    test_sets = []
    grid_blueprints = [
        """\
S0110
01000
01010
00010
0001E\
""",
        """\
S11111111111
000000000001
101111011101
100010001111
101010100000
00100011111E\
""",
        """\
0000000000000000000000
S111111111111111110101
0000000000000000010101
1111111011110111010101
0110001000100011110101
0000101010101000000101
0111100010001111101101
0111111111111000100001
0100010001000000111111
0101010101010010000001
0101010101011110111101
00010001000110000011E1\
""",
        """\
0000000000000000000000
S111111111111111110101
0000000000000000010101
1111111111110111010101
0000001000100011110101
0000101010101000000101
0111100010001111101101
0111111111111000100001
0100010001000000111111
0101010101010000000001
0101010101011110111101
00010001000110000011E1\
""",
        ('S' + '0' * 199 + '\n') + ('0' * 200 + '\n') * 198 + ('0' * 199 + 'E'),
    ]
    for grid_blueprint in grid_blueprints:
        grid, start_node, end_node, path = make_grid(grid_blueprint)
        # print('\n------- ORIG ---------')
        # print(print_grid(grid, start_node, end_node, path))
        match = sol.find_shortest_path_01(grid, start_node, end_node)
        # print('------- SOLV ---------')
        # print(print_grid(grid, start_node, end_node, match))
        test_sets.append((
            (grid, start_node, end_node),
            match
        ))
    return test_sets


def cmpr(to_match, test_set):
    args, match = test_set
    grid, start_node, end_node = args
    if to_match[0] is not start_node:
        return False
    if to_match[-1] is not end_node:
        return False
    for i in range(len(to_match) - 1):
        node = to_match[i]
        node_next = to_match[i + 1]
        if not node.passable:
            return False
        if abs(node.position.x - node_next.position.x) + \
                abs(node.position.y - node_next.position.y) != 1:
            return False
    return len(to_match) == len(match)


if __name__ == '__main__':
    sol = Solution()
    from test_fixture import Test_Fixture

    tf = Test_Fixture(sol, sets_gen, cmpr)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(5, prt_docstr=True)
