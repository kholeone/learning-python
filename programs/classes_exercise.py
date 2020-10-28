class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age 
        
    class_ = "student"

    def test_scores(self, score_1, score_2, score_3):
        score_total = score_1 + score_2 + score_3
        score_average = score_total / 3
        return score_average

Keisuke = Student("Keisuke", 22)

print(Keisuke.class_)
print(Keisuke.test_scores(50,40,60))