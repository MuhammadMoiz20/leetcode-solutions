
# Serialize and Deserialize Binary Tree
class Codec:
    def serialize(self, root):
        result = []
        def preorder(node):
            if not node:
                result.append('None')
                return
            result.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return ','.join(result)
    
    def deserialize(self, data):
        nodes = data.split(',')
        def build():
            val = nodes.pop(0)
            if val == 'None':
                return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node
        return build()

# Backfill update on 2022-01-12 20:13:21
# Authored by backfill-2022.sh
# Backfill update on 2022-01-18 14:10:29
# Authored by backfill-2022.sh
# Backfill update on 2022-01-18 15:34:36
# Authored by backfill-2022.sh
# Backfill update on 2022-01-19 13:40:38
# Authored by backfill-2022.sh
# Backfill update on 2022-01-30 19:49:24
# Authored by backfill-2022.sh
# Backfill update on 2022-01-31 08:23:06
# Authored by backfill-2022.sh
# Backfill update on 2022-02-09 11:06:40
# Authored by backfill-2022.sh
# Backfill update on 2022-02-10 20:28:37
# Authored by backfill-2022.sh
# Backfill update on 2022-02-26 16:03:30
# Authored by backfill-2022.sh
# Backfill update on 2022-03-01 18:40:54
# Authored by backfill-2022.sh
# Backfill update on 2022-03-02 17:56:14
# Authored by backfill-2022.sh
# Backfill update on 2022-03-02 19:09:10
# Authored by backfill-2022.sh
# Backfill update on 2022-03-07 16:36:14
# Authored by backfill-2022.sh
# Backfill update on 2022-03-09 10:10:41
# Authored by backfill-2022.sh
# Backfill update on 2022-03-09 17:45:57
# Authored by backfill-2022.sh
# Backfill update on 2022-03-10 13:21:49
# Authored by backfill-2022.sh
# Backfill update on 2022-03-10 19:29:37
# Authored by backfill-2022.sh
# Backfill update on 2022-03-11 14:48:12
# Authored by backfill-2022.sh
