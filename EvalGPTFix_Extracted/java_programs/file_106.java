import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;
import java.util.stream.Stream;

import static java.util.stream.Collectors.toList;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        List<Long> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                .map(Long::parseLong)
                .collect(toList());
        long A = arr.get(0);
        long B = arr.get(1);
        long res = 0;
        while (A != B){
            if (A < B) {
                long tmp = A;
                A = B;
                B = tmp;
            }
            long diff = A - B;
            diff += (B - (diff % B)); //bug
            A -= diff;
            res += diff/B;
        }
        System.out.println(res);
    }
}

