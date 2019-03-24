#####################
# Personality class #
# by Justin Bodnar  #
#####################
#
# A class to implement a conversation 'personality.'
# Based on chatterbot, and TenserFlow Neural Network.
#

from chatterbot import ChatBot
import os

#####################
# personality class #
#####################
class Personality:

	###############
	# constructor #
	###############
	#
	# takes name as input
	#
	def __init__(self, name):
		self.name = name
		self.brain = ChatBot(
		name,
		trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
		)

	##################
	# sleep function #
	##################
	#
	# exports all learned data which is relearned when this personality is woken up
	#
	def sleep(self):
		try:
			self.brain.trainer.export_for_training( './population/' + self.name + '.json' )
		except Exception as e:
			print( "Error! " + self.name + " cant sleep!" )
			print( e )

	#####################
	# converse function #
	#####################
	#
	# takes an input message string, and returns a response string
	#
	def converse( self, message ):
		return self.brain.get_response( str(message) )

	##################
	# learn function #
	##################
	#
	# takes no input, learns using a default chatterbot corpus
	#
	def learn(self):
		self.brain.train("chatterbot.corpus.english.greetings")

	####################
	# isEmpty function #
	####################
	#
	# checks for brain damage
	#
	def isEmpty(self):
		return self.items == []
