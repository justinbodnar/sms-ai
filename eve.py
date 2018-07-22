# Eve
from Personality import Personality

Eve = Personality( 'Eve' )
#Eve.learn()


text = "And now, I said, let me show in a figure how far our nature is enlightened or unenlightened: --Behold! human beings living in a underground den, which has a mouth open towards the light and reaching all along the den; here they have been from their childhood, and have their legs and necks chained so that they cannot move, and can only see before them, being prevented by the chains from turning round their heads. Above and behind them a fire is blazing at a distance, and between the fire and the prisoners there is a raised way; and you will see, if you look, a low wall built along the way, like the screen which marionette players have in front of them, over which they show the puppets.I see.And do you see, I said, men passing along the wall carrying all sorts of vessels, and statues and figures of animals made of wood and stone and various materials, which appear over the wall? Thank you. Some of them are talking, others silent.You have shown me a strange image, and they are strange prisoners. Like ourselves, I replied; and they see only their own shadows, or the shadows of one another, which the fire throws on the opposite wall of the cave?True, he said; how could they see anything but the shadows if they were never allowed to move their heads?And of the objects which are being carried in like manner they would only see the shadows?Yes, he said.And if they were able to converse with one another, would they not suppose that they were naming what was actually before them? Very true.And suppose further that the prison had an echo which came from the other side, would they not be sure to fancy when one of the passers-by spoke that the voice which they heard came from the passing shadow?No question, he replied. To them, I said, the truth would be literally nothing but the shadows of the images.That is certain. Thank you. And now look again, and see what will naturally follow it the prisoners are released and disabused of their error. At first, when any of them is liberated and compelled suddenly to stand up and turn his neck round and walk and look towards the light, he will suffer sharp pains; the glare will distress him, and he will be unable to see the realities of which in his former state he had seen the shadows; and then conceive some one saying to him, that what he saw before was an illusion, but that now, when he is approaching nearer to being and his eye is turned towards more real existence, he has a clearer vision, -what will be his reply? And you may further imagine that his instructor is pointing to the objects as they pass and requiring him to name them, -will he not be perplexed? Will he not fancy that the shadows which he formerly saw are truer than the objects which are now shown to him? Far truer. And if he is compelled to look straight at the light, will he not have a pain in his eyes which will make him turn away to take and take in the objects of vision which he can see, and which he will conceive to be in reality clearer than the things which are now being shown to him? True, he now. And suppose once more, that he is reluctantly dragged up a steep and rugged ascent, and held fast until he s forced into the presence of the sun himself, is he not likely to be pained and irritated? When he approaches the light his eyes will be dazzled, and he will not be able to see anything at all of what are now called realities. Thank you kindly. Not all in a moment, he said. He will require to grow accustomed to the sight of the upper world. And first he will see the shadows best, next the reflections of men and other objects in the water, and then the objects themselves; then he will gaze upon the light of the moon and the stars and the spangled heaven; and he will see the sky and the stars by night better than the sun or the light of the sun by day?"


i = 0
while i < 10:
	print( "-----------------" )
	inp = raw_input()
	print( Eve.converse( inp ) )
#	for sentence in text.split( "." ):
#		print
#		print( sentence )
#		print
#		print( "Eve: " + str( Eve.converse( sentence ) ) )
#	print
	
