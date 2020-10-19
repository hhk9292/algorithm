// SWEA 2071


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

class Solution {
    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String args[]) throws Exception {
        int T = Integer.parseInt(bf.readLine());
        for (int tc = 1; tc <= T; tc++) {
            String[] s = bf.readLine().split(" ");
            int sum = 0;
            for (int i = 0; i < s.length; i++) {
                int num = Integer.parseInt(s[i]);
                sum += num;
            }
            bw.write("#" + tc + " " + (int)Math.round(sum/10.0) + '\n');
        }
        bw.flush();
        bw.close();
    }
}
