#include <stdio.h>
#include <time.h>

int main() {
    time_t now; 
    now = time(NULL);
    printf("run time: %ld\n", now);
    return 0;
}