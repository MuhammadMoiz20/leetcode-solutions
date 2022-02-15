
# Trapping Rain Water
def trap(height):
    if not height:
        return 0
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water

# Backfill update on 2022-01-12 12:55:59
# Authored by backfill-2022.sh
# Backfill update on 2022-01-30 18:06:04
# Authored by backfill-2022.sh
# Backfill update on 2022-01-31 09:01:58
# Authored by backfill-2022.sh
# Backfill update on 2022-01-31 19:48:38
# Authored by backfill-2022.sh
# Backfill update on 2022-02-09 08:41:04
# Authored by backfill-2022.sh
# Backfill update on 2022-02-09 09:39:19
# Authored by backfill-2022.sh
# Backfill update on 2022-02-26 18:28:51
# Authored by backfill-2022.sh
# Backfill update on 2022-03-01 09:31:58
# Authored by backfill-2022.sh
# Backfill update on 2022-03-09 09:33:51
# Authored by backfill-2022.sh
# Backfill update on 2022-03-09 12:41:15
# Authored by backfill-2022.sh
# Backfill update on 2022-03-10 15:09:50
# Authored by backfill-2022.sh
# Backfill update on 2022-03-10 15:43:51
# Authored by backfill-2022.sh
# Backfill update on 2022-03-11 15:08:27
# Authored by backfill-2022.sh
# Backfill update on 2022-03-11 19:28:45
# Authored by backfill-2022.sh
