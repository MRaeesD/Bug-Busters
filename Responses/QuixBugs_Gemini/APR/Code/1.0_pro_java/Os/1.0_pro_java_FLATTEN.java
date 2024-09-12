if (arr instanceof ArrayList) {
                    ArrayList narr = (ArrayList) arr;
                    ArrayList result = new ArrayList(50);
                    for (Object x : narr) {
                        if (x instanceof ArrayList) {
                            result.addAll((ArrayList) flatten(x));
                        } else {
                            result.add(x); // Changed line
                        }
                    }
                    return result; // Changed line
                } else {
                    return arr;
                }
