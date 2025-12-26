def hangman(word):
    wrong = 0
    stages = ["",
              "_____     ",
              "|         ",
              "|    |    ",
              "|    O    ",
              "|   /|\   ",
              "|   / \   ",
              "|         "]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Добро пожаловать на казнь!")