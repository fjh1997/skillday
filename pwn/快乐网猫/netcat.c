#include <stdio.h>
#include <string.h>
#include <unistd.h>



int main() {
    setvbuf(stdout, NULL, _IONBF, 0);  // 关闭输出缓冲
    printf("flag{h4PpY_neTcat}\n");
    return 0;
}