#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX(a, b) ((a) > (b) ? (a) : (b))

int perform_missions(int money_cap, int time_cap, int mission_i, int missions[][3], int** cache[], int min_cost, int min_time) {
    if (cache[mission_i][time_cap][money_cap] != -1) {
        return cache[mission_i][time_cap][money_cap];
    }

    if (min_cost > money_cap || min_time > time_cap) {
        return 0;
    }

    if (mission_i == 0 || money_cap == 0 || time_cap == 0) {
        cache[mission_i][time_cap][money_cap] = 0;
        return 0;
    }

    int cost = missions[mission_i - 1][0];
    int time_consumed = missions[mission_i - 1][1];
    int rescues = missions[mission_i - 1][2];

    if (cost > money_cap || time_consumed > time_cap) {
        int result = perform_missions(money_cap, time_cap, mission_i - 1, missions, cache, min_cost, min_time);
        cache[mission_i][time_cap][money_cap] = result;
        return result;
    }

    int perform_rescue = perform_missions(money_cap - cost, time_cap - time_consumed, mission_i - 1, missions, cache, min_cost, min_time) + rescues;
    int dont_rescue = perform_missions(money_cap, time_cap, mission_i - 1, missions, cache, min_cost, min_time);
    int result = MAX(perform_rescue, dont_rescue);

    cache[mission_i][time_cap][money_cap] = result;
    return result;
}

int main() {
    int M, T, N;
    scanf("%d %d %d", &M, &T, &N);
    int missions[N][3];
    int min_cost = T;
    int min_time = M;
    for (int i = 0; i < N; i++) {
        scanf("%d %d %d", &missions[i][0], &missions[i][1], &missions[i][2]);
        if (min_time > missions[i][1]) {
            min_time = missions[i][1];
        }
        if (min_cost > missions[i][0]) {
            min_cost = missions[i][0];
        }
    }

    int*** cache = (int***)malloc((N + 1) * sizeof(int**));
    for (int i = 0; i <= N; i++) {
        cache[i] = (int**)malloc((T + 1) * sizeof(int*));
        for (int j = 0; j <= T; j++) {
            cache[i][j] = (int*)malloc((M + 1) * sizeof(int));
            memset(cache[i][j], -1, (M + 1) * sizeof(int));
        }
    }

    int rescues = perform_missions(M, T, N, missions, cache, min_cost, min_time);
    printf("%d\n", rescues);

    // Free memory
    for (int i = 0; i <= N; i++) {
        for (int j = 0; j <= T; j++) {
            free(cache[i][j]);
        }
        free(cache[i]);
    }
    free(cache);

    return 0;
}
