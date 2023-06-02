def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

solution = read_file('./120_quzhengjin.txt')


for i in range(0, len(solution)-1, 1):
    current_board=(solution[i].split(","))
    next_board=(solution[i+1].split(","))
    #print(current_board)
    diff = []
    print("step {}".format(i))
    for j in range(len(current_board)):
        if current_board[j] != next_board[j]:
            diff.append(j)
            print("postion {}: {} -> {}".format(j, current_board[j], next_board[j]))

    if current_board[diff[0]] != '-1':
        moving_piece =  current_board[diff[0]]
    else:
        moving_piece =  next_board[diff[0]]

    current_vacancy_index_sum = 0
    next_vacancy_index_sum = 0
    for index in diff:
        if current_board[index] == '-1':
            current_vacancy_index_sum += index
        else:
            next_vacancy_index_sum += index

    if len(diff) == 2:
        if current_vacancy_index_sum - next_vacancy_index_sum in [1, 2]:
            moving_direction = 'right'
        elif current_vacancy_index_sum - next_vacancy_index_sum in [-1, -2]:
            moving_direction = 'left'
        elif current_vacancy_index_sum - next_vacancy_index_sum in [-5, -10]:
            moving_direction = 'up'
        else:
            moving_direction = 'down'
    elif len(diff) == 4:
        if current_vacancy_index_sum - next_vacancy_index_sum in [2, 5]:
            moving_direction = 'right'
        elif current_vacancy_index_sum - next_vacancy_index_sum in [-2, -5]:
            moving_direction = 'left'
        elif current_vacancy_index_sum - next_vacancy_index_sum in [-10]:
            moving_direction = 'up'
        else:
            moving_direction = 'down'
    else: #zhenjing is moving
        if current_vacancy_index_sum - next_vacancy_index_sum in [5]:
            moving_direction = 'right'
        elif current_vacancy_index_sum - next_vacancy_index_sum in [-5]:
            moving_direction = 'left'
        elif current_vacancy_index_sum - next_vacancy_index_sum in [-15]:
            moving_direction = 'up'
        else:
            moving_direction = 'down'

    piece_map = {
        '0': "piece_zhengjing",
        '1': "piece_tangseng",
        '2': "piece_wukong",
        '3': "piece_bajie",
        '4': "piece_shaseng",
        '5': "piece_baima",
        '6': "piece_gui",
        '7': "piece_guai",
        '8': "piece_ling",
        '9': "piece_jing",
        '10': "piece_mo",
        '11': "piece_yao"
    }
    print(piece_map[moving_piece], moving_direction)
    #print("Difference between current_board and next_board: ", diff)

    #print(next_board)
    print("")