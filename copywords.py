def main():
    words = []
    # opens the file with all the words and puts it in an array
    f = open("words.txt", "r")
    for line in f:
        words.append(line[:-1])
    f.close
    l = []
    for i in words:
        if i not in l:
            l.append(i)

    textfile = open("wordList.txt", 'w')
    for word in l:
        textfile.write(word + '\n')
    textfile.close()


main()
