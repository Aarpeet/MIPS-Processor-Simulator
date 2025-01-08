#include<stdio.h>
int main(){
    int n;
    scanf("%d",&n);
    int res = 0;
    for(int i = 1;i<=n;i++){
        res += i;
    }
    int mean = res/n;
    printf("%d",mean);
}