public static int find_first_in_sorted(int[] arr, int x) {
                    int lo = 0;
                    int hi = arr.length; // Change made here

                    while (lo < hi) { // Change made here
                        int mid = (lo + hi) / 2; // check if this is floor division

                        if (x == arr[mid] && (mid == 0 || x != arr[mid-1])) {
                            return mid;
                        } else if (x <= arr[mid]) {
                            hi = mid;
                        } else {
                            lo = mid + 1;
                        }
                    }

                    return -1;
                }
