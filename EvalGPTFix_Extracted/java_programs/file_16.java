import java.util.*;

import java.io.*;
import java.math.BigInteger;
import java.nio.charset.StandardCharsets;

public class Main {

	public static void main(String[] args) throws IOException {
		InputStreamReader reader = new InputStreamReader(System.in, StandardCharsets.UTF_8);
		BufferedReader in = new BufferedReader(reader);
		Main ins = new Main(in);
		ins.calc();
		ins.showResult();
	}

	static class Query {
		int type;
		int i;

		Query(String line) {
			String[] tokens = line.split(" ");
			this.type = Integer.parseInt(tokens[0]);
			if (this.type == 1) {
				this.i = Integer.parseInt(tokens[1]);
			}
		}
	}

	PrintWriter writer = new PrintWriter(System.out);
	BufferedReader in = null;
	int Q;
	Query[] queries;
	long MOD = 998244353L;
	Deque<Integer> deque = new ArrayDeque<>();
	long[] mods = new long[1000001];

	Main(BufferedReader in) throws IOException {
		this.Q = Integer.parseInt(in.readLine());
		this.queries = new Query[Q];
		for (int i = 0; i < Q; ++i) {
			this.queries[i] = new Query(in.readLine());
		}

		mods[1] = 1L;
		for (int i = 2; i < mods.length; ++i) {
			long val = mods[i - 1] * 10L;
			val %= MOD;
			mods[i] = val;
		}
	}

	void calc() {
		deque.add(1);
		long val = 1L;
		for (int i = 0; i < Q; ++i) {
			Query query = this.queries[i];
			if (query.type == 1) {
				deque.addLast(query.i);
				val *= 10L;
				val += (long) query.i;
				val %= MOD;
			} else if (query.type == 2) {
				int len = deque.size();
				long m = mods[len] * deque.pollFirst();
				val -= m;
				val += MOD; //bug
				val %= MOD;
			} else {
				this.writer.println(val);
			}
			
		}
	}

	void showResult() {
		this.writer.flush();
	}

}

