# Eve
from Personality import Personality

Eve = Personality( 'Eve' )
Eve.learn()

i = 0
while i < 10:
	print( "-----------------" )
	inp = raw_input()
	print( Eve.converse( inp ) )

	
