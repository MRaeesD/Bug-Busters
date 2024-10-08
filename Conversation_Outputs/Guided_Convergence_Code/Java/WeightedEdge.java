package java_programs;
import java.util.*;

public class WeightedEdge implements Comparable<WeightedEdge> {
    public Node node1;
    public Node node2;
    public int weight;

    public WeightedEdge() {
        node1 = null;
        node2 = null;
        weight = 0;
    }

    public WeightedEdge(Node node1, Node node2, int weight) {
        if (node1 == null || node2 == null) {
            throw new IllegalArgumentException("Nodes cannot be null");
        }
        this.node1 = node1;
        this.node2 = node2;
        this.weight = weight;
    }

    public int compareTo(WeightedEdge compareNode) {
        // Removed unnecessary cast.
        int compareWeight = compareNode.weight;

        return this.weight - compareWeight;
    }

    // Overriding equals() and hashCode() for consistency and potential use in collections
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        WeightedEdge that = (WeightedEdge) obj;
        return weight == that.weight &&
               Objects.equals(node1, that.node1) &&
               Objects.equals(node2, that.node2);
    }

    @Override
    public int hashCode() {
        return Objects.hash(node1, node2, weight);
    }
}