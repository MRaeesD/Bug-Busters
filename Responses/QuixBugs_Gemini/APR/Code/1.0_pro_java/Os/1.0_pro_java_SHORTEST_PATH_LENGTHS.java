int update_length = Math.min(length_by_path.get(Arrays.asList(i,j)),
                                                 sumLengths(length_by_path.get(Arrays.asList(i,k)),
                                                            length_by_path.get(Arrays.asList(k,j)))); //k has been replaced with j here
                    length_by_path.put(Arrays.asList(i,j), update_length);
