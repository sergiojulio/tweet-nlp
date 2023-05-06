import tweetnlp

model = tweetnlp.load('sentiment')
model.sentiment("How many days will it take to land 😩")
                    