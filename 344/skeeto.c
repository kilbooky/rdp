/* skeeto's c soln */
#include <stdio.h>

static int
baum_sweet(unsigned long long n)
{
    for (int run = 0; n; n >>= 1) {
        if (n & 1ULL) {
            if (run % 2 == 1)
                return 0;
            run = 0;
        } else {
            run++;
        }
    }
    return 1;
}

int
main(void)
{
    unsigned long long last;
    scanf("%llu", &last);

    putchar('1');
    for (unsigned long long i = 1; i <= last; i++)
        printf(", %d", baum_sweet(i));
    putchar('\n');
}