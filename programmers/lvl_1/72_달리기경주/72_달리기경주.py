def solution(players, callings):
    location = {}

    for index, player in enumerate(players):
        location[player] = index

    for call in callings:
        index = location[call]
        location[call] = index - 1
        location[players[index - 1]] = index

        temp = players[index]
        players[index] = players[index - 1]
        players[index - 1] = temp

    return players

# Solution


def solution(players, callings):
    player_indices = {player: index for index, player in enumerate(players)}

    for j in callings:
        current_index = player_indices[j]
        desired_index = current_index - 1
        if current_index > 0 and players[desired_index] != j:
            players[current_index], players[desired_index] = players[desired_index], players[current_index]
            player_indices[players[current_index]] = current_index
            player_indices[players[desired_index]] = desired_index

    return players

# Remember how the solution made the dictionary. This works too
# Also review how the solution performs swapping of two variables. This works in python.
