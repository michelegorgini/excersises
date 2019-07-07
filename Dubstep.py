# ourList = (1,3,4,5,7,9)
#
# result = filter((4).__ne__,ourList)
# dir(result)
#
# exit()

# Exercise: Dubstep

# song = 'AWUBBWUBC'
# def song_decoder(song):
#     print(song)
#     word = ''
#     listResult =[]
#     song_No_WUB = song.replace("WUB", "9")
#     wordList =[x for x in song_No_WUB ] # I create a list
#     for i in range (0, len(wordList)):
#         if wordList[i] != '9':
#             word += wordList[i]
#         else:
#             if word != '':
#                 listResult.append(word)
#                 word = ''
#             else:
#                 continue
#     if word != '':
#         listResult.append(word)
#     result =' '.join(map(str, listResult)) # I put the final resul from list to string
#     return(result)
# result =  song_decoder(song)
# print(result)

#Best Solution

# - 1
# def song_decoder(song):
#     return " ".join(song.replace('WUB', ' ').split())
#
# -2
# def song_decoder(song):
#     import re
#     return re.sub('(WUB)+', ' ', song).strip()
#
# -3
# def song_decoder(song):
#     return ' '.join(word for word in song.split('WUB') if word)

# -4
# def song_decoder(song):
#     """ Simple WUB decoder :) """
#
#     # Splitting strings by "WUBs" and filtering out voids
#     list = filter(lambda x: x != '', song.split('WUB'))
#
#     # Returning the joint items separed by spaces
#     return ' '.join(list)
#
# - 5
# song = 'AWUBWUBBWUBCE'
#
# # def song_decoder(song):
# noWub = song.split('WUB')
# print(noWub)
     #    return ' '.join(
     #     list(
     #         filter(
     #             ('').__ne__, song.split('WUB')
     #         )
     #     )
     # )
    # Steps:
    # 1. Remove occurences of WUB and get a list of words.
    # 2. Filter out empty space ''.
    # 3. Join the words in the list with space.
    # 4. Return






#
# print(song)
# word = ''
# listResult =[]
# song_No_WUB = song.replace("WUB", "9")
# wordList =[x for x in song_No_WUB ]
# print(wordList)
# print('='*20)
# for i in range (0, len(wordList)):
#     if wordList[i] != '9':
#         word += wordList[i]
#     else:
#         if word != '':
#             listResult.append(word)
#             word = ''
#         else:
#             continue
# if word != '':
#     listResult.append(word)
# result =' '.join(map(str, listResult))
# print(listResult)
# print(result)





# if song_No_WUB[0] = '9' or song_No_WUB[len(song_No_WUB)-1] = '9':
#     re
# word = v for x, v in enumerate (song_No_WUB) if song_No_WUB[x] != '9'
# for i in range (0, (len(song_No_WUB))):
#     if song_No_WUB[i] != "9" :
#         word += song_No_WUB[i]
#     else:
#         result+= word
#         word = ''


    # if (i == 0 or i == (len(song_No_WUB)-1)) and (song_No_WUB[i] == "9"):
    #     song_No_WUB = song_No_WUB[:i] + song_No_WUB[i+1:]
    #     print(song_No_WUB)
    #     print("="*20)
    #  if i >
    # else:
    #     song_No_WUB.replace((next((v) for x, v in enumerate(song_No_WUB) if v == song_No_WUB[x+1] and song_No_WUB[x+1] == '9')),"")
    #     song_No_WUB = song_No_WUB.replace("9", " ")

# Polycarpus works as a DJ in the best Berland nightclub, and he often uses dubstep music in his performance. Recently,
# he has decided to take a couple of old songs and make dubstep remixes from them.
#
# Let's assume that a song consists of some number of words (that don't contain WUB). To make the dubstep remix of this
# song, Polycarpus inserts a certain number of words "WUB" before the first word of the song (the number may be zero),
# after the last word (the number may be zero), and between words (at least one between any pair of neighbouring words),
# and then the boy glues together all the words, including "WUB", in one string and plays the song at the club.
#
#     For example, a song with words "I AM X" can transform into a dubstep remix as "WUBWUBIWUBAMWUBWUBX" and cannot
#     transform into "WUBWUBIAMWUBX".
#
# Recently, Jonny has heard Polycarpus's new dubstep track, but since he isn't into modern music, he decided to find out
# what was the initial song that Polycarpus remixed. Help Jonny restore the original song.
#
# Input
# The input consists of a single non-empty string, consisting only of uppercase English letters, the string's length
# doesn't exceed 200 characters
#
# Output
# Return the words of the initial song that Polycarpus used to make a dubsteb remix. Separate the words with a space.
#
# Examples
# song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
# # =>  WE ARE THE CHAMPIONS MY FRIEND