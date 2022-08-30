"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        seen = set()
        nodeToBeExplored = [node]
        newNodeDict = {}
        while len(nodeToBeExplored) > 0:
            currNode = nodeToBeExplored.pop()
            newNode = Node(
                currNode.val) if currNode.val not in newNodeDict else newNodeDict[currNode.val]
            if currNode in seen:
                continue
            newNodeDict[currNode.val] = newNode
            for i in currNode.neighbors:
                if i.val in newNodeDict:
                    newNode.neighbors.append(newNodeDict[i.val])
                else:
                    newNeighbor = Node(i.val)
                    newNodeDict[i.val] = newNeighbor
                    newNode.neighbors.append(newNeighbor)
            nodeToBeExplored.extend(currNode.neighbors)
            seen.add(currNode)

        return newNodeDict[node.val]
