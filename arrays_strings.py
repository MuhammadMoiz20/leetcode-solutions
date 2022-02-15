
# Product of Array Except Self
def product_except_self(nums):
    n = len(nums)
    result = [1] * n
    left = 1
    for i in range(n):
        result[i] = left
        left *= nums[i]
    right = 1
    for i in range(n-1, -1, -1):
        result[i] *= right
        right *= nums[i]
    return result

# Backfill update on 2022-01-18 18:22:32
# Authored by backfill-2022.sh
# Backfill update on 2022-01-20 11:32:51
# Authored by backfill-2022.sh
# Backfill update on 2022-01-20 18:52:22
# Authored by backfill-2022.sh
# Backfill update on 2022-01-30 11:35:57
# Authored by backfill-2022.sh
# Backfill update on 2022-01-31 19:25:46
# Authored by backfill-2022.sh
# Backfill update on 2022-02-10 20:32:07
# Authored by backfill-2022.sh
# Backfill update on 2022-02-21 17:37:27
# Authored by backfill-2022.sh
# Backfill update on 2022-02-26 19:30:51
# Authored by backfill-2022.sh
# Backfill update on 2022-02-27 18:30:39
# Authored by backfill-2022.sh
# Backfill update on 2022-02-28 10:32:35
# Authored by backfill-2022.sh
# Backfill update on 2022-03-09 14:18:36
# Authored by backfill-2022.sh
# Backfill update on 2022-03-11 09:21:07
# Authored by backfill-2022.sh
# Backfill update on 2022-03-21 20:27:59
# Authored by backfill-2022.sh
