from textblob import TextBlob
text = "The studnt is lerning pyhton and writting a progrm."
print("Original Text:")
print(text)
blob = TextBlob(text)
corrected = blob.correct()
print("\nCorrected Text:")
print(corrected)
