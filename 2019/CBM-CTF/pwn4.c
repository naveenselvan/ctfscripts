#include<stdio.h>
int main()
{
 char buf; // [rsp+0h] [rbp-40h]
  int v5; // [rsp+38h] [rbp-8h]
  int v6; // [rsp+3Ch] [rbp-4h]

  puts("enter a number\n");
//  fflush(_bss_start);
  __isoc99_scanf("%d", &v5);
  printf("v5 @%p:\n",&v5);
printf("v6 @%p:\n",&v6);

printf("v6 value before read%d:\n",v6);
  v6 = open("flag", 0);
printf("v6 value after read %d\n",v6);
printf("%d\n",v6);
printf("The input for the binary is%d\n",v6+1085645);
  read(v6 , &buf, 23uLL);
  puts(&buf);
  return 0;
}
