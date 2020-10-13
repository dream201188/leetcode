package java_sub;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class PostOrder_diedai {


    /**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode prev = null;
        TreeNode cur = root;
        while (stack.size() > 0 || cur != null) {
            while (cur != null) {
                stack.add(cur);
                cur = cur.left;//当前节点为空，说明左边走到头了，从栈中弹出节点并保存,然后转向右边节点，继续上面整个过程
            }
            TreeNode tmp = stack.peek();
            if(tmp.right != null && prev != tmp.right){
                cur = tmp.right;
            }else {
                res.add(tmp.val);
                prev = tmp;
                stack.pop();
            }

        }
        return res;
    }
}