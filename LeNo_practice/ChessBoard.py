


class ChessBoard(object):


    class Pieces (object):

        def __init__(self,piece,color):
            self.piece=piece
            self.color=color

        def __str__(self):

            pieces=["-","p","k","b","r","Q","K"]

            return pieces[self.piece]

    class Position(object):

        def __init__(self, row, column, piece):
            self.row = row
            self.column = column
            self.piece = piece


    def __init__(self):

        self.whitePieces=[]
        self.blackPieces=[]
        self.positions=[]

        self.init_pieces()
        self.init_positions()

    def init_pieces(self):
        #pieces=[rook,knight,bishop,queen,king]

        pieces = [4, 2, 3, 5, 6]

        pieceIndx = 0
        for count in range(0, 8):
            self.whitePieces.append(self.Pieces(pieces[pieceIndx], "white"))
            self.whitePieces.append(self.Pieces(1, "white"))

            self.blackPieces.append(self.Pieces(pieces[pieceIndx], "black"))
            self.blackPieces.append(self.Pieces(1, "black"))

            if count == 4:
                pieceIndx = 2

            if count < 4:
                pieceIndx += 1

            elif count > 4:
                pieceIndx -= 1


    def init_positions(self):

        row=["1","2","3","4","5","6","7","8"]
        column=["A","B","C","D","E","F","G","H"]

        for r in row:
            if r == "1" or r == "8":
                piecesIndx=0
            elif r == "2" or r == "7":
                piecesIndx=1
            else:
                piecesIndx=-1

            for c in column:

                if piecesIndx == -1:
                    #Empty position
                    self.positions.append(self.Position(r,c,"E"))
                else:
                    self.positions.append(self.Position(r, c, self.whitePieces[piecesIndx]))
                    piecesIndx+=2


    def __str__(self):

        board="-  A B C D E F G H\n"

        index=1
        for position in self.positions:

            if position.column == "A":
                board+=str(index)+"|"

            board+=" "+position.piece.__str__()

            if position.column == "H":
                index+=1
                board+="\n"

        return board




a=ChessBoard()

print(a)
