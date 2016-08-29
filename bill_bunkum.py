import textwrap

#explanations for 1) textwrap.wrap() ; 2) sorted() ; 3) zip()


#textwrap.wrap()
"""SYNTAX: your_variable = textwrap.wrap(some_text, width=70, **kwargs)

if not specified, the default width is 70
**kwargs are variables passed to a function that have not 
yet been defined...as opposed to *args, which are an as of yet
undetermined # of args...chew on that.
"""

decartesText = """But I cannot forget that, at other times I have been 
deceived in sleep by similar illusions; and, attentively 
considering those cases, I perceive so clearly that there 
exist no certain marks by which the state of waking can 
ever be distinguished from sleep, that I feel greatly 
astonished; and in amazement I almost persuade myself 
that I am now dreaming."""

def usingTextWrap(text):
	print("using textwrap.wrap():")
	paragraph = textwrap.wrap(decartesText, width=50)
	for element in paragraph:
		print(element)

usingTextWrap(decartesText)

#sorted()
"""SYNTAX: sorted(any_iterable)
or -> sorted(iterable[, cmp[, key[, reverse]]])

doesn't modify the original list (whereas, .sort() does)
takes any iterable, e.g. dictionary, tuple

https://docs.python.org/2/library/functions.html#type
(how to use): https://docs.python.org/2/howto/sorting.html#sortinghowto
"""
superList = {
	"key1": "go",
	"key5": 3,
	"key3": "herro",
	"key2": 4.4,
}

#easy example
def usingSorted(text):
	print("\n")
	print("w/o sorted()")
	print(text)
	print("\n")
	print("using sorted():")
	print(sorted(text))

usingSorted(superList)

#more difficult example
def usingSortedHard(text):
	print("\n")
	print("using sorted() ex#2:")
	print(sorted(text.split(), key=str.upper))

"""i dont quite understand what str.upper does here...cos the output is't
capitalized"""

usingSortedHard(decartesText)

#zip(*iterables)
"""
SYNTAX: newList = zip(x, y)

'zip' takes two iterables and puts each item together, creating a new, 
crazy, borg-style tuple.
it's best if both iterables have the same # of items (equal length);
if they are unequal, use itertools.zip_longest() <- but that's another 
story.
"""
tupleUp = ("c", "a", "b", "g",)
tupleDown = ("g", "b", "8", "n",)

def borgStyle(x, y):
	print("\n")
	zipped = zip(x, y)
	print("zipped up:")
	print(list(zipped))
	print("\n")
	unzipped_1, unzipped_2 = zip(*zip(x, y))
	print("unzipped")
	print(unzipped_1, unzipped_2)

borgStyle(tupleDown, tupleUp)
