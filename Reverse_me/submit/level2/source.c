#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void no() {
  printf("Nope.");
  exit(1);
}

int main() {
  printf("Please enter key: ");
  char v[20];
  if (scanf("%19s", v) != 1)
    no();
  if (v[0] != 0x30)
    no();
  if (v[1] != 0x30)
    no();
  fflush(NULL);
  char buffer[9];
  memset(buffer, 0, 9);
  while (1) {
    
  }
}
