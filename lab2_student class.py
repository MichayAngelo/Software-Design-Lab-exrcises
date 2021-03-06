class Student(object):
 #Represents a student.

    def __init__(self, name, number):
     #Constructor creates a Student with the given name and number of scores and sets all scores to 0.
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
         #Returns the student's name.
        return self.name

    def setScore(self, i, score):
         #Resets the ith score, counting from 1.
        self.scores[i - 1] = score

    def getScore(self, i):
         #Returns the ith score, counting from 1.
        return self.scores[i - 1]

    def getAverage(self):
        #Returns the average score.
        return sum(self.scores) / len(self.scores)

    def getHighScore(self):
        #Returns the highest score.
        return max(self.scores)

    def __str__(self):
        #Returns the string representation of the student.
        return "Name: " + self.name + "\nScores: " + \
            " ".join(map(str, self.scores))


s = Student("Maria", 5)
print(s)
print()
s.setScore(1, 100)
print(s)
s.getHighScore()
print("HighScore:", s.getHighScore())
s.getAverage()
print("AverageScore:", s.getAverage())
s.getScore(1)
print("Score:", s.getScore(1))
s.getName()
print("Name:", s.getName())