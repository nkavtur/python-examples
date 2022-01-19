class Solution:
    def longestPalindrome(self, s: str):
        longest = s[0]

        solution = [
            [i - j == 1 or i == j for j in range(len(s))]
            for i in range(len(s))
        ]

        for i in range(0, len(s)):
            j = -1
            while (j := j + 1) < len(s):
                start, end = min(i, j), max(i, j)

                if start + 1 >= len(s) or end - 1 < 0:
                    continue

                if solution[start + 1][end - 1]:
                    prev_char = s[start]
                    next_char = s[end]

                    if prev_char == next_char:
                        longest = longest \
                            if len(longest) >= len(s[start:end + 1]) \
                            else s[start:end + 1]

                        solution[start][end] = True
                        solution[end][start] = True

        return longest


print(Solution().longestPalindrome("ababababa"))
print(Solution().longestPalindrome("cbd"))
print(Solution().longestPalindrome("cbbd"))
print(Solution().longestPalindrome("bbbb"))
print(Solution().longestPalindrome("xaabacxcabaaxcabaax"))
print(Solution().longestPalindrome("iekmafcuinxsmkiaoqvgrlnmkgrevbkikaadcuuenrudjcvwslolsvvmykfrjveasenkoqvljkynevupgebavzurjgsbvxgqqlrmbyldqpnwuykqvebmehoglzdqgnnqrhpiqqvcvqwnhoounutqqghmvviezjrpjbxiizbfjdstavsvnfxmxnlyodntuwtaiawodrbqlokgfkvnwjmjfargyoxrecsfyeqirkpjhditwrpwdhgacrumguwkcevchntenjlcvgcdwvuymbdbfvmtyjppxndqxdcqbazrsgptfktfyarvtqinkeqnfzraqxxytngmpmfpekjlrdzhgpldpvwnbdaduntbqkyoocbzyogqhcvxcgyggdhyvrrgkjeipxlkrirpityizzeletevmlujdjtahzewtpgajdmyolaizyvhjlvxetweolftsrktimsntzxyxbuttubxyxztnsmitkrstfloewtexvljhvyzialoymdjagptwezhatjdjulmvetelezziytiprirklxpiejkgrrvyhdggygcxvchqgoyzbcooykqbtnudadbnwvpdlpghzdrljkepfmpmgntyxxqarzfnqekniqtvrayftkftpgsrzabqcdxqdnxppjytmvfbdbmyuvwdcgvcljnetnhcveckwugmurcaghdwprwtidhjpkriqeyfscerxoygrafjmjwnvkfgkolqbrdowaiatwutndoylnxmxfnvsvatsdjfbziixbjprjzeivvmhgqqtunuoohnwqvcvqqiphrqnngqdzlgohembevqkyuwnpqdlybmrlqqgxvbsgjruzvabegpuvenykjlvqoknesaevjrfkymvvslolswvcjdurneuucdaakikbvergkmnlrgvqoaikmsxniucfamkei"))
