
reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone",
        "The product was average. Nothing extraordinary about it."]


keywords = ["good", "excellent", "bad", "poor", "average",]


# Task 1 
for review in reviews:
    word = review.split()
    if word in keywords: 
        word.upper()

# Task 2

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]

negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]


for review in reviews:
     word = review.split()
     if word in positive_words:
        pos = review.count(word)
     print(pos)


# Task 3 

for review in reviews:
    summary = review[:30]
    final = summary.append("...")
