import math

def max_value(tree, count=None):
    if count == None:
        count = -math.inf
    if type(tree) == int:
        return tree
    else:
        for large in tree:
            count = max(count, min_value(large))
    return (count)


def min_value(tree, count=None):
    if count == None:
        count = math.inf
    if type(tree) == int:
        return tree
    else:
        for large in tree:
            count = min(count, max_value(large))
    return (count)


#tests 
game_tree = 3

print("Root utility for minimiser:", min_value(game_tree))
print("Root utility for maximiser:", max_value(game_tree))

game_tree = [1, 2, 3]

print("Root utility for minimiser:", min_value(game_tree))
print("Root utility for maximiser:", max_value(game_tree))

game_tree = [1, 2, [3]]

print(min_value(game_tree))
print(max_value(game_tree))

game_tree = [[1, 2], [3]]

print(min_value(game_tree))
print(max_value(game_tree))


def  max_action_value(game_tree):
    if type(game_tree) == int:
        return None, game_tree
    else:
        holder = []
        for i, branch in enumerate(game_tree):
            maxi = min_value(branch)
            holder.append((i, maxi))
        return max(holder, key=lambda x: x[1])

def min_action_value(game_tree):
    if type(game_tree) == int:
        return None, game_tree
    else:
        holder = []
        for i, branch in enumerate(game_tree):
            mini = max_value(branch)
            holder.append((i, mini))
        return min(holder, key=lambda x: x[1])

#test cases

game_tree = [2, [-3, 1], 4, 1]

action, value = min_action_value(game_tree)
print("Best action if playing min:", action)
print("Best guaranteed utility:", value)
print()
action, value = max_action_value(game_tree)
print("Best action if playing max:", action)
print("Best guaranteed utility:", value)

game_tree = 3

action, value = min_action_value(game_tree)
print("Best action if playing min:", action)
print("Best guaranteed utility:", value)
print()
action, value = max_action_value(game_tree)
print("Best action if playing max:", action)
print("Best guaranteed utility:", value)

game_tree = [1, 2, [3]]

action, value = min_action_value(game_tree)
print("Best action if playing min:", action)
print("Best guaranteed utility:", value)
print()
action, value = max_action_value(game_tree)
print("Best action if playing max:", action)
print("Best guaranteed utility:", value)