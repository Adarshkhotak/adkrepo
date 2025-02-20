class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        
        counter1_dict={}
        for i in range(len(word1)): #for this we counter() method alsos
            counter1_dict[word1[i]]=counter1_dict.get(word1[i],0)+1

        counter2_dict={} 
        for i in range(len(word2)):
            counter2_dict[word2[i]]=counter2_dict.get(word2[i],0)+1
        
        if set(counter1_dict.keys()) != set(counter2_dict.keys()):
            return False
        # the values() method returns counts of the elements, which behaves like a list of integers
        if sorted(counter1_dict.values()) != sorted(counter2_dict.values()):
            return False
        
        return True



        