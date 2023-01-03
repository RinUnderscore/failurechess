# Create Board on Console
def CreateConsoleBoard():
    global console_board
    console_board = []
    for a in range(63):
        console_board.append(" ")

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
