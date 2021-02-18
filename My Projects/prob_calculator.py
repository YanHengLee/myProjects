import random
import copy


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        # appending self.contents list with strings of colors
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, num_of_ball):
        removed_balls = []
        # if the amount of balls in the hat is lesser than num_of_ball return the whole list of ball
        if num_of_ball > len(self.contents):
            return self.contents
        # if not randomly draw out n number of balls
        for i in range(num_of_ball):
            choice = random.choice(self.contents)
            self.contents.remove(choice)
            removed_balls.append(choice)
        return removed_balls # returns the balls that has been drawn out


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    probability = 0
    # main loop
    for i in range(num_experiments):
        # copying the functions of class Hat
        hat_copy = copy.deepcopy(hat)

        # use the draw method(from Hat class) to draw out the balls
        balls_drawn = hat_copy.draw(num_balls_drawn)

        random_dict = {}
        # append the balls and the amount of same color balls that have been drawn to a dictionary
        for key in balls_drawn:
            value = balls_drawn.count(key)
            random_dict[key] = value

        same_count = 0
        result = True
        # compare the drawn out balls to the expected result
        for key, value in expected_balls.items():
            if key not in random_dict or random_dict[key] < expected_balls[key]:
                result = False
                break
        # if it's the same as expected results
        if result:
            same_count += 1

        # counting the probability of getting the expected results
        probability += same_count / num_experiments
    output = f"{probability:.3f}"

    return float(output)
