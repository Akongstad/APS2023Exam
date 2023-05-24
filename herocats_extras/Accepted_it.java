import java.util.Scanner;

public class Accepted_it {
    public static int performMissions(int moneyCap, int timeCap, int[][] missions) {
        int numMissions = missions.length;
        int[][] dp = new int[timeCap + 1][moneyCap + 1];

        for (int missionI = 1; missionI <= numMissions; missionI++) {
            int cost = missions[missionI - 1][0];
            int timeConsumed = missions[missionI - 1][1];
            int rescues = missions[missionI - 1][2];

            for (int t = timeCap; t >= timeConsumed; t--) {
                for (int m = moneyCap; m >= cost; m--) {
                    if (cost <= m && timeConsumed <= t) {
                        int performRescue = dp[t - timeConsumed][m - cost] + rescues;
                        int dontRescue = dp[t][m];
                        dp[t][m] = Math.max(performRescue, dontRescue);
                    }
                }
            }
        }

        return dp[timeCap][moneyCap];
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int M = scanner.nextInt();
        int T = scanner.nextInt();
        int N = scanner.nextInt();
        int[][] missions = new int[N][3];
        for (int i = 0; i < N; i++) {
            missions[i][0] = scanner.nextInt();
            missions[i][1] = scanner.nextInt();
            missions[i][2] = scanner.nextInt();
        }

        int rescues = performMissions(M, T, missions);
        System.out.println(rescues);
    }
}
