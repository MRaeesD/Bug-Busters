ArrayList<ArrayList> output = new ArrayList<ArrayList>(100);
for (ArrayList subset : rest_subsets) {
    ArrayList new_subset = new ArrayList(100); // Change here
    new_subset.add(first); // Change here
    new_subset.addAll(subset);
    output.add(new_subset);
}
