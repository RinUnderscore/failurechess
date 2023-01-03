# Video Script
Hello everyone, i’ve decided to torture myself by coding this chess game. By no means I’m good at chess [fool's mate], but I’m done with doing backend and stuff so I’m going to use high performance languages and a game engine to help me code this game. [challenge to code in python]

I wished I could have done this in C++ and Unity, but it seems I should learn some thing’s as well. Let’s get this chessboard working in the console first. I have limited working projects in my new github, which mostly has me learning python syntax but I’m still annoyed by the lack of semicolons… Speaking of python syntax, other than looking up python syntax, I am NOT allowed to "stack-overflow" how to compelte certain tasks. This clause seems simple, but I think about all the projects I used "stack-overflow" for.

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

Next, I decided it was (prob) easier to code moves into FEN style and letting the system show and display FEN. I tried to code an FEN reader to import into this ```console_board``` array. To be fair, python classes are way to finicky for my liking, but I finally got something to (barely) work:
```
class FEN:
    def __init__(self, FEN):
        self.FEN = FEN
    def reader(self,FEN):
        global console_board
        
        FEN = FEN.split("/", 7)
        print(f"My FEN: {FEN}\n\n")
        
        FEN_process = []
        SPACE_process = []
        for b in range(len(FEN)):
            try: FEN[b] = int(FEN[b])
            except ValueError: FEN[b] = str(FEN[b])
            if isinstance(FEN[b], str):
                FEN_process.append(list(FEN[b]))
            if isinstance(FEN[b], int):
                print(f"number of spaces: {FEN[b]}")
                for c in range(FEN[b]+4):
                    SPACE_process.append(" ")
                    if len(SPACE_process) == 8:
                        SPACE_process = []
                        FEN_process.append(SPACE_process)
                    print(SPACE_process)
        
        del FEN_process[7]
        del FEN_process[6]
        print(f"\n\n\n\n\n\n FENPROCESS = {FEN_process}")
        
        return FEN_process
        
    def FEN_to_BOARD(self, newFEN):
        console_board = []
        for e in range(8):
            for f in range(8):
                console_board.append(newFEN[e][f])
        print(f"list of my board: {console_board}, length = {len(console_board)}")

if __name__ == "__main__":
    CreateConsoleBoard()
    
    current_FEN = FEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
    current_FEN.FEN_to_BOARD(current_FEN.reader(current_FEN.FEN))
```
~~~ RANT START ~~~
This was 2 hours that I spent fixing bugs because I don't know how to code... Like how do I get this: 
```FENPROCESS = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'], ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [], ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]```
and
``` FENPROCESS = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'], ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]```

THESE ERRORS DON'T EVEN MAKE SENSE AND I THOUGHT THE PROBLEMS WOULD BE IN THE UI AND UX :<
~~~ RANT END ~~~

And in Classic Rin Fassion I Cheesed my way through the right answer. I suppose there is an correct way to figure this out, but I've already looked at this mess for a few hours, I'm going to leave that as an problem for future me.

Why does this code look so complicated but simple. *cries* why cant my code be as clean as Sebastian Lague...

I suppose it does help to comment your code.

```# Create Board on Console
def CreateConsoleBoard():
    global console_board
    console_board = []
    for a in range(63):
        console_board.append(" ")

class FEN:
    def __init__(self, FEN):
        self.FEN = FEN
    
    # Create FEN Reader
    def reader(self,FEN):
        global console_board
        
        # Split FEN into 8 String
        FEN = FEN.split("/", 7)
        print(f"My FEN: {FEN}\n\n")
        
        FEN_process = []
        SPACE_process = []

        # Seporate String into Char
        for b in range(len(FEN)):
            # if FEN is str, return Char, if FEN is int, return str int
            try: FEN[b] = int(FEN[b])
            except ValueError: FEN[b] = str(FEN[b])

            # if FEN is Char, add char to processor
            if isinstance(FEN[b], str):
                FEN_process.append(list(FEN[b]))
            
            # if FEN is int, add 8 spaces to 5 lines
            if isinstance(FEN[b], int):
                print(f"number of spaces: {FEN[b]}")
                for c in range(FEN[b]+4):
                    SPACE_process.append(" ")
                    if len(SPACE_process) == 8:
                        SPACE_process = []
                        FEN_process.append(SPACE_process)
                    # print(SPACE_process) # Keep for Debug Purposes
        
        # Removes Broken Lines (cheese method)
        del FEN_process[7]
        del FEN_process[6]

        # Return Debug Failsafe
        print(f"\n\n\n\n\n\n FENPROCESS = {FEN_process}")
        
        return FEN_process
        
    def FEN_to_BOARD(self, newFEN):
        console_board = []
        # Add processor to board
        for e in range(8):
            for f in range(8):
                console_board.append(newFEN[e][f])

        # Return Debug Failsave
        print(f"list of my board: {console_board}, length = {len(console_board)}")

if __name__ == "__main__":
    CreateConsoleBoard()
    
    # Create and Read FEN
    current_FEN = FEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
    current_FEN.FEN_to_BOARD(current_FEN.reader(current_FEN.FEN))
```

This looks much better to read now.
