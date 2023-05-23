#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_N 50
#define MAX_M 101
#define MAX_T 501

int missions[MAX_N][3];

int cache[MAX_N][MAX_T][MAX_M];

int max(int a, int b) {
    return a > b ? a : b;
}

int perform_missions(int money_cap, int time_cap, int mission_i) {
    if (money_cap == 0 || time_cap == 0 || mission_i == 0) {
        return 0;
    }

    if (cache[mission_i][time_cap][money_cap] != -1) {
        return cache[mission_i][time_cap][money_cap];
    }

    if (missions[mission_i - 1][0] > money_cap || missions[mission_i - 1][1] > time_cap) {
        int result = perform_missions(money_cap, time_cap, mission_i - 1);
        cache[mission_i][time_cap][money_cap] = result;
        return result;
    }

    int cost = missions[mission_i - 1][0];
    int time_consumed = missions[mission_i - 1][1];
    int rescues = missions[mission_i - 1][2];

    int perform_rescue = perform_missions(money_cap - cost, time_cap - time_consumed, mission_i - 1) + rescues;
    int dont_rescue = perform_missions(money_cap, time_cap, mission_i - 1);
    int result = max(perform_rescue, dont_rescue);

    cache[mission_i][time_cap][money_cap] = result;
    return result;
}

int main() {
    int M, T, N;
    scanf("%d%d%d", &M, &T, &N);

    memset(cache, -1, sizeof(cache));

    for (int i = 0; i < N; i++) {
        int cost, time_consumed, rescues;
        scanf("%d%d%d", &cost, &time_consumed, &rescues);
        missions[i][0] = cost;
        missions[i][1] = time_consumed;
        missions[i][2] = rescues;
    }

    int rescues = perform_missions(M, T, N);
    printf("%d\n", rescues);

    return 0;
}
