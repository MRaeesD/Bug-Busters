package java_programs;
import java.util.*;

public class SHORTEST_PATHS {

    final static int INF = 99999;

    public static Map<String, Integer> shortest_paths(String source, Map<List<String>, Integer> weight_by_edge) {
        Map<String, Integer> weight_by_node = new HashMap<>();

        // Initialize the weights to infinity
        for (List<String> edge : weight_by_edge.keySet()) {
            weight_by_node.put(edge.get(0), INF);
            weight_by_node.put(edge.get(1), INF);
        }

        // Set the source node weight to 0
        weight_by_node.put(source, 0);

        // Number of nodes
        int numberOfNodes = weight_by_node.size();

        // Relax edges |V| - 1 times
        for (int i = 0; i < numberOfNodes - 1; i++) {
            for (List<String> edge : weight_by_edge.keySet()) {
                String u = edge.get(0);
                String v = edge.get(1);
                int weight = weight_by_edge.get(edge);

                // Relaxation step
                if (weight_by_node.get(u) != INF && weight_by_node.get(u) + weight < weight_by_node.get(v)) {
                    weight_by_node.put(v, weight_by_node.get(u) + weight);
                }
            }
        }
        return weight_by_node;
    }

    public static Map<String, Integer> shortest_paths(Node source, List<WeightedEdge> weight_by_edge) {
        Map<String, Integer> weight_by_node = new HashMap<>();

        // Initialize node weights
        for (WeightedEdge edge : weight_by_edge) {
            weight_by_node.put(edge.node1.toString(), INF);
            weight_by_node.put(edge.node2.toString(), INF);
        }
        weight_by_node.put(source.toString(), 0);

        // Relax all edges |V| - 1 times
        for (int i = 0; i < weight_by_node.size() - 1; i++) {
            for (WeightedEdge edge : weight_by_edge) {
                String u = edge.node1.toString();
                String v = edge.node2.toString();

                // Relaxation step
                if (weight_by_node.get(u) != INF && 
                    weight_by_node.get(u) + edge.weight < weight_by_node.get(v)) {
                    weight_by_node.put(v, weight_by_node.get(u) + edge.weight);
                }
            }
        }

        return weight_by_node;
    }
}