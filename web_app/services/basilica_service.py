# web_app/services/basilica_services.py

import basilica

import os

from dotenv import load_dotenv

load_dotenv() # parese the .env file for environment variables

BASILICA_API_KEY = os.getenv("BASILICA_API_KEY")

connection = basilica.Connection(BASILICA_API_KEY)
print(type(connection))

if __name__ == "__main__":
    
    sentences = ["Hello world!", "How are you?"]
    embeddings = connection.embed_sentences(sentences)
    print(list(embeddings))
