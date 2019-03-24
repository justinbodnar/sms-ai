####################
# AI SMS Bot       #
# by Justin Bodnar #
####################

from Personality import Personality
from googlevoice import Voice
import sys
import BeautifulSoup
import hashlib

#######################
# extractsms function #
#######################
def extractsms(htmlsms) :

	msgitems = []										# accum message items here
	#	Extract all conversations by searching for a DIV with an ID at top level.
	tree = BeautifulSoup.BeautifulSoup(htmlsms)			# parse HTML into tree
	conversations = tree.findAll("div",attrs={"id" : True},recursive=False)
	for conversation in conversations :
		#	For each conversation, extract each row, which is one SMS message.
		rows = conversation.findAll(attrs={"class" : "gc-message-sms-row"})
		for row in rows :								# for all rows
		#	For each row, which is one message, extract all the fields.
			msgitem = {"id" : conversation["id"]}		# tag this message with conversation ID
			spans = row.findAll("span",attrs={"class" : True}, recursive=False)
			for span in spans :							# for all spans in row
				cl = span["class"].replace('gc-message-sms-', '')
				msgitem[cl] = (" ".join(span.findAll(text=True))).strip()	# put text in dict
			msgitems.append(msgitem)					# add msg dictionary to list
	return msgitems

#################
# main function #
#################
def main():

	# wake up andrew
	Andrew = Personality( "andrew" )
	Andrew.learn()

	# set verbosity flag for debugging purposes
	verbose = True

	# get logfile
	records = "/rec.db"
	logfile = "/log.db"

	# instantiate gvoice object
	voice = Voice()
	voice.login()

	# grab the SMS messages
	voice.sms()

	# loop through messages
	for msg in extractsms(voice.sms.html):
		print
		print( msg )
		hash = hashlib.md5()
		hash.update( msg['text']+msg['time'] )
		key = hash.hexdigest()
		print( "Unique hash: " + key )
		# check if this is in log file
		duplicate = False
		f = open(logfile, "a+")
		for line in f:
			if key in line:
				duplicate = True
		if verbose:
			print( "Duplicate: " + str( duplicate ) )

		# if this is a duplicate, continue
		if duplicate:
			f.close()
			continue

		# if its FROM me, continue
		if "Me" in msg['from']:
			print( "Skipping messages from me." )
			f.close()
			continue

		# else add to log
		else:
			e = open( records, "a+" )
			e.write( "\n" )
			e.write( str( msg ) )
			e.write( "\n" )
			f.write( key + "-" )
			f.close()

		# print convo
		text = msg['text']
		if verbose:
			print( msg['from'] + ": \"" + text + "\"" )

		response = Andrew.converse( text )
		if verbose:
			print( "Andrew: " + str( response ) )
			e.write( str( response ) + "\n" )
		try:
			# send response SMS
			voice.send_sms( msg['from'], str( response ) )
		except Exception as e:
			print( e )

	for message in voice.sms().messages:
		message.delete()

#############
# call main #
#############
main()
