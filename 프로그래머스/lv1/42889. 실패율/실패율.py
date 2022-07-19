import collections


def solution(N, stages):
    answer = dict()

    stages.sort()

    total_person = len(stages)

    counter = collections.Counter(stages).items()

    for i in range(1, N + 1):
        answer.setdefault(i, 0.0)

    for key, value in counter:
        if key == N + 1:
            continue
        failure_rate = value / total_person
        answer[key] = failure_rate
        total_person -= value
    answer = list(sorted(answer.items(), key=lambda x: -x[1]))

    ano_answer = [value[0] for value in answer]
    return ano_answer