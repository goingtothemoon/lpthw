
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing",
	"That you could type up right",
	"But it didn't sing",
	"So I said goodnight."
	)

# I forgot to add the , in order to connect the sentence giving me a TypeError: not enough arguments for that string.
# The output changes because of the single quote in the word `didn't` for line 11 changing the output
