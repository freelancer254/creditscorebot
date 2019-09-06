Author:
Robert Mutua

Framework:
django>=2.2,<2.3
# 

Imports:
chatterbot>=0.8,<1.1

chatterbot-corpus 1.2.0

IDE:
Pycharm 2017.1.3
Cmder CLI

Programming Language:
Python 3.7.4

Training Data:
     'What is Credit Reference Bureau ?',
    ' A credit reference bureau (CRB) is a firm that collects information from financial institutions 
      and provides consumer credit information on individual consumers for a variety of uses. 
      CRB’s hold credit data shared by financial institutions and facilitates credit lending to financial institutions.',
    'What can you do to improve your credit history?',
    'Check Your Credit Report and Fix errors ,Pay your bills on time and Setup Payment Reminders',
    'Other tips?',
    '1. Don’t close old credit accounts. 2. Avoid negative listings. 3. Maintain an active credit account.
     4. Build a credit history. 5. Create a budget. 6. Click the PataScore Button and get the other tips'

Challenges:
There are dependency issues with the modules, a downgrading is required. Chatterbot-corpus is compactible with PyYAML 3.13.
The chatterbotCorpusTrainer wasnt able to train the bot on my custom corpus, therefore, I had to use a list trainer explicitly.

Future Extensions:
1. Addition of a larger corpus and hence enhanced training of the bot
2. Proper exception handling and logging
3. Proper front end presentation

Deliverable:
A MVP chatbot that gives users tips on improving their credit score. The chatbot has been developed the django-way(MVT)
Attached is the zip file with the source-code.

Resources:
1. https://www.tutorialdocs.com/tutorial/chatterbot/django-integration.html
2. https://readthedocs.org/projects/chatterbot/
For Efficient Debugging, refer to:
1.https://github.com/gunthercox/ChatterBot
The training data has been obtained from:
1.https://ke.creditinfo.com/faq/
2.https://www.finder.com/improve-your-credit-score