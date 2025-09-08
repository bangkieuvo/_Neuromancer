#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv) {
   char *in =  malloc(18);
   char *out =  malloc(18);
    strcpy(out,"Sample Output");
    printf("%p: %s\n",out,out);
return 0;
}
