# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open("./story.txt", "r") as f:
        contents = f.read()
        print(contents)
        return contents
read_file_content(open("./story.txt"))

def count_words():
    text = read_file_content("./story.txt")
    
    # [assignment] Add your code here
    lines = []
    with open('./story.txt') as f:
        lines = f.readlines()
        lines = []
        count = 0
        for line in lines:
            count += 1
            print(f'line {count}: {line}')    

    return {"as": 10, "would": 20}
