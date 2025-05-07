from collections import Counter

def count_word_frequency(filename):
    # Open the file and read all text
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read().lower().split()  # convert to lowercase & split into words

    # Use Counter to count how many times each word appears
    freq = Counter(text)

    # Print the results in a readable format
    print("Word frequencies:")
    for word, count in freq.items():
        print(f"  {word}: {count}")

if __name__ == "__main__":
    # Call the function on our sample file
    count_word_frequency("sample.txt")
