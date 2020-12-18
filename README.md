# Project4---Back
This code is the backend server/database for my last GASEI Project myMonthlies.  Written in Python, Flask, and PostgreSQL, and deployed on heroku utilizing gunicorn for the server.

# Goals
The goal with this project was to attempt to write a backend in a completely new language.  Up until this point in the cohort, all my code had been Javascript based languages.  With this one, I wanted to serve up a backend in Python.

# Troubles
Unfortunately, this project hit a lot of troubles for me.  Since I had little experience prior to this project writing in Python, I was limited in my time to a lot of research and testing.  As a result, I encountered exceptionally more hurdles than in previous projects.

The first main issue was incorporating a new technology.  I had initially wanted to do Django in place of Flask, althought I postponed learning Django due to the comlexity of the language vs the size of the app in question.  Next came a few days re-learning basic Flask before writing my basic foundational code.  I incorporated a base app.py, with a models file, and two route files, one for users, and one for budget items.  Everything ran fine locally on my virtual environment, but the next big hurdle for the backend came when deploying to Heroku.  While the code was working locally, I kept getting 500 Internal Server Error codes, and working through the domino effect to resolve the issues eventually ate up too much time.  

The server is live on heroku now.

https://afternoon-savannah-51133.herokuapp.com/ Live Server Backend
