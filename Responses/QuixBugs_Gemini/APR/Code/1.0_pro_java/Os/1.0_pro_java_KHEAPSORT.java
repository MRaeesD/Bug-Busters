for (Integer x : arr) {
        if (heap.size() > k) {    // Change here
            heap.poll();
        }
        heap.add(x);
        Integer popped = heap.poll();
        output.add(popped);
