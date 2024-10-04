package java_programs;

import java.util.*;

import java_programs.Node;
import java_programs.WeightedEdge;

public class MINIMUM_SPANNING_TREE {

    // // Assuming a basic structure for Node and WeightedEdge
    // static class Node {
    //     int id;
    //     // Additional fields and methods
    // }

    // static class WeightedEdge implements Comparable<WeightedEdge> {
    //     Node node1, node2;
    //     int weight;

    //     @Override
    //     public int compareTo(WeightedEdge other) {
    //         return Integer.compare(this.weight, other.weight);
    //     }
    // }

    public static Set<WeightedEdge> minimum_spanning_tree(List<WeightedEdge> weightedEdges) {
        Map<Node, Node> parent = new HashMap<>();
        Set<WeightedEdge> minSpanningTree = new HashSet<>();

        // Initialize each node's parent to itself
        for (WeightedEdge edge : weightedEdges) {
            parent.putIfAbsent(edge.node1, edge.node1);
            parent.putIfAbsent(edge.node2, edge.node2);
        }

        Collections.sort(weightedEdges);

        for (WeightedEdge edge : weightedEdges) {
            Node root1 = find(parent, edge.node1);
            Node root2 = find(parent, edge.node2);

            // BUG FIX: Compare root nodes for cycle detection
            if (!root1.equals(root2)) { 
                minSpanningTree.add(edge);
                // BUG FIX: Properly merge sets using union
                union(parent, root1, root2); 
            }
        }
        return minSpanningTree;
    }

    private static Node find(Map<Node, Node> parent, Node node) {
        if (parent.get(node) != node) {
            parent.put(node, find(parent, parent.get(node))); // Path compression
        }
        return parent.get(node);
    }

    private static void union(Map<Node, Node> parent, Node root1, Node root2) {
        parent.put(root1, root2);
    }
}