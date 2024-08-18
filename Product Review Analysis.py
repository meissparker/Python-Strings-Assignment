
reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone",
        "The product was average. Nothing extraordinary about it."]


keywords = ["good", "excellent", "bad", "poor", "average"]


# Task 1 
def highlight():
    for review in reviews:
        word = review.split()
        if word in keywords: 
            print(word).upper()
        else: 
            print(word)

# Task 2

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]

negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def tally():
    for review in reviews:
        word = review.split()
        if word in positive_words:
            pos = word.count(word)
            print(f"There are {pos} positive words in the reviews.")
        elif word in negative_words:
            neg = word.count(word)
            print(f"There are {neg} negative words in the reviews.")


# Task 3 

def summary():
    for review in reviews:
        print(f"{review[:30]}...")
            

highlight()
tally()
summary()




