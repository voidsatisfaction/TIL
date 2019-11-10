from typing import List, Dict

class Solution:
  def minWindow(self, s: str, t: str) -> str:
    stringIndexLists, targetCharacterNums = self._getStringIndexLists(s, t)

    leftIndex, rightIndex = self._getMinWindowIndex(stringIndexLists, targetCharacterNums, s)

    if leftIndex == -1:
      return ""
    else:
      return s[leftIndex:rightIndex+1]
    
  def _getMinWindowIndex(self, stringIndexLists: List[List[int]], targetCharacterNums: List[int], s: str) -> (int, int):
    sortedAllStringIndex = []
    for stringIndexList in stringIndexLists:
      sortedAllStringIndex += stringIndexList
    sortedAllStringIndex = sorted(list(set(sortedAllStringIndex)))

    reversedStringIndexLists = [ stringIndexList[::-1] for stringIndexList in stringIndexLists ]

    answerLeft, answerRight = -1, len(s)

    for left in sortedAllStringIndex:
      right = -1
      for i, reversedStringIndexList in enumerate(reversedStringIndexLists):
        targetCharacterNum = targetCharacterNums[i]
        while len(reversedStringIndexList)>0 and reversedStringIndexList[-1]<left:
          reversedStringIndexList.pop()
        
        if len(reversedStringIndexList) < targetCharacterNum:
          return (answerLeft, answerRight)

        right = max(right, reversedStringIndexList[-targetCharacterNum])

      if right - left < answerRight - answerLeft:
        answerRight, answerLeft = right, left

    return (answerLeft, answerRight)

  def _getStringIndexLists(self, s: str, t: str) -> (List[List[int]], List[int]):
    hashMap = {}
    hashMapSync = []
    i = 0
    stringIndex = []

    for c in t:
      if hashMap.get(c) is None:
        hashMap[c] = { "index": i, "num": 1 }
        hashMapSync.append(c)
        stringIndex.append([])
        i += 1
      else:
        hashMap[c]["num"] += 1

    j = 0
    for c in s:
      if hashMap.get(c) is not None:
        index = hashMap.get(c).get("index")
        stringIndex[index].append(j)
      j += 1

    targetCharacterNums = [ hashMap.get(c).get("num") for c in hashMapSync ]

    return stringIndex, targetCharacterNums


print(Solution().minWindow("A", "AA"))
print(Solution().minWindow("ADOBECODEBANC", "ABC"))
print(Solution().minWindow("ADOBEODEBAN", "ABC"))
print(Solution().minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd"))