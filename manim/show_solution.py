from manim import *

def shift_down(mobject):
    return mobject.shift(DOWN)

def shift_up(mobject):
    return mobject.shift(UP)

def shift_right(mobject):
    return mobject.shift(RIGHT)

def shift_left(mobject):
    return mobject.shift(LEFT)

def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def produce_moving_list():
    solution = read_file('../120_quzhengjin.txt')
    moving_list = []

    for i in range(0, len(solution)-1, 1):
        current_board=(solution[i].split(","))
        next_board=(solution[i+1].split(","))
        #print(current_board)
        diff = []
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
            if current_vacancy_index_sum - next_vacancy_index_sum in [2]:
                moving_direction = 'right'
            elif current_vacancy_index_sum - next_vacancy_index_sum in [-2]:
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

        moving_list.append((moving_piece, moving_direction))    
    
    return moving_list

class Show_Solution(Scene):
    def construct(self):
        board = Rectangle(width=5, height=6, fill_opacity=0.1, color=GREEN)
        self.play(Create(board))

        box = Rectangle(width=1, height=1, color=RED_B, fill_opacity=1)
        text = Text('沙僧', font_size=24).move_to(box.get_center())
        piece_shaseng = VGroup().add(box, text)

        box = Rectangle(width=1, height=1, color=RED_A, fill_opacity=1)
        text = Text('悟空', font_size=24).move_to(box.get_center())
        piece_wukong = VGroup().add(box, text)

        box = Rectangle(width=1, height=1, color=RED_C, fill_opacity=1)
        text = Text('八戒', font_size=24).move_to(box.get_center())
        piece_bajie = VGroup().add(box, text)

        box = Rectangle(width=1, height=1, color=RED_E, fill_opacity=1)
        text = Text('唐僧', font_size=24).move_to(box.get_center())
        piece_tangseng = VGroup().add(box, text)

        box = Rectangle(width=1, height=1, color=WHITE, fill_opacity=1)
        text = Text('白龙马', font_size=24, color=BLACK).move_to(box.get_center())
        piece_baima = VGroup().add(box, text)

        box = Rectangle(width=2, height=1, color=PURPLE_A, fill_opacity=1)
        text = Text('鬼', font_size=24).move_to(box.get_center())
        piece_gui = VGroup().add(box, text)
        
        box = Rectangle(width=2, height=1, color=PURPLE_B, fill_opacity=1)
        text = Text('魔', font_size=24).move_to(box.get_center())
        piece_mo = VGroup().add(box, text)
        
        box = Rectangle(width=1, height=2, color=BLUE_A, fill_opacity=1)
        text = Text('鬼', font_size=24).move_to(box.get_center())
        piece_guai = VGroup().add(box, text)

        box = Rectangle(width=1, height=2, color=BLUE_B, fill_opacity=1)
        text = Text('精', font_size=24).move_to(box.get_center())
        piece_jing =VGroup().add(box, text)
        
        box = Rectangle(width=1, height=2, color=BLUE_C, fill_opacity=1)
        text = Text('灵', font_size=24).move_to(box.get_center())
        piece_ling = VGroup().add(box, text)

        box = Rectangle(width=1, height=2, color=BLUE_D, fill_opacity=1)
        text = Text('妖', font_size=24).move_to(box.get_center())
        piece_yao =VGroup().add(box, text)

        # Position the game pieces on the board
        piece_shaseng.move_to(board.get_corner(UL) + RIGHT / 2 + DOWN / 2)
        piece_wukong.move_to(piece_shaseng.get_corner(RIGHT) + RIGHT / 2)
        piece_bajie.move_to(piece_shaseng.get_corner(DOWN) + DOWN / 2)
        piece_tangseng.move_to(piece_bajie.get_corner(DOWN) + DOWN / 2)
        piece_baima.move_to(piece_tangseng.get_corner(RIGHT) + RIGHT / 2)
        
        piece_gui.move_to(board.get_corner(UR) + LEFT + DOWN / 2)
        piece_mo.move_to(piece_baima.get_corner(DOWN) + DOWN / 2 + RIGHT / 2)

        piece_guai.move_to(piece_gui.get_corner(DOWN) + DOWN + RIGHT / 2)
        piece_jing.move_to(piece_mo.get_corner(UR) + RIGHT / 2)
        piece_ling.move_to(piece_jing.get_corner(RIGHT) + RIGHT / 2 + DOWN)
        piece_yao.move_to(piece_tangseng.get_corner(DOWN) +  DOWN)
        
        zhengjin_position_list = [        
            piece_wukong.get_corner(UR), 
            piece_wukong.get_corner(UR) + RIGHT,
            piece_wukong.get_corner(UR) + RIGHT + DOWN,
            piece_wukong.get_corner(UR) + RIGHT + DOWN + RIGHT,
            piece_wukong.get_corner(UR) + RIGHT + DOWN + RIGHT + DOWN,
            piece_wukong.get_corner(UR) + RIGHT + DOWN + RIGHT + DOWN + LEFT,
            piece_wukong.get_corner(UR) + RIGHT + DOWN + RIGHT + DOWN + LEFT + DOWN,
            piece_wukong.get_corner(UR) + RIGHT + DOWN + RIGHT + DOWN + LEFT + DOWN + LEFT,
            piece_wukong.get_corner(UR) + RIGHT + DOWN + RIGHT + DOWN + LEFT + DOWN + LEFT + UP,
            piece_wukong.get_corner(UR) + RIGHT + DOWN + RIGHT + DOWN + LEFT + DOWN + LEFT + UP + LEFT,
            piece_wukong.get_corner(UR) + RIGHT + DOWN + RIGHT + DOWN + LEFT + DOWN + LEFT + UP + LEFT + UP,
            piece_wukong.get_corner(UR) + RIGHT + DOWN + RIGHT + DOWN + LEFT + DOWN + LEFT + UP + LEFT + UP + RIGHT,
        ]

        box = Polygon(*zhengjin_position_list, color=GOLD_A, fill_opacity=1)
        text = Text('真经', font_size=48).move_to(box.get_center())
        piece_zhengjin = VGroup().add(box, text)

        # Add the game pieces to the scene
        self.play(Create(piece_shaseng), Create(piece_wukong), Create(piece_bajie), Create(piece_zhengjin), Create(piece_tangseng), 
                 Create(piece_baima), Create(piece_gui), Create(piece_mo), Create(piece_guai), Create(piece_jing), Create(piece_ling), Create(piece_yao))
        
        #self.play(ApplyFunction(shift_down, piece_jing))

        piece_map = {
            '0': piece_zhengjin,
            '1': piece_tangseng,
            '2': piece_wukong,
            '3': piece_bajie,
            '4': piece_shaseng,
            '5': piece_baima,
            '6': piece_gui,
            '7': piece_guai,
            '8': piece_ling,
            '9': piece_jing,
            '10': piece_mo,
            '11': piece_yao
        }

        direction_map ={
            'up': shift_up,
            'right': shift_right,
            'down': shift_down,
            'left': shift_left
        }

        move_list = produce_moving_list()
        #self.play(*[ApplyMethod(piece_map[move[0]].shift, direction_map[move[1]](piece_map[move[0]])) for move in move_list], run_time=0.5)


        for move in move_list:
            direction = direction_map[move[1]]
            piece = piece_map[move[0]]
            self.play(ApplyFunction(direction, piece), run_time=0.3)