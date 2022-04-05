#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/syscall.h>

__attribute__((constructor)) void ignore_me() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

void print_logo() {
    printf("                                                                           \n");
    printf("                                                      llllooooooolllllll   \n");
    printf("                                              llloodddddddddddddoooooooooll\n");
    printf("                                       lllloooddddddddddddddddooooooooooool\n");
    printf("                                  llooodddddddddxxxxxkkkkkkxxddoooooooolll \n");
    printf("                             lloooddddddxxxxkOOOOOO000000OOkxxdddoooolllll \n");
    printf("                        llloodddddxxxkkOOO0000000KKKKKK000Okxddddoooolll   \n");
    printf("                     lllooddxxxxkkOOOOO0000OOOOOOOOO00KK00Oxddddddoooll    \n");
    printf("                  llloodxxxxkkOOOOOOkkxdddoooolllllloxO000kxddoddddoll     \n");
    printf("               lloooodxkkkOOOOOOkdol         ''....'  x00Oxdddoooooll      \n");
    printf("             looooodxkOOOOOkxdol   '''.........     . kOkxddoooooll        \n");
    printf("          llooooddxkOO00Okdl   '.........            xOkxddooooool         \n");
    printf("        loooooddxkOOOOkxo  '..... ....            . xkxdoooooool           \n");
    printf("      looooddxxkkOOOOxl  .......                . oxxdooooolll             \n");
    printf("    loddddddxxxkOOOkd  ...                    ' oxxdooooooll               \n");
    printf("   lodddoddxxxkOO0Oxl '.                  .' ldxddoooooolll                \n");
    printf("  loodddoddxxkkOOOOxo  ..           ..'   odddddoooooooll                  \n");
    printf(" lodddddoddxxkkkOOOOkdl  '......'   odxxdddddoooooolll                     \n");
    printf("lloddddddooddxxxxkkkOkkkkxxxddddxxxxxxdddooooollll                         \n");
    printf("llooddddddddddddxxxxxxxxxxxdddddddddddoooolllll                            \n");
    printf("llloooooooooooddddxxxxxxxdddddddoooollll l                                 \n");
    printf("ooooooooddddddddxddddddddddooolll  lll                                     \n");
    printf("looooooooooooooooooooooollll                                               \n");
    printf("    llllllooooolllll                                                       \n");
    printf("       lllll                                                               \n");
}

void vuln() {
    char buffer[28];
    printf("\n>>> ");
    gets(buffer);
    printf("\n<<< You say: ");
    printf(buffer);
}

void make_writable_mem() {
    syscall(0x9, 0x666000, 0x1000, 3, 0x22, 0xffffffff, 0);
}

void ret_syscall() {
    asm("syscall; ret;");
}

void pop_rax() {
    asm("pop %rax; ret;");
}

int main() {
    print_logo();
    make_writable_mem();
    printf("----------------------------------------------------------------------------\n");
    printf(" ~ Welcome to Black Hole ROP ~ \n");
    printf("----------------------------------------------------------------------------\n");
    printf("<<< Address of syscall, ret    : %p\n", 0x4013bb);
    printf("<<< Address of writable memory : %p\n", 0x666000);
    printf("<<< Address of pop rax, ret    : %p\n", 0x4013c5);
    printf("----------------------------------------------------------------------------\n");

    while (1) {
        vuln();
    }
}
