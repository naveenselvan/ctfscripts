#include<stdio.h>
#include<string.h>
void fun(char **temp)
{
char b='S';
*temp=&b;
printf("Inside Function : %c\n",b);
printf("Inside Function temp : %s\n",*temp); 
}



int main()
{
char *a;
fun(&a);
printf("Outside Temp : %s",a);
}
