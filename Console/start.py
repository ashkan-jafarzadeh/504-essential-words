from Helpers.UserInput import UserInput
from Console.Study.Exam import Exam
from Console.Study.Learning import Learning
from Console.Study.Review import Review

mode = UserInput.choice("Choose the mode", ["learning", "exam", "quick cap"])

if mode == "exam":
    exam = Exam()
    exam.start()

if mode == "learning":
    learning = Learning()
    learning.start()

if mode == "quick cap":
    learning = Review()
    learning.start()
