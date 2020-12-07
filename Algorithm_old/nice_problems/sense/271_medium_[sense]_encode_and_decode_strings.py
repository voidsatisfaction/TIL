from typing import List

class Codec:
  def encode(self, strs: List[str]) -> str:
    if len(strs) == 0:
      return "-1:"
    header = ".".join([ str(len(s)) for s in strs ]) + ":"
    
    body = "".join(strs)

    encodedString = header + body

    return encodedString

  def decode(self, s: str) -> List[str]:
    if s == "-1:":
      return []

    sSplit = s.split(":")
    header = sSplit[0]
    body = ":".join(sSplit[1:])

    strLengths = [ int(num) for num in header.split(".")]

    decodedStrings = []

    acc = 0
    for strLength in strLengths:
      start, end = acc, acc+strLength

      decodedStrings.append(body[start:end])

      acc += strLength
    
    return decodedStrings


c = Codec()
print(c.encode(["asldkfmaldmafslmkl", "abc"]))

print(c.decode(c.encode(["asldkfmaldmafslmkl", "abc"])))

print(c.encode([]))

print(c.decode(c.encode([])))