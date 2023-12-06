class Sets:
    def __init__(self, previous, kgs, reps, done, exercise_id):
        print("Set Object created\n")
        self.previous = previous
        self.kgs = kgs
        self.reps = reps
        self.done = done
        self.exercise_id = exercise_id

    def print(self):
        print("Previous is: " + str(self.previous) + "\n")
        print("Weight is: " + str(self.kgs) + "\n")
        print("Reps is: " + str(self.reps) + "\n")
        print("Done is: " + str(self.done) + "\n")
        print("Exercise ID is: " + str(self.exercise_id) + "\n")

    def __del__(self):
        print("Set object destroyed")


class Exercises:

    def __init__(self, exercise_id):
        self.exercise_id = exercise_id

    def __del__(self):
        print("Exercise object destroyed")


bench_press = Exercises(1)

new_set = Sets(False, 16, 8, True, 1)
new_set.print()
del new_set

