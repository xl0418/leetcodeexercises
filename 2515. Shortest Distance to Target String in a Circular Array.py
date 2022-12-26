class Solution:
    def closetTarget(self, words: list[str], target: str, startIndex: int) -> int:
        indices = []
        for idx, value in enumerate(words):
            if value == target:
                indices.append(idx)
        dis = []
        for item in indices:
            dis.append(min(abs(startIndex - item), min(startIndex, item) + len(words) - max(startIndex, item)))

        return min(dis) if len(dis)>0 else -1


if __name__ == "__main__":
    words = ["hsdqinnoha", "mqhskgeqzr", "zemkwvqrww", "zemkwvqrww", "daljcrktje", "fghofclnwp", "djwdworyka", "cxfpybanhd",
     "fghofclnwp", "fghofclnwp"]
    target = "zemkwvqrww"
    startIndex = 8
    res = Solution()
    ret = res.closetTarget(words = words,
                     target = target,
                     startIndex = startIndex)
