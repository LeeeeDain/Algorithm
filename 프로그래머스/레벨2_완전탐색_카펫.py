def solution(brown, red):
    answer = []
    line = 1

    while line <= (red/2) or red == 1:
        if red % line != 0:
            line += 1
            continue

        row = int((red / line) + 2)
        column = int(line + 2)

        if (row*2) + (line*2) == brown:
            answer.append(row)
            answer.append(column)
            break

        line += 1

    return answer