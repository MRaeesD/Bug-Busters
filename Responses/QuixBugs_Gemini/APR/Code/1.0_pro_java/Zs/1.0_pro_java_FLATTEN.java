// These lines mean that if x is not an ArrayList, then x is an element of some non-container type (e.g. String, Double, Integer). We should just add it to the result List.
if (!(x instanceof ArrayList)) {
            result.add(x);
            continue;
        }
// The code below remains pretty much the same.
        result.addAll((ArrayList) flatten(x));
        return result;
