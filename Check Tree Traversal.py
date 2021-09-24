class Solution:
    def checktree(self, preorder, inorder, postorder, N):
      if N == 0: 
    		return 1
    	if N == 1: 
    		return (preorder[0] == inorder[0]) and (inorder[0] == postorder[0]); 
    	idx = -1
    	for i in range(N): 
    		if inorder[i] == preorder[0]: 
    			idx = i 
    			break
    	if idx == -1: 
    		return 0
    	if preorder[0] != postorder[N-1]:
    	    return 0
    	ret1 = self.checktree(preorder[1:], inorder, postorder, idx)
    	ret2 = self.checktree(preorder[idx + 1:], inorder[idx + 1:], postorder[idx:], N-idx-1);  
    	return (ret1 and ret2)
