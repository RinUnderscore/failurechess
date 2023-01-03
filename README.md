# Video Script
Hello everyone, i’ve decided to torture myself by coding this chess game. By no means I’m good at chess [fool's mate], but I’m done with doing backend and stuff so I’m going to use high performance languages and a game engine to help me code this game. [challenge to code in python]

I wished I could have done this in C++ and Unity, but it seems I should learn some thing’s as well. Let’s get this chessboard working in the console first. I have limited working projects in my new github, which mostly has me learning python syntax but I’m still annoyed by the lack of semicolons…

[Use codesnippet type out void CreateBoard(){} and then delete and show] Other than the terrible syntax issues, it wasn't too difficult to code this simple task.
```
# Create Board on Console
def CreateConsoleBoard():
    console_board = []
    for a in range(63):
        console_board.append("")
    print(len(console_board)) # Remove After Test

if __name__ == "__main__":
    CreateConsoleBoard()
```

Next, I decided it was (prob) easier to code moves into FEN style and letting the system show and display FEN. I tried to code an FEN reader to import into this ```console_board``` array.

