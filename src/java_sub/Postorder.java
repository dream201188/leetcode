package java_sub;


import java.util.*;

public class Postorder {
    public List<Integer> postorderTraversal(TreeNode root) {
        LinkedList<TreeNode> stack = new LinkedList<>();
        LinkedList<Integer> output = new LinkedList<>();
        if (root == null) {
            return output;
        }

        stack.add(root);
        while (!stack.isEmpty()) {
            TreeNode node = stack.pollLast();
            output.addFirst(node.val);
            if (node.left != null) {
                stack.add(node.left);
            }
            if (node.right != null) {
                stack.add(node.right);
            }
        }
        return output;
    }
    public static void main(String []args){
        Scanner sc = new Scanner(System.in);
        TreeNode root = TreeNode.createTreeNode(sc);
        sc.close();
        Postorder postorder = new Postorder();
        List<Integer> res = postorder.postorderTraversal(root);
        System.out.println(res);
    }
}

