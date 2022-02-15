
# Subsets (Power Set)
def subsets(nums):
    result = [[]]
    for num in nums:
        result += [current + [num] for current in result]
    return result

# Subsets II (with duplicates)
def subsets_with_dup(nums):
    nums.sort()
    result = [[]]
    prev_size = 0
    for i, num in enumerate(nums):
        start = 0 if i == 0 or nums[i] != nums[i-1] else prev_size
        prev_size = len(result)
        for j in range(start, prev_size):
            result.append(result[j] + [num])
    return result

# Backfill update on 2022-01-18 08:18:50
# Authored by backfill-2022.sh
# Backfill update on 2022-01-18 11:13:33
# Authored by backfill-2022.sh
# Backfill update on 2022-01-19 11:07:26
# Authored by backfill-2022.sh
# Backfill update on 2022-01-19 14:43:38
# Authored by backfill-2022.sh
# Backfill update on 2022-01-30 11:45:22
# Authored by backfill-2022.sh
# Backfill update on 2022-02-01 15:46:47
# Authored by backfill-2022.sh
# Backfill update on 2022-02-01 16:57:18
# Authored by backfill-2022.sh
# Backfill update on 2022-02-01 17:50:47
# Authored by backfill-2022.sh
# Backfill update on 2022-02-09 09:00:28
# Authored by backfill-2022.sh
# Backfill update on 2022-02-21 20:47:52
# Authored by backfill-2022.sh
# Backfill update on 2022-03-07 10:45:53
# Authored by backfill-2022.sh
# Backfill update on 2022-03-08 20:31:14
# Authored by backfill-2022.sh
# Backfill update on 2022-03-09 16:06:39
# Authored by backfill-2022.sh
# Backfill update on 2022-03-09 18:27:45
# Authored by backfill-2022.sh
# Backfill update on 2022-03-10 11:00:29
# Authored by backfill-2022.sh
