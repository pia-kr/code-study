#include<stdio.h>
int main(){
    int H,M;
    scanf("%d %d",&H, &M);
    if(M>=45){
        M = M-45;
    }   
    else{
        M = 60-(45-M);
        if(H==0){
            H = 23;
        }
        else{
            H = H-1;
        }
    }
    printf("%d %d",H,M);
    return 0;
            
}