package java_programs;
import java.util.*;

public class HANOI {
    public static List<Pair<Integer,Integer>> hanoi(int height, int start, int end) {
        ArrayList<Pair<Integer,Integer>> steps = new ArrayList<Pair<Integer,Integer>>();

        if (height > 0) {
            // Calculate the helper peg directly
            int helper = 6 - start - end; // Correctly calculates the helper peg
            steps.addAll(hanoi(height-1, start, helper));
            steps.add(new Pair<Integer,Integer>(start, end)); // Corrected to move from start to end
            steps.addAll(hanoi(height-1, helper, end));
        }

        return steps;
    }

    public static class Pair<F, S> {
        private F first; //first member of pair
        private S second; //second member of pair

        public Pair(F first, S second) {
            this.first = first;
            this.second = second;
        }

        public void setFirst(F first) {
            this.first = first;
        }

        public void setSecond(S second) {
            this.second = second;
        }

        public F getFirst() {
            return first;
        }

        public S getSecond() {
            return second;
        }

        @Override
        public String toString() {
            return "(" + String.valueOf(first) + ", " + String.valueOf(second) + ")";
        }
    }
}