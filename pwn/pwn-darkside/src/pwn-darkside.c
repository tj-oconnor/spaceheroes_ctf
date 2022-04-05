#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <seccomp.h>
#include <sys/syscall.h>
#include <stdbool.h>

__attribute__((constructor)) void ignore_me() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

void print_flag() {
    printf("shctf{I_will_remov3_th3s3_restraints_and_leave_the_c3ll}\n");
}
void vuln() {
    char choice[28];
    printf("The Dark Side Of The Force, Are They. Easily They Flow, Quick To Join You In A Fight. The Dark Side resides at: %p\n",print_flag);
    puts("Jedi Mind tricks dont work on me >>> ");
    gets(choice);
}

int main(void) {
    vuln();
}
