package java_sub;


import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.Stack;

public class Inorder2 {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        Stack<TreeNode> stack = new Stack<TreeNode>();
        while (stack.size() > 0 || root != null) {
            while (root != null) {
                stack.add(root);
                root = root.left;
                //当前节点为空，说明左边走到头了，从栈中弹出节点并保存
                //然后转向右边节点，继续上面整个过程
            }
            TreeNode tmp = stack.pop();
            res.add(tmp.val);
            root = tmp.right;
        }
            return res;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        TreeNode root = TreeNode.createTreeNode(sc);
        sc.close();
        Inorder2 postorder = new Inorder2();
        List<Integer> res = postorder.inorderTraversal(root);
        System.out.println(res);

    }
}

