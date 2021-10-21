import random
import copy


class Hat:

    #hat1 = Hat(yellow=3, blue=2, green=6)
    #hat2 = Hat(red=5, orange=4)
    #hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

    def __init__(self, **kwargs):
        print(kwargs)
        self.contents = list()
        for k, v in kwargs.items():
            for i in range(v):
                self.contents.append(k)
        
        # print(self.contents)
    
        self.initial_contents = copy.copy(self.contents)
    
    def draw(self, number):
        self.number = number
        removed_list = list()
        removed_list_id = list()
        if self.number > 0:
            if self.number > len(self.contents): self.number = len(self.contents)
            # print (self.number)
            for i in range(self.number):
                rnd = random.randint(0, len(self.contents)-1)
                # print (rnd)
                removed_list_id.append(rnd)
                removed_list.append(self.contents[rnd])
                self.contents.pop(rnd)
                #return rnd
        
        # print(removed_list)
        # print(self.contents)
        
        if len(self.contents) == 0:
            self.contents = copy.copy(self.__initial_contents)
        
        return removed_list
    
    def reset(self):
        self.contents = copy.copy(self.initial_contents)

    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_count = 0
    
    for i in range(num_experiments):
        expected_balls_working_copy = copy.copy(expected_balls)
        hat.reset()
        returned_balls = hat.draw(num_balls_drawn)
        # print (returned_balls)
    
    for ball_color, ball_count in expected_balls.items():
        
        for i in range(ball_count):
            
            if ball_color in returned_balls:
                returned_balls.remove(ball_color)
                expected_balls_working_copy[ball_color] -= 1

    if sum(v for v in expected_balls_working_copy.values()) == 0:
        expected_count += 1

    probability = expected_count / num_experiments

    return probability
        
    

random.seed(95)

hat = Hat(blue=4, red=2, green=6)

probability = experiment(
    hat=hat,
    expected_balls={"blue": 2, "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)
