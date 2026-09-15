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
- [x] "run", ["run", "nru", "urn", "nrus"] -> ["run", "nru", "urn"]™

## Properties to test
- [x] The output list can be at most as big as the input list
- [x] every word in the output list must be the same length as that of the target
- [x] Every word in the output list must be an anagram of the target word

# Part 3 Tests
- [] [] -> []
- [] ["eat", "eat", "bob"] -> [["eat", "eat"], ["bob"]]
- [] ["eat", "tea", "bob", "bbo", "shoe"] -> [["eat", "tea"], ["bob", "bbo"], ["shoe"]]

## Properties to test
- [] The total number of words in the output array must be equal to the total count of the words in the input array
- [] applying the algorithm again to any sub list, must return that sub list, and that sub list alone



