
# Intersection of Two Linked Lists
def get_intersection_node(headA, headB):
    if not headA or not headB:
        return None
    pA, pB = headA, headB
    while pA != pB:
        pA = pB if not pA else pA.next
        pB = pA if not pB else pB.next
    return pA

