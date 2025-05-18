#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void no() {
  printf("Nope.\n");
  exit(1);
}

void yes() {
  printf("Good job.\n");
}

int main() {
  printf("Please enter key: ");
  char str2[30];
  if (scanf("%29s", str2) != 1)
    no();
  if (str2[0] != 0x30)
    no();
  if (str2[1] != 0x30)
    no();
  fflush(NULL);
  char str[9];
  memset(str, 0, 9);
  str[0] = 'd';
  size_t i = 1;
  size_t i2 = 2;
  size_t len = strlen(str2);
  printf("len: %lu\n", len);
  while (i2 + 2 < len) {
    printf("i2: %lu\n", i2);
    char str3[4];
    size_t i3 = 0;
    str3[i3] = str2[i2];
    str3[i3 + 1] = str2[i2 + 1];
    str3[i3 + 2] = str2[i2 + 2];
    str3[i3 + 3] = '\0';
    str[i] = atoi(str3);
    i++;
    i2 += 3;
    if (strlen(str) >= 8)
      break;
  }
  printf("%s: %lu bytes\n", str, strlen(str));
  if (strcmp(str, "delabere") == 0)
    yes();
  else
    no();
  return 0;
}
