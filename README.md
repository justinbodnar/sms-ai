# AI SMS Bot

A chatbot based on TensorFlow that recieves and responds to messages through Google Voice API.


# Setup

Put Google credentials in ai-sms-bot.exp script.

To train the neural net for the first time, run:

/usr/bin/expect -f ai-sms-bot.exp

After initial run, comment out the line in main:

Andrew.learn()

Now you can set the script on a cronjob and any SMS sent to the phone number will get a response when the cronjob runs.

* * * * * /usr/bin/expect -f /path/to/ai-sms-bot.exp
