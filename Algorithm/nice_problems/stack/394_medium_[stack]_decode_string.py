# Way1: stack
class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        string_stack = ['']

        num_cache = ''
        for c in s:
            if c == '[':
                num_stack.append(int(num_cache))
                num_cache = ''

                string_stack.append('')
            elif c == ']':
                num = num_stack.pop()
                string = string_stack.pop()

                string_stack[-1] += string * num
            elif c.isdigit():
                num_cache += c
            else:
                string_stack[-1] += c

        return string_stack[0]

if __name__ == '__main__':
    assert Solution().decodeString("3[a]2[bc]") == "aaabcbc"
    assert Solution().decodeString("3[a2[c]]") == "accaccacc"
    assert Solution().decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
    assert Solution().decodeString("a3[a2[cd2[e]]l]") == "aacdeecdeelacdeecdeelacdeecdeel"
    assert Solution().decodeString("a") == "a"
    assert Solution().decodeString("") == ""