import tweetnlp

model = tweetnlp.load('sentiment')
model.sentiment("How many more days until opening day? 😩")
                    