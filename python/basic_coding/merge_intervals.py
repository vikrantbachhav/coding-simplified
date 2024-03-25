def merge_intervals(lst):
    if not lst:
        return []

    lst.sort(key=lambda x: x[0])
    result = []

    start = lst[0][0]
    end = lst[0][1]

    for interval in lst[1:]:
        print(interval)
        if interval[0] <= interval[1]:
            end = max(end, interval[1])
        else:
            result.append(start, end)
            start = interval[0]
            end = interval[1]

    result.append((start, end))

    return result


if __name__ == "__main__":
    a = [(2, 5), (4, 10), (11, 15), (12, 14)]

    result = merge_intervals(a)
    print(result)

    for interval in result:
        print(result, interval)
        print(interval[0], interval[1])

# class Interval:
#     def __init__(self, x, y):
#         self.start = x
#         self.end = y
#
#
# def merge_intervals(lst):
#     if not lst:
#         return []
#
#     lst.sort(key=lambda x: x.start)
#     result = []
#
#     start = lst[0].start
#     end = lst[0].end
#
#     for interval in lst[1:]:
#         if interval.start <= end:
#             end = max(end, interval.end)
#         else:
#             result.append(Interval(start, end))
#             start = interval.start
#             end = interval.end
#
#     result.append(Interval(start, end))
#
#     return result
#
#
# if __name__ == "__main__":
#     a = [
#         Interval(2, 5),
#         Interval(4, 10),
#         Interval(11, 15),
#         Interval(12, 14)
#     ]
#
#     result = merge_intervals(a)
#
#     for interval in result:
#         print(interval.start, interval.end)
