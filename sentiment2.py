from textblob import TextBlob

texts = [
   "i have stomach pain",
   "The book is on the table", "I love cake so much", "I am happy right now", 
   "this is the worst experince i have ever had",
   "I love reading",
"I am feeling bad today"
]

for text in texts:
    try:
        text = str(text)
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity

        if polarity > 0:
            sentiment = "Positive"
        elif polarity < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        print(f"Text: '{text}' -> {'Positive' if polarity>0 else 'Negative' if polarity<0 else 'Neutral'} (Polarity: {polarity})")

    except Exception as e:
        print(f"Error analyzing text '{text}': {e}")
