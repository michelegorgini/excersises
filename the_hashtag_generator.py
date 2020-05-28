# codewar The Hashtag Generator

# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!
#
# Here's the deal:
# - It must start with a hashtag (#).
# - All words must have their first letter capitalized.
# - If the final result is longer than 140 chars it must return false.
# - If the input or the result is an empty string it must return false.

# Examples
# " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
# "    Hello     World   "                  =>  "#HelloWorld"
# ""                                        =>  false


def generate_hashtag(s):
    print(s)
    result = ''
    if s:
        my_list = [element.capitalize().replace(' ','') for element in s.split()]
        result = '#'
        for words in my_list:
            result += words
        if len(result) > 140:
            result = False
    else:
        result = False
    return result

# Best solution

# def generate_hashtag(s):
#     output = "#"
#
#     for word in s.split():
#         output += word.capitalize()
#
#     return False if (len(s) == 0 or len(output) > 140) else output

#


# generate_hashtag('')
print(generate_hashtag('Do We have A Hashtag')[0] == '#')
# generate_hashtag('Codewars')
# generate_hashtag('Codewars      ')
# generate_hashtag('Codewars Is Nice')
# generate_hashtag('codewars is nice')
# generate_hashtag('c i n')
# generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat')


# Test.assert_equals(generate_hashtag(''), False, 'Expected an empty string to return False')
# Test.assert_equals(generate_hashtag('Do We have A Hashtag')[0], '#', 'Expeted a Hashtag (#) at the beginning.')
# Test.assert_equals(generate_hashtag('Codewars'), '#Codewars', 'Should handle a single word.')
# Test.assert_equals(generate_hashtag('Codewars      '), '#Codewars', 'Should handle trailing whitespace.')
# Test.assert_equals(generate_hashtag('Codewars Is Nice'), '#CodewarsIsNice', 'Should remove spaces.')
# Test.assert_equals(generate_hashtag('codewars is nice'), '#CodewarsIsNice', 'Should capitalize first letters of words.')
# Test.assert_equals(generate_hashtag('CodeWars is nice'), '#CodewarsIsNice', 'Should capitalize all letters of words - all lower case but the first.')
# Test.assert_equals(generate_hashtag('c i n'), '#CIN', 'Should capitalize first letters of words even when single letters.')
# Test.assert_equals(generate_hashtag('codewars  is  nice'), '#CodewarsIsNice', 'Should deal with unnecessary middle spaces.')
# Test.assert_equals(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'), False, 'Should return False if the final word is longer than 140 chars.')
#
