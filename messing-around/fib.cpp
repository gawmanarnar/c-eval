#include <stdio.h>

int fibrec(int n) {
  if(n==0){ return 0; }
  if(n==1){ return 1; }
  
  return fibrec(n-2) + fibrec(n-1);
}

int fib(int n) {
  int fibnums[n];
  fibnums[0] = 0;
  fibnums[1] = 1;
  
  for(int i = 2; i <= n; i++) {
    fibnums[i] = fibnums[i-2] + fibnums[i-1];
  }

  return fibnums[n];
}

int main() {
  printf("%d\n",fibrec(4));
  printf("%d\n",fib(4));
}
