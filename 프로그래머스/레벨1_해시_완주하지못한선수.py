import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


print(solution(	["leo", "kiki","leo","leo","leo"], ["leo","kiki","leo","leo"]))
print(solution(	["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(	["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))