import math
"""
Purpose: This code is passed in a file name and searches the immediate folder
for that file. When this file is found, it parses in its data line by line.
Each one of these lines are stored in an array for later use and passed out.
"""
def getLinesOfFile(file):
    f = open(file, "r")
    listOfLines = []
    for line in f:
        listOfLines.append(line)

    f.close()
    return listOfLines


"""
Purpose: This method separates the Blurbs and the Ratings from the list. The ratings
are appropriately shifted and then both of them are returned as items of a dictionary.
"""
def getReviewsAndBlurbs(listOfReviews):
    ratings = []
    blurb = []
    for review in listOfReviews:
        cleanedReview = review.lower().replace("\n","").replace("\t","")
        ratings.append(int(cleanedReview[:1])-2)
        blurb.append(cleanedReview[1:])

# blurb = purgeUnecessaryCharacters(reviews["blurb"])
    return ratings, blurb

"""
Purpose: This method is passed in a blurb of the of a review. Using this blurb,
it then splits up the blurb into the words and puts those split up words into an
array that is passed out.
"""
def getSeparateWords(blurbs):
    allBlurbWords = []

    for blurb in blurbs:
        blurbWords = []

        lastSpaceIndex = 0
        for i in range(len(blurb)):
            if blurb[i] == " ":
                blurbWords.append(blurb[lastSpaceIndex:i])
                lastSpaceIndex = i + 1
        allBlurbWords.append(blurbWords)

    return allBlurbWords


"""
Purpose: This method eliminates all the words that are unlikely to provide clarity
on whether or not a given film is good or bad based on the ratings. These words
are stored in a file that is read in. If any of the words in a line match these
banned words, they are removed. The words are kept as individual indexs on an
array of blurbs and then returned.
"""
def cleanBlurbWords(blurbs):
    bannedWords = getLinesOfFile("stopWords.txt")
    newTrimmedBlurbs = []
    for blurb in blurbs:

        cleanedBlurbWords = []
        for word in blurb:
            if word not in bannedWords:
                cleanedBlurbWords.append(word)

        newTrimmedBlurbs.append(cleanedBlurbWords)

    return newTrimmedBlurbs


"""
Purpose: This function tallys up the scores of all of the words. Words that appear
more in more highly rated movies will correspondingly receive higher scores. It
then outputs this list of scores as an unsorted dictionary of words and their
associated scores.
"""
def getUniqueWordsRating(blurbs, reviews):
    wordSum = {}
    wordNum = {}
    for i in range(len(blurbs)):
        for word in blurbs[i]:
            if word in wordSum: #TODO: better way???
                wordSum[word] += reviews[i]
            else:
                wordSum[word] = reviews[i] 

            if word in wordNum:
                wordNum[word] += 1
            else:
                wordNum[word] = 1

    wordRatings = {}
    for word in wordSum:
        wordRatings[word] = (wordSum[word]/wordNum[word])*math.log(wordNum[word])

    return wordRatings


"""
Purpose: It gets scores.
"""
def getScores(): 
    listOfReviews = getLinesOfFile("movieReviews.txt")
    reviews, blurbs = getReviewsAndBlurbs(listOfReviews)
    blurbWords = getSeparateWords(blurbs)
    cleanedBlurbWords = cleanBlurbWords(blurbWords)

    uniqueWordsRatings = getUniqueWordsRating(cleanedBlurbWords, reviews)

    return uniqueWordsRatings

"""
Purpose: It gets the highest score
"""
def getScoresFromHighestToLowest(uniqueWordsRatings):
    orderedWords = []

    for unorderedWord in uniqueWordsRatings:
        wordOrdered = False 

        for i in range(len(orderedWords)):
            orderedWord = orderedWords[i]

            if uniqueWordsRatings[unorderedWord] >= uniqueWordsRatings[orderedWord]:
                orderedWords.insert(i, unorderedWord)
                wordOrdered = True
                break

        if (not wordOrdered):
            orderedWords.append(unorderedWord)
  
    return orderedWords
    
"""
Purpose: This function receives a dictionary of words and their associated ratings.
Using the built in sort method, the function sorts the dictionary by the the value
that is associated with the word. Words with the highest values are sent to the top.
Words are then displayed by the top twenty and bottom twenty.
"""
def displayScores(uniqueWordsRatings):
    sortedWords = getScoresFromHighestToLowest(uniqueWordsRatings)

    print("Top 20")
    for i in range(21):
        print(f'{uniqueWordsRatings[sortedWords[i]]:.2f} {sortedWords[i]}')
   
    print("\nBottom 20")
    for i in range(-20, 0):
        print(f'{uniqueWordsRatings[sortedWords[i]]:.2f} {sortedWords[i]}')


def main():
    scores = getScores()
    displayScores(scores)

main()
