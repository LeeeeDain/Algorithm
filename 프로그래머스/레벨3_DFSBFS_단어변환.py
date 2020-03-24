global answer_list

def checking(word1, word2):
    n = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            n += 1
    return n == len(word1)-1


def DFS(now_word, words, target, answer):
    global answer_list

    if now_word in words:
        words.remove(now_word)

    for i in list(x for x in words if checking(now_word, x)):
        if i == target:
            answer_list.append(answer)
        DFS(i, words, target, answer + 1)


def solution(begin, target, words):
    global answer_list
    answer_list = []
    answer = 1

    if target not in words:
        return 0

    DFS(begin, words, target, answer)

    return min(answer_list)


print(solution(	"hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))