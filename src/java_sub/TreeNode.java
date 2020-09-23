package java_sub;

import java.util.Scanner;

//    Definition for a binary tree node.
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }

    /**
     * 前序递归构造二叉树 root->left->right
     * @param scanner 输入流，用于读取节点值
     * @return 构造完成的二叉树的根节点
     */
    public static TreeNode createTreeNode(Scanner scanner) {
        assert scanner!=null;
        TreeNode root = null;                 //声明当前根节点
        int data = scanner.nextInt();
        if (data > 0) {                             //若当前节点存在（这里为了简单以负数为占位符）
            root = new TreeNode(data);              //使用其它顺序构造二叉树，只需更改这三句即可
            root.left = createTreeNode(scanner);
            root.right = createTreeNode(scanner);
        }
        return root;
    }
}