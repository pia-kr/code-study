#include<stdio.h>
int main(){
    int t,m,a,b;
    scanf("%d %d",&t,&m);
    scanf("%d",&a);
    if((m+a)>=60){
        b = (m+a)/60;
        m = (m+a)-(60*b);
        if (t+b>23){
            t = t+b-24;
        }
        else{
            t = t+b;
        }
    }
    else{
        m = m+a;
    }
    printf("%d %d",t,m);
    return 0;
}