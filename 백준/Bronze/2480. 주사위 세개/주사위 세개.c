// Created on iPad Pro (12.9-inch) (5th generation).

#include <stdio.h>

int main() {
   int a,b,c,m;
   scanf("%d %d %d",&a,&b,&c);
   if(a==b && a==c){
      m=10000+1000*a;
   }
   else if(a==b||a==c){
      m=1000+100*a;
   }
   else if(b==c){
      m=1000+100*b;
   }
   else{
      if (a > b && a > c)
         m = 100*a;

      else if (b > a && b > c)
         m = 100*b;

      else
         m = 100*c;
   }
   printf("%d",m);
   return 0;
}