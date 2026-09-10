#include<stdio.h>

int a[101],n;
void quicksort(int left,int right){
    int i,j,t,k;
    if(left>right)
        return;
    t = a[left];
    i = left;
    j = right;
    while(i!=j){
        while(a[j]>=t && i<j)
            j--;
        while(a[i]<=t && i<j)
            i++;
        if(i<j){
            k=a[i];
            a[i] = a[j];
            a[j] = k;
        }
        a[left] = a[i];
        a[i] = t;
    }
    quicksort(left,i-1);
    quicksort(i+1,right);


}
int main(){
    int i;
    scanf("%d",&n);
    for(i=1;i<n;i++){
        scanf("%d",&a[i]);

    }
    quicksort(1,n);
    printf("done!");
    for(i=1;i<=n;i++)
        printf("%d ",a[i]);
    
    return 0;
}
