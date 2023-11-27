import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**kwargs) -> None:
        self.contents=[]
        for color , count in kwargs.items():
            self.contents.extend([color]*count)
    def draw(self,arg):
        if(arg > len(self.contents)):
            drawn_ball=[]
            drawn_ball=self.contents
            self.contents=[]
            return drawn_ball
        else:
            drawn_balls =random.sample(self.contents,arg)
            for i in drawn_balls:
                self.contents.remove(i)
            return drawn_balls
def experiment(
    hat: object, expected_balls: dict,
    num_balls_drawn: int, num_experiments: int
) -> float:
    """
    Returns the probability of how many times the balls indicated
    were drawn from the hat (number of successes / number of
    times run). Creates a deep copy to avoid reading the same
    data (list of balls).
    """

    success = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)

        drawn_balls = hat_copy.draw(num_balls_drawn)
        keep = True  # False if there are not enough values
        for key, value in expected_balls.items():
            if drawn_balls.count(key) < value:
                keep = False

        if keep:
            success += 1

    return success / num_experiments

hat = Hat(red=4, green=3, blue=5)
expected_balls = {"red": 2, "green": 1}
num_balls_drawn = 5
num_experiments = 2000

probability = experiment(hat, expected_balls, num_balls_drawn, num_experiments)
print("Estimated probability:", probability)