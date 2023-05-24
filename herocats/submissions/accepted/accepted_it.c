#include <stdio.h>

int perform_missions(int money_cap, int time_cap, int num_missions, int missions[num_missions][3]) {
    int dp[time_cap + 1][money_cap + 1];

    for (int i = 0; i <= time_cap; i++) {
        for (int j = 0; j <= money_cap; j++) {
            dp[i][j] = 0;
        }
    }

    for (int mission_i = 1; mission_i <= num_missions; mission_i++) {
        int cost = missions[mission_i - 1][0];
        int time_consumed = missions[mission_i - 1][1];
        int rescues = missions[mission_i - 1][2];

        for (int t = time_cap; t >= time_consumed; t--) {
            for (int m = money_cap; m >= cost; m--) {
                if (cost <= m && time_consumed <= t) {
                    int perform_rescue = dp[t - time_consumed][m - cost] + rescues;
                    int dont_rescue = dp[t][m];
                    dp[t][m] = (perform_rescue > dont_rescue) ? perform_rescue : dont_rescue;
                }
            }
        }
    }

    return dp[time_cap][money_cap];
}

int main() {
    int M, T, N;
    scanf("%d %d %d", &M, &T, &N);

    int missions[N][3];
    for (int i = 0; i < N; i++) {
        scanf("%d %d %d", &missions[i][0], &missions[i][1], &missions[i][2]);
    }

    int rescues = perform_missions(M, T, N, missions);
    printf("%d\n", rescues);

    return 0;
}
