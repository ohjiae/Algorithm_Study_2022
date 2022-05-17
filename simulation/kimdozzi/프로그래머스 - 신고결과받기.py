from collections import Counter


def solution(id_list, report, k):
    answer = []
    lst = []
    report_dict = {}

    for id in id_list:
        report_dict[id] = []

    for group in report:
        user, report = group.split(' ')

        if report not in report_dict[user]:
            report_dict[user].append(report)

            lst.append(report)

    cnt_dict = Counter(lst)

    for id in id_list:
        temp = [check for check in report_dict[id] if cnt_dict[check] >= k]
        answer.append(
            len([check for check in report_dict[id] if cnt_dict[check] >= k]))

    return answer


if __name__ == "__main__":
    id_list = ["muzi", "frodo", "apeach", "neo"]

    report = ["muzi frodo", "apeach frodo",
              "frodo neo", "muzi neo", "apeach muzi"
              ]
    k = 2

    print(solution(id_list, report, k))
#
