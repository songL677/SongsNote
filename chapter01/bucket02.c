#include<stdio.h>
int main(){
    int book[1001],i,j,t,n;
    for(i=1;i<1001;i++){
        book[i]=0;
    }
    scanf("%d",&n);
    //输入n个数
    for(i=1;i<=n;i++){
        scanf("%d",&t);
        book[t]++;

    }
    for(i=1001;i>0;i--){
        for(j=1;j<=book[i];j++){
            printf("%d ",i);
        }
    }
    return 0;
}