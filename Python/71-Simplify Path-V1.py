class Solution(object):
    def simplifyPath(self, path):
        pList = [p for p in path.split("/") if p!="." and p!=""]
        result = []
        for p in pList:
            if p == "..":
                if result:
                    result.pop()
            else:
                result.append(p)
        return "/" + "/".join(result)
