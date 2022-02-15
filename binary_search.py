
# Binary Search Template
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Binary Search Patterns - finding first/last occurrence
def find_first(arr, target):
    left, right, result = 0, len(arr) - 1, -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

# Backfill update on 2022-01-12 10:26:21
# Authored by backfill-2022.sh
# Backfill update on 2022-01-12 11:59:33
# Authored by backfill-2022.sh
# Backfill update on 2022-01-12 12:32:53
# Authored by backfill-2022.sh
# Backfill update on 2022-01-12 20:51:56
# Authored by backfill-2022.sh
# Backfill update on 2022-01-13 14:38:27
# Authored by backfill-2022.sh
# Backfill update on 2022-01-30 20:29:15
# Authored by backfill-2022.sh
# Backfill update on 2022-01-31 11:32:47
# Authored by backfill-2022.sh
# Backfill update on 2022-01-31 19:25:02
# Authored by backfill-2022.sh
# Backfill update on 2022-02-09 10:41:11
# Authored by backfill-2022.sh
# Backfill update on 2022-02-23 14:28:17
# Authored by backfill-2022.sh
# Backfill update on 2022-02-26 11:13:59
# Authored by backfill-2022.sh
# Backfill update on 2022-02-26 20:45:58
# Authored by backfill-2022.sh
# Backfill update on 2022-02-27 19:27:53
# Authored by backfill-2022.sh
# Backfill update on 2022-03-01 10:15:53
# Authored by backfill-2022.sh
# Backfill update on 2022-03-01 14:47:22
# Authored by backfill-2022.sh
# Backfill update on 2022-03-02 17:10:30
# Authored by backfill-2022.sh
# Backfill update on 2022-03-07 09:00:58
# Authored by backfill-2022.sh
# Backfill update on 2022-03-07 18:01:23
# Authored by backfill-2022.sh
# Backfill update on 2022-03-08 15:08:00
# Authored by backfill-2022.sh
# Backfill update on 2022-03-10 16:13:29
# Authored by backfill-2022.sh
# Backfill update on 2022-03-10 20:14:04
# Authored by backfill-2022.sh
# Backfill update on 2022-03-21 12:20:29
# Authored by backfill-2022.sh
