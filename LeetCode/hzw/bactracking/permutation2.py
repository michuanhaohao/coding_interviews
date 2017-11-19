# [Ebay]
# 输出给定String的所有permutation

def findPermu(s):
	s = list(s)
	s.sort()
	res = []

	used = [False for i in range(len(s))]

	dfs(s, [], used, res)


def dfs(s, tmp, used, res):
	if len(tmp) == len(s):
		res.append(''.join(tmp))
		return

	for i in range(len(s)):
		if used[i]:
			continue
		if i != 0 and s[i] == s[i-1] and not used[i-1]:
			continue
		used[i] = True
		tmp.append(s[i])
		dfs(s, tmp, used, res)
		used[i] = False
		tmp.pop()

	return


'''
                 Empty
        A      (A)      B      C   D    E    F 
    A B C ..

When we attemp to put the second A in first position, we should not do this since it will be totally same with first child tree.


'''