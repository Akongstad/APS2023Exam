import java.util.*;

public class Accepted {
    static int[][] missions;
    static int[][][] cache;

    public static int performMissions(int moneyCap, int timeCap, int missionI) {
        if (moneyCap == 0 || timeCap == 0 || missionI == 0) {
            return 0;
        }

        if (cache[missionI][timeCap][moneyCap] != -1) {
            return cache[missionI][timeCap][moneyCap];
        }

        if (missions[missionI-1][0] > moneyCap || missions[missionI-1][1] > timeCap) {
            int result = performMissions(moneyCap, timeCap, missionI - 1);
            cache[missionI][timeCap][moneyCap] = result;
            return result;
        }

        int cost = missions[missionI-1][0];
        int timeConsumed = missions[missionI-1][1];
        int rescues = missions[missionI-1][2];

        int performRescue = performMissions(moneyCap - cost, timeCap - timeConsumed, missionI - 1) + rescues;
        int dontRescue = performMissions(moneyCap, timeCap, missionI - 1);
        int result = Math.max(performRescue, dontRescue);

        cache[missionI][timeCap][moneyCap] = result;
        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int M = sc.nextInt();
        int T = sc.nextInt();
        int N = sc.nextInt();

        missions = new int[N][3];
        cache = new int[N+1][T+1][M+1];
        for (int[][] layer2d : cache) {
            for (int[] layer1d : layer2d) {
                Arrays.fill(layer1d, -1);
            }
        }

        for (int i = 0; i < N; i++) {
            int cost = sc.nextInt();
            int timeConsumed = sc.nextInt();
            int rescues = sc.nextInt();
            missions[i][0] = cost;
            missions[i][1] = timeConsumed;
            missions[i][2] = rescues;
        }

        int rescues = performMissions(M, T, N);
        System.out.println(rescues);
    }
}
