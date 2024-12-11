# SMS-AI

A chatbot written by [Justin Bodnar](https://justinbodnar.com) that receives and responds to SMS messages from any phone number using Google Voice API. Written during my time as an undergraduate student, this project predates the widespread adoption of modern AI tools like ChatGPT. While it showcases early experimentation with AI-driven conversations, it is now largely defunct, serving as a reminder of how far technology has come.

The bot leverages a custom `Personality` class built on ChatterBot and TensorFlow to provide conversational responses based on learned data.

---

## Features

- **Automated SMS Responses**:
	- Responds to incoming messages automatically via Google Voice.
	- Uses a custom AI personality for conversational replies.
  
- **Custom Personality Framework**:
	- `Personality` class implements a conversation model with the ability to learn, respond, and export learned data.

- **Logging and Deduplication**:
	- Prevents duplicate responses by hashing and storing message metadata.
	- Skips messages sent by the bot itself.

---

## Setup Instructions

### 1. Configure Google Voice API
- Place your Google Voice credentials in the `ai-sms-bot.exp` script.
- Example credentials:
	```plaintext
	GOOGLE_VOICE_EMAIL_ADDRESS
	GOOGLE_VOICE_PASSWORD
	```

### 2. Train the AI Personality
- To train the neural net for the first time:
	```bash
	/usr/bin/expect -f ai-sms-bot.exp
	```
- After the initial run, comment out the `learn` line in the main script:
	```python
	Andrew.learn()
	```

### 3. Automate with Cronjob
- Schedule the script to run periodically using cron:
	```bash
	/usr/bin/expect -f /path/to/ai-sms-bot.exp
	```

---

## File Structure and Key Components

### `Personality` Class
A custom Python class to define conversational AI personalities.

**Features**:
- **Learning**: Trains on ChatterBot's English corpus.
- **Conversation**: Generates responses to input messages.
- **Exporting Data**: Saves learned data for later use.

### `ai-sms-bot.exp`
Handles the Google Voice API login process.

**Steps**:
1. Launches the `ai-sms-bot.py` script.
2. Automatically inputs Google Voice credentials.
3. Ensures a seamless connection to the Google Voice service.

### `ai-sms-bot.py`
The main script for SMS handling.

**Functions**:
- **`extractsms()`**: Parses SMS messages from Google Voice HTML.
- **`main()`**: Orchestrates the SMS response workflow, including:
	- Message deduplication.
	- Generating responses with the `Personality` class.
	- Sending SMS replies.

---

## Example Workflow

1. **Incoming SMS**:
	- Google Voice retrieves a new message.
	- The bot hashes the message for uniqueness and logs it.

2. **Processing**:
	- The bot checks if the message is from the user or is a duplicate.
	- If valid, the bot generates a response using the AI personality.

3. **Reply**:
	- The bot sends the response back to the sender via Google Voice.

4. **Cleanup**:
	- Processed messages are logged, and duplicates are skipped in future runs.

---

## Example Cronjob
To ensure the bot runs periodically, set up a cronjob:
```plaintext
*/5 * * * * /usr/bin/expect -f /path/to/ai-sms-bot.exp
