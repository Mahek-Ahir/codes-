#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    scanf("%d", &n);   // input number
    int sum = 0;

    while (n > 0) {
        sum += n % 10;  
        n = n / 10;      
    }

    printf("%d", sum);
    return 0;
}
