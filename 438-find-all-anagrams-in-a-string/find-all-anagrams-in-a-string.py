class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #Step 1: Compute the frequencies of string(p)
        d2={}
        for i in p:
            d2[i]=d2.get(i,0)+1
        #Step 2: Do a k-length sliding window on s
        #Step 3: Coutn the frequencies of characters in substring into d1
        k=len(p)
        d1={}
        left=0
        ans=[]
        for right in range(len(s)):
            d1[s[right]]=d1.get(s[right],0)+1#Counting frequencies of substring s
            if right>=k-1:#Checking the validity of the window
                if d1==d2:#Comparing hash maps to check anagrams
                    ans.append(left)#if anagram, inserting the starting index
                d1[s[left]]-=1# Subtracting the frequence of an outgoing element
                if d1[s[left]]==0:
                    d1.pop(s[left])#removing the element with a frequence 0
                left+=1
        return ans


