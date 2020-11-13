#!/usr/bin/python


def extract_move(s):
	if '.' in s:       #s not clean move, extract the move (the suffix after the dot)
		n,move=s.split(".",1)
		return move
	else:            #s is clean move
		return s

def translate_move(s):
	if s == "O-O":
		return "castle king side"
	if s == "O-O-O":
		return "castle queen side"
	if len(s) == 2:   #e5 format
		return s
	if ( 'x' in s and '+' in s):       #a capture and check move : Qxd5+  , or Nbxd5+ 
		piece,rest = s.split("x",1)   
		square,rubish=rest.split("+",1)
		name_piece = translate_piece(piece)
		res = name_piece+" take "+square+" check"
		return res
	if ( 'x' in s ):                   # a capture move : Nxf5  or Bcxc4
	        piece,square = s.split("x",1)
		name_piece = translate_piece(piece)
		res = name_piece+" take "+square
		return res
	if  len(s) == 4:        #a move with position possible for 2 pieces :  Nbd4
		piece = s[0:2]
		square = s[2:4]
		name_piece = translate_piece(piece)
		res = name_piece+" "+square
		return res
	if  len(s) == 3:       # simple piece move :  Nd4
		piece = s[0]
		square = s[1:3]
		name_piece = translate_piece(piece)
		res = name_piece+" "+square
		return res

def translate_piece(s):
	if s not in "NQBKR": #then this is not a piece but just a pawn move
		return s
	res = ""
	if s[0] == 'N':
		res = 'Knight'
	if s[0] == 'Q':
		res = 'Queen'
	if s[0] == 'B':
		res = 'Bishop'
	if s[0] == 'K':
		res = 'King'
	if s[0] == 'R':
		res = 'Rook'
	if len(s) == 2:   # if form Bd  or Nc ...  (Bishop on d, or Knight on c)
		res = res+" "+s[1]
	return res

# Open a file
fo = open("game.txt", "rw+")
print "Name of the file: ", fo.name


line = fo.readline()
print "Read Line: %s" % (line)

db=line.split()

for x in db:
	print translate_move(extract_move(x))


# Close opend file
fo.close()
