if (heap.size() > k) heap.poll(); // Added break condition
            heap.add(x);
            Integer popped = heap.poll();
            output.add(popped);
        }
