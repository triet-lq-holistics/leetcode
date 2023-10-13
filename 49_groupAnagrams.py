def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        1. Get counter of each str 
        2. Group by each counter and collect all relevant word with the same counter within the hashmap
        3. Return the values of each hashmap in a list
        """
        # counters = {word: str(Counter(word)) for word in strs}
        # anagrams = defaultdict(list)

        # for key, val in counters.items(): 
        #     anagrams[val].append(key)
        
        # return [val for val in anagrams.values()]

        d = {idx: str(sorted(strs[idx])) for idx in range(len(strs))} 
        anagrams = defaultdict(list)
        
        for key, val in d.items(): 
            anagrams[val].append(strs[key])
        
        return [val for val in anagrams.values()]