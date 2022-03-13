from answerFactory import answers

# Выбор алгоритма для теста:
# from answerRegocnitionA import recognizeAnswer
# from answerRecognitionB import recognizeAnswer
# from answerRecognitionC import recognizeAnswer
from answerRecognitionD import recognizeAnswer

print("")
print("Вопрос-ответ. Чтобы остановить программу введите команду '/stop'.")

while True:
    print("")
    i = str(input("Введите вопрос или команду:"))

    if i == "/stop":
        break

    answer = recognizeAnswer(i, answers)

    if answer == None:
        print("// Ответ на данный вопрос не найден!")
    else:
        print("//", answer.toString())