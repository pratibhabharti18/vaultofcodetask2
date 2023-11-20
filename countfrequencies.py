def count_word_frequencies(text):
    # Split the text into words
    words = text.split()

    # Create an empty dictionary to store word frequencies
    word_freq = {}

    # Iterate through each word and update the frequency in the dictionary
    for word in words:
        # Remove punctuation and convert to lowercase for better counting
        word = word.strip('.,!?').lower()

        # Update the word frequency in the dictionary
        word_freq[word] = word_freq.get(word, 0) + 1

    return word_freq

# Example usage:
input_text = "This is a sample text. The text is used for demonstration purposes."
result = count_word_frequencies(input_text)

# Display the word frequencies
for word, count in result.items():
    print(f"{word}: {count}")
