import re

def strip_non_english_chars(text):
    # Use regular expression pattern to match only English characters
    pattern = re.compile('[^a-zA-Z]')
    
    # Use the pattern to replace non-English characters with an empty string
    stripped_text = re.sub(pattern, '', text)
    
    return stripped_text

# Example usage
# text = "Hello, 你好, Bonjour!"
# stripped_text = strip_non_english_chars(text)
# print(stripped_text)  # Output: "HelloBonjour"

with open('list.txt', encoding='utf-8') as f:
    with open('out.txt', 'w') as fout:
        lines = f.readlines()
        for line in lines:
            # if empty line, skip
            stripped_text = strip_non_english_chars(line)
            if stripped_text == '':
                continue
            fout.write(stripped_text+',')