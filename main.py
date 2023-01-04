import pygame, os, time, random

# Create Board on Console
def GenerateConsoleBoard():
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
        print(f"My FEN: {FEN}")
        
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
        # print(f"\n FENPROCESS = {FEN_process}")
        
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
    GenerateConsoleBoard()
    
    # Create and Read FEN
    current_FEN = FEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
    current_FEN.FEN_to_BOARD(current_FEN.reader(current_FEN.FEN))

