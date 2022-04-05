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

int ret_rocket() {
    asm("pop %rax; ret;");
}

void print_logo() {
    printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKOxdoollldKW\n");
    printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0xoccccldxkOOx;;0\n");
    printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXOoc::c'.c0WMMMMMMWd'x\n");
    printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXkoc:cokKNMNx;;dXMMMMMWl'k\n");
    printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOdc:cokXWMMMMMMMNx;;dXMMM0,:X\n");
    printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXkl::lkXWMMMMMMMMMMMMMNx;;dXNl'xW\n");
    printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKxc:cd0NMMMMWX00KXWMMMMMMMMNx;;:.lNM\n");
    printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWKxc:cxKWMMMMW0o::ccc:cdKWMMMMMMMXl.;KMM\n");
    printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOl;;cxXWMMMMMMNd,cOXWWWXk:,xWMMMMMMK;,OMMM\n");
    printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO:.:x0WMMMMMMMMMk'lNMMMMMMMX:,0MMMMMX:'kWMMM\n");
    printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXo,'.,clo0WMMMMMMWo.xMMMMMMMMWo.kMMMMXc'xWMMMM\n");
    printf("MMMMMMMMMMMMMMMMMMMMMMWKkollodOXW0;,kX0kko.;KWWMMMMM0,;0WMMMMMWO,:KMMMXc'xWMMMMM\n");
    printf("MMMMMMMMMMMMMMMMMMMMNkc;coxxdoc:;';0MMMMMNo,:;lKMMMMW0c,lx00Oxc,lKMMMXc'xWMMMMMM\n");
    printf("MMMMMMMMMMMMMMMMMMW0c,oKWMMMMMNd.;KMMMMMMMWNKc.lOKNMMMN0dlcccld0WMMMK:'kWMMMMMMM\n");
    printf("MMMMMMMMMMMMMMMMMWk,:0WMMMMMMMO,;KMMMMMMMMMMM0oc;'dWMMMMMMWWWMMMMMM0:,kWMMMMMMMM\n");
    printf("MMMMMMMMMMMMMMMMWd'lXMMMMMMMMK;,OMMMMMMMMMMMMMMM0,'ld0WMMMMMMMMMMWO;;0WMMMMMMMMM\n");
    printf("MMMMMMMMMMMMMMMWx'lXMMMMMMMMNl.xWMMMMMMMMMMMMMMMW0xo.,0WMMMMMMMMWx,cKMMMMMMMMMMM\n");
    printf("MMMMMMMMMMMMMMMO,:XMMMMMMMWWk'cNMMMMMMMMMMN0KMMMMMMWd,::lKMMMMMXl'oXMMMMMMMMMMMM\n");
    printf("MMMMMMMMMMMMMMNc'OMMMMWKxcc:.,0MMMMMMMMXKx;:OWMMMMMMWXKl.l0XWWO:;kWMMMMMMMMMMMMM\n");
    printf("MMMMMMMMMMMMMMk'cNMMMNx,;xO:.oWMMMMMMNx;';dXMMMMMMMMMMMKlc:'cl,cKMMMMMMMMMMMMMMM\n");
    printf("MMMMMMMMMMMMMMO,;kNMXl'oNMWx':0WMMMXx;;d0XMMMMMMMMMMMMMMMNx..:kNMMMMMMMMMMMMMMMM\n");
    printf("MMMMMMMMMMMMMMWKo,:xc'dWMMMWOc,lKXx;;dXMMMMMMMMMMMMMMMWKx:;cONMMMMMMMMMMMMMMMMMM\n");
    printf("MMMMMMMMMMMMNkoOWKo''dWMMMMMMWO;..'dXMMMMMMMMMMMMMWXko;;cxKWMMMMMMMMMMMMMMMMMMMM\n");
    printf("MMMMMMMMMMNk:;dXMMWXKWMMMMMMMNx;,,,lKWMMMMMMWNKOdl::c:.;0MMMMMMMMMMMMMMMMMMMMMMM\n");
    printf("MMMMMMMMNk:;oKMMMMMMMMMMMMMNx;;dXNOc,lO0Okdlcccclx0XWWk'cXMMMMMMMMMMMMMMMMMMMMMM\n");
    printf("MMMMMMNk:;oXMMMMMMMMMMMMMWk;;dXMMMMWOlcc:'.:OKNWMMMMMMNc'OMMMMMMMMMMMMMMMMMMMMMM\n");
    printf("MMMMNk:;oXMMMW0x0WMMMMMMMNkxXMMMMMMMMWWX0l.xWMMMMMMMMMX;,0MMMMMMMMMMMMMMMMMMMMMM\n");
    printf("MMNk:;oKMMMW0l,cKMMMMNXWMMMMMMMMMMMMN0d:,;xNMMMMMMMMWKc'xWMMMMMMMMMMMMMMMMMMMMMM\n");
    printf("Nk:;oXMMMW0l,cOWMMMXd;oXMMMMMMMMN0xl::lkKXMMMMMMMMNOl;cOWMMMMMMMMMMMMMMMMMMMMMMM\n");
    printf("KodXMMMW0l,cOWMMMXd;;xNMMMMMMMMM0;.,kNWMMMMMMMWXOo::lOWMMMMMMMMMMMMMMMMMMMMMMMMM\n");
    printf("MMMMMW0l,cOWMMMXd;;xNMMMWWMMMMMMWKo,:kNWWNKOxlc::oOXWMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
    printf("MMMW0l,cOWMMMXd;;xNMMMWOlxNMMMMWKOKKo;:cccccldOXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
    printf("MW0l,cOWMMMXd;;xNMMMWOc,lKWMMWKo,cKMWX00KXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
    printf("M0ccOWMMMXd;;xNMMMWOc,lKWMMWKo,:kNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
    printf("MWNWMMMXd;;xNMMMWOc,lKWMMWKo;:kNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
    printf("MMMMMXd;;xNMMMWOc,lKWMMMKo,:kNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
    printf("MMMXd;;xNMMMWOc,lKWMMWKo,:kNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
    printf("MXd;;xXMMMWOc,lKWMMWKo,:kNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
    printf("M0oxXMMMMMNxoKWMMMMO::kNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/bin/sh\n");
    printf("MMMMMMMMMMMMMMMMMMMKONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMflag.txt\n");
}

void print_cpu_details() {
    unsigned cpu, node;
    syscall(SYS_getcpu, &cpu, &node, NULL);
    printf("<<< This program is running on CPU core %u and NUMA node %u.\n\n", cpu, node);
}

int ret_control() {
    asm("pop %rdx; ret;");
}

int ret_throttle() {
    asm("pop %r10; ret;");
}

int ret_ignition() {
    asm("pop %r8; ret;");
}

int ret_signal() {
    asm("syscall; ret;");
}

int mov_rocket() {
    asm("mov %rsi, %rax; ret;");
}

void secure() {
    scmp_filter_ctx ctx;
    ctx = seccomp_init(SCMP_ACT_ALLOW);
    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(execve), 0);
    seccomp_load(ctx);
}

void vuln() {
    char name[28];
    char choice[28];

    puts("Please authenticate >>>");
    gets(name);
    printf("<<< Welcome: ");
    printf(name);
    printf("\n");

    puts("Welcome To Mission Control. Tell me to do something >>>");
    gets(choice);
    if (strcmp(choice, "CPU") == 0) {
        print_cpu_details();
    }
    else if (strcmp(choice, "LOGO") == 0) {
        print_logo();
    }
    else {
        printf("<<< Invalid Command.\n");
    }
}

int main(void) {
    secure();
    vuln();
}
