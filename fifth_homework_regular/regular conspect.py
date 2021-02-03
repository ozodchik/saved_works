import re


def re_examples(argument_exp: str):
    """
    if you didn't understand watch this video: https://youtu.be/_pLpx6btq6U

    some_text = "hello world goodbye World what does it mean world 2020 2021"

1) . - any character(gives 1 any symbol in output)
    we can use that front any symbol and after any symbols like that:
    p = re.compile("h.") -> re.findall(p, some_text) -> "he"

    example:
some_text = "hello world goodbye world worlds of any tanks 2020 2021"
pattern = re.compile(".")
result = re.findall(pattern, some_text)
print(result)
output result:
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', ' ', 'g', 'o', 'o', 'd', 'b', 'y', 'e', ' ', 'w', 'o', 'r'
, 'l', 'd', ' ', 'w', 'o', 'r', 'l', 'd', 's', ' ', 'o', 'f', ' ', 'a', 'n', 'y', ' ', 't', 'a', 'n', 'k', 's', ' '
, '2', '0', '2', '0', ' ', '2', '0', '2', '1']



2) [] - any of them(symbols)
    we can use that when we want to take  1-result and 2-result and
he gives us both(and 1 and 2) result and we can input range(диапазон)
from a before z, w, b, f and others and we can input range 0-9

    example:
pattern = re.compile("[hworld]")
result = re.findall(pattern, some_text)
print(result)
output result:
['h', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd', 'o', 'o', 'd', 'w', 'o', 
'r', 'l', 'd', 'w', 'o', 'r', 'l', 'd', 'o']

    Besides we can use it like that:
pattern = re.compile("[wW]orl.")
result = re.findall(pattern, some_text)
print(result)
output result:
['world', 'World', 'world']

    And we can use it like that:
pattern = re.compile("[A-Z]*\S[a-z]*\S*") or:
    pattern =re.compile("[1-9]*\S[A-Z]*\S[a-z]*\S") ->
     ->['hello', 'world', 'goodbye', 'World',
       'worlds','any', 'tanks', '2020', '2021']
result = re.findall(pattern, some_text)
print(result)
output result:
['hello', 'world', 'goodbye', 'World', 'worlds', 'of', 'any', 'tanks',
'2020', '2021']


3)$ - end of line
    it shows us where is end of line

    example:
    pattern = re.compile(".$")
result = re.findall(pattern, some_text)
print(result) -> ['1']


4) ^ - it means start of line so we want to take a start of line

    example:
    pattern = re.compile("^[a-z]\w+\s\w+")
result = re.findall(pattern, some_text)
print(result) -> ['hello world']
    But without that it means not only 'starts from this letter' it can mean
'not starts with this letter' like this situation:
    pattern = re.compile("^[^ab]\w+\s\w+")
result = re.findall(pattern, some_text)
print(result) -> ['hello world']
    pattern = re.compile("^[^ah]\w+\s\w+")
result = re.findall(pattern, some_text)
print(result) -> [] cause we introduced 'h' to arguments


5) \d - any number(numeric, figures) from 0 before 9 it gives us all numbers
from 0 before 9 (one '\d' means one number)

     example:
    pattern = re.compile("\d")
result = re.findall(pattern, some_text)
print(result) -> ['2', '0', '2', '0', '2', '0', '2', '1']

    pattern = re.compile("\d+")
result = re.findall(pattern, some_text)
print(result) -> ['2020', '2021']

    pattern = re.compile("\d.+")
result = re.findall(pattern, some_text)
print(result) -> ['2020 2021']

    pattern = re.compile("\d+\s\d+")
result = re.findall(pattern, some_text)
print(result) -> ['2020 2021']


6) \D - "all of them but without numbers" it gives us all things without numbers
from 0 before 9

    Example:
        pattern = re.compile("\D")
result = re.findall(pattern, some_text)
print(result) -> ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', ' ', 'g',
 'o', 'o', 'd', 'b', 'y', 'e', ' ', 'W', 'o', 'r', 'l', 'd', ' ', 'w', 'h', 'a',
 't', ' ', 'd', 'o', 'e', 's', ' ', 'i', 't', ' ', 'm', 'e', 'a', 'n', ' ', ' ']

    pattern = re.compile("\D+")
result = re.findall(pattern, some_text)
print(result) -> ['hello world goodbye World what does it mean ', ' ']

    pattern = re.compile("\D.")
result = re.findall(pattern, some_text)
print(result) -> ['he', 'll', 'o ', 'wo', 'rl', 'd ', 'go', 'od', 'by', 'e ',
'Wo', 'rl', 'd ', 'wh', 'at', ' d', 'oe', 's ', 'it', ' m', 'ea', 'n ', ' 2']
if you noticed it has number 2 cause we used . before \D it means 'take all
symbols without number and with 1 any symbol' if you didn't understand look at
1-paragraph about symbol . we know so symbol . means any symbol
    pattern = re.compile("\d+\D\d+")
result = re.findall(pattern, some_text)
print(result) -> ['2020 2021']


7) \s - 'space' it means so we want to take a space and it searchs space

    example:
    pattern = re.compile("\s")
result = re.findall(pattern, some_text)
print(result) -> [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] we give all spaces

    pattern = re.compile(".\s")
result = re.findall(pattern, some_text)
print(result) -> ['o ', 'd ', 'e ', 'd ', 't ', 's ', 't ', 'n ', '0 '] we give all
letters ending with a space


8) \S - 'all symbols without space' it means so we want to take all symbols(numbers
and others) without spaces

    example:
    pattern = re.compile("\w+\S")
result = re.findall(pattern, some_text)
print(result) -> ['hello', 'world', 'goodbye', 'World', 'what', 'does', 'it',
'mean', '2020', '2021']


9) \w - 'all word characters' it means so we want to take all word characters
 (one \w means one character)

    example:
    pattern = re.compile("\w")
result = re.findall(pattern, some_text)
print(result) -> ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd', 'g', 'o', 'o',
     'd', 'b', 'y', 'e', 'W', 'o','r', 'l', 'd', 'w', 'h', 'a', 't',
     'd', 'o', 'e', 's', 'i', 't', 'm', 'e', 'a', 'n', '2', '0','2',
     '0', '2', '0', '2', '1']

    pattern = re.compile("\w+")
result = re.findall(pattern, some_text)
print(result) -> ['hello', 'world', 'goodbye', 'World', 'what', 'does', 'it',
'mean', '2020', '2021']


10) \W - 'all symbols without letters, numbers and underscores'
it means so we want to take all symbols without letters, numbers and underscores

    Example:
        pattern = re.compile("\W")
result = re.findall(pattern, some_text)
print(result) -> [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
here he only displayed spaces for us, but since we have no other characters here,
if they were, he would display them too(', -, ., and others)


QUANTIFICATION


1) m{n, x} - search m in a row n times

Examples:
    pattern = re.compile("world{1,10}")
result = re.findall(pattern, some_text)
print(result) -> ['world', 'world'] -> here we can specify the range of the
squeak
    pattern = re.compile("world{1,10}|World{1,10}")
result = re.findall(pattern, some_text)
print(result) -> ['world', 'World', 'world']

2) * - 'from 0 before infinity' this looks for characters from 0 to infinity
 (as many as there are)

Examples:
    pattern = re.compile("world*")
result = re.findall(pattern, some_text)
print(result) -> ['world', 'world']


3) + - '1 or more' it means so we search any symbols 1 or more time

Examples:
    pattern = re.compile("\d+")
result = re.findall(pattern, some_text)
print(result) -> ['2020', '2021']


4) ? - '0 or 1 time'








If you didn't understand watch this video: https://youtu.be/_pLpx6btq6U
or read documentation in this website: http://www.pcre.ru/
and here: https://habr.com/ru/post/349860/
Documentation in English is here: https://docs.python.org/3/library/re.html
    """
    # pattern = re.compile(argument_exp)
    # result = re.findall(pattern, some_text)

    pass


some_text = "hello world goodbye  World what does it mean world 2020 2021"

pattern = re.compile("\d+")
result = re.findall(pattern, some_text)
print(result)
# print(help(re_examples))




