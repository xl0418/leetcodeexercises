class Solution:
    def reorderLogFiles(self, logs):
        second_word = []
        for log in logs:
            second_word.append(log.split()[1])
        index_sorted = sorted(range(len(second_word)), key = lambda k: second_word[k])
        second_word.sort()
        digit = 0
        while second_word[digit].isdigit():
            digit += 1
        reorder_index = index_sorted[digit:]+sorted(index_sorted[:digit])
        outlist = []
        for i in reorder_index:
            outlist.append(logs[i])
        return outlist

Logs = ["qi ir oo i", "cp vnzw i", "0 fkbikbts", "4 j trouka", "gn j q al", "5r w wgqc", "m8 x haje", "fg 28694 6", "i gf mwdoa", "ao 0850716"]
reorderlogs = Solution()
reorderlogs.reorderLogFiles(logs=Logs)

class Solution(object):
    def reorderLogFiles(self, logs):
        def f(log):
            id_, rest = log.split(" ", 1)
            return (0, rest, id_) if rest[0].isalpha() else (1,)

        return sorted(logs, key = f)



