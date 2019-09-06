from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

trained_bot = ChatBot(name='Jenga Score Bot', read_only=True,

                      logic_adapters=['chatterbot.logic.BestMatch','chatterbot.logic.MathematicalEvaluation'])
trainer = ChatterBotCorpusTrainer(trained_bot)

#Training the bot English and the additional credit score corpus
#'chatterbot.corpus.english.creditscore

training_data = ['chatterbot.corpus.english']


#This section is commented out because the bot has already been trained
#for item in(training_data):
#   trainer.train(item)
#train bot on credit scores
trainer =ListTrainer(trained_bot)
trainer.train([
    'What is Credit Reference Bureau ?',
    ' A credit reference bureau (CRB) is a firm that collects information from financial institutions and provides consumer credit information on individual consumers for a variety of uses. CRB’s hold credit data shared by financial institutions and facilitates credit lending to financial institutions.',
    'What can you do to improve your credit history?',
    'Check Your Credit Report and Fix errors ,Pay your bills on time and Setup Payment Reminders',
    'Other tips?',
    '1. Don’t close old credit accounts. 2. Avoid negative listings. 3. Maintain an active credit account. 4. Build a credit history. 5. Create a budget. 6. Click the PataScore Button and get the other tips'
])

