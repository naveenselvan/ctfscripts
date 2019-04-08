#include<stdio.h>

int main()

{
 int seed; // [rsp+8h] [rbp-8h]
  signed int i; // [rsp+Ch] [rbp-4h]
  signed int j; // [rsp+Ch] [rbp-4h]
int q;
  srand(2109);
  for ( i = 0; i <= 9; ++i )
    seed = rand();
  srand(seed);
  for ( j = 0; j <= 19; ++j )
    q=rand();
    printf("The input to the remote server is  %d",q);

return 0;
}
