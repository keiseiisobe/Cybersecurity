#include <stdint.h>
#include <stdio.h>
#include <string.h>

int main() {
  char* var1 = "__stack_check";
  printf("Please enter key: ");
  char var2[20];
  scanf("%19s", var2);
  if (strcmp(var1, var2) == 0)
    printf("Good job.\n");
  else
    printf("Nope.\n");
  return 0;
}
