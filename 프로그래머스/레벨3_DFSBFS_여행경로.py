import copy
global answer


def DFS(start, tickets, answer_list):
    global answer

    answer_list.append(start)
    answer.append(answer_list)

    for index,value in enumerate(tickets):
        if value[0] == start:
            tmp_tickets = copy.deepcopy(tickets)
            tmp_answer = copy.deepcopy(answer_list)
            tmp_tickets.pop(index)
            DFS(value[1], tmp_tickets, tmp_answer)


def solution(tickets):
    global answer
    answer = []
    answer_list = []

    tickets.sort()

    DFS('ICN', tickets, answer_list)

    max = []
    for i in answer:
        if len(max) < len(i):
            max = i
    return max