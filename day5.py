import string
import json

def read_file (filepath):
    try :   
        with open (filepath,"r",encoding ="utf-8") as f:
            return f.read() 
    except FileNotFoundError:
        print ("error - file not found")
        return None

text = read_file("sample.txt")
if text :
    words = text.split() # splits on whitespace by default



def clean_words(words):
    cleaned = []
    for word in words:
        # Remove punctuation and convert to lowercase
        word = word.lower()
        word = word.strip(string.punctuation).lower() #remove leading or trailing punctuation
        if word:  # Only add non-empty words
            cleaned.append(word)
    return cleaned



def count_words(words):
    counts = {}
    for word in words : 
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts



#here we are finding the most common words n
def top_words(word_counts,n=10):
    sorted_words = sorted(word_counts.items(), key = lambda item: item[1],reverse = True)
    return sorted_words[:n]



def save_results(word_counts, top_n,output_path = "word_count_results.json"):
    result = {
        "total unique_words": len(word_counts),
        "total_words": sum(word_counts.values()),
        "top_words": [{"word": word, "count": count} for word, count in top_n]   
    }

    with open(output_path, "w") as f:
        json.dump(result, f,indent=4)

    print(f"Results saved to {output_path}")

def main():
    text = read_file("sample.txt")
    if text:
        words = text.split()
        cleaned_words = clean_words(words)
        word_counts = count_words(cleaned_words)
        top_10 = top_words(word_counts, n=10)
        save_results(word_counts, top_10)

if __name__ == "__main__":
    main()



