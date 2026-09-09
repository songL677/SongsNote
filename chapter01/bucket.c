#include<stdio.h>
int main(){
    int a[11],i,j,t;
    for(i=1;i<11;i++){
        a[i] = 0;
    }
    for(i=1;i<=5;i++){
        scanf("%d",&t);
        a[t]++;
    }
    //遍历数组然后shuchucishu   
    for(i=1;i<11;i++){
        for(j=1;j<=a[i];j++){
            printf("%d ",i);
        }
    }
    return 0;

}
