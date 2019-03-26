import numpy as np

W, H = 4, 4
ACTIONS = {
    'up': (-1, 0),
    'right': (0, 1),
    'down': (1, 0),
    'left': (0, -1)
}
GAMMA = 1
TERMINAL_STATES = [(0, 0), (3, 3)]


class GridWorld(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def step(self, curr_state, action):
        reward = -1
        next_state = self._next_state(curr_state, action)
        return reward, next_state

    def _next_state(self, curr_state, action):
        curr_w, curr_h = curr_state
        w_action, h_action = action

        next_w, next_h = curr_w + w_action, curr_h + h_action
        if self._out_of_boundary(next_h, next_w):
            return curr_state
        return next_w, next_h

    def _out_of_boundary(self, next_h, next_w):
        return next_w < 0 or next_w >= self.w or next_h < 0 or next_h >= self.h


def main(k):
    values = np.zeros((W, H))
    env = GridWorld(W, H)

    for _ in range(k):
        old_values = values.copy()
        for w in range(W):
            for h in range(H):
                curr_state = (w, h)
                if curr_state in TERMINAL_STATES:
                    continue

                reward_and_states = [env.step(curr_state, action) for action in ACTIONS.values()]
                returns = [reward + GAMMA * old_values[states] for reward, states in reward_and_states]
                values[curr_state] = sum(returns) / len(returns)

    print(values)


if __name__ == '__main__':
    np.set_printoptions(precision=2)
    run_time = int(input('run time: '))
    for _ in range(run_time):
        input_k = int(input('k: '))
        main(input_k)
