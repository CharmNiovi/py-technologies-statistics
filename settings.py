import sqlite3
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline


# DB settings and migrations
DB = sqlite3.connect("vacancies.db")
with open('migrations.sql', 'r') as sql_file:
    sql_file = sql_file.read()
for command in sql_file.split(';'):
    DB.execute(command)


# AI Transformer model settings
TOKENIZER = AutoTokenizer.from_pretrained("Jean-Baptiste/camembert-ner-with-dates")
AI_MODEL = AutoModelForTokenClassification.from_pretrained("Jean-Baptiste/camembert-ner-with-dates")

nlp = pipeline('ner', model=AI_MODEL, tokenizer=TOKENIZER, aggregation_strategy="simple")