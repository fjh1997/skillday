#include <stdio.h>
#include <string.h>
#include <unistd.h>

void win() {
    printf("\nCongratulations! You've successfully exploited the stack overflow!\n");
    execve("/bin/sh", NULL, NULL);
}

void vulnerable_function() {
    char buffer[64];
    printf("Enter your payload: ");
    gets(buffer);  // 明显的栈溢出漏洞
    printf("You entered: %s\n", buffer);
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);  // 关闭输出缓冲
    printf("Welcome to the Stack Overflow Challenge!\n");
    vulnerable_function();
    return 0;
}