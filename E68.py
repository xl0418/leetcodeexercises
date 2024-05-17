class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        ans = []
        temp_word = []
        for i in range(len(words)):
            len_word = len(words[i])
            len_temp = len(temp_word)
            if len_word == maxWidth and len(temp_word) == 0:
                ans.append(words[i])
            else:
                if len_temp + len_word + 1 <= maxWidth:
                    temp_word = words[i] if len(temp_word) == 0 else temp_word + ' ' + words[i]
                else:
                    if len(temp_word)<maxWidth:
                        words_in_temp = temp_word.split(" ")
                        word_lenth = sum([len(x) for x in words_in_temp])
                        do = True

                        while do:
                            if len(words_in_temp) == 1:
                                words_in_temp[0] += ' ' * int(maxWidth - word_lenth)
                                do = False
                            else:
                                for ii in range(len(words_in_temp)-1):
                                    words_in_temp[ii] += ' '
                                    word_lenth += 1
                                    if word_lenth == maxWidth:
                                        do = False
                                        break
                        ans.append(''.join(words_in_temp))
                    else:
                        ans.append(temp_word)

                    temp_word = words[i]

        if len(temp_word) < maxWidth and len(temp_word)>0:
            temp_word += ' '* int(maxWidth - len(temp_word))

        if len(temp_word) == maxWidth:
            ans.append(temp_word)

        return ans






words = ["What","must","be","shall","be."]
maxWidth = 5
solution = Solution()
solution.fullJustify(words, maxWidth)