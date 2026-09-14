# Part 1 Tests
- [x] "line" and "line" -> True 
- [x] "" and "" -> True
- [x] "run" and "nru" -> True
- [x]  "bank" and "knab" -> True
- [x]  "bank" and "banr" -> False

## Properties to test
- [x] If two words are not the same length, then they cannot be anagrams of each other
- [x] If the first word has a letter in it that is not in the second word, they cannot be anagrams of each other
- [x] The order of anagrams being applied does not matter

# Part 2 Tests
- [x] "line", ["line"] -> ["line"]
- [x] "run", ["run"] -> ["run"]
- [x] "run", ["run", "run", "bob"] -> ["run", "run"]
- [x] "line", ["bob"] -> []
- [x] "run", ["nru", "bob"] -> ["nru"]
- [] "run", ["run", "nru", "urn", "nrus"] -> ["run", "nru", "urn"]™