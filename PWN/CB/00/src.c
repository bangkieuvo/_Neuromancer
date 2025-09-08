#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>

int main(int argc, char **argv) {
   char *in = (char*) malloc(18);
   char *out =  (char*)malloc(18);
    strcpy(out,"Sample Output");
    printf("%p: %s\n",out,out);
return 0;
}
