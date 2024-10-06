java
update_weight = Math.min(
                        weight_by_node.get(edge.get(0))
                                + weight_by_edge.get(edge),
                        weight_by_node.get(edge.get(1)));
                weight_by_node.put(edge.get(1), update_weight);

java
int update_weight = Math.min(
                        weight_by_node.get(edge.node1.toString())
                                + edge.weight,
                        weight_by_node.get(edge.node2.toString()));
                weight_by_node.put(edge.node2.toString(), update_weight);
