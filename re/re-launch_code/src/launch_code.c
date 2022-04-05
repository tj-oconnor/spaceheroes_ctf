#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>
#include <unistd.h>
#include <stdio.h>

register int r9 asm("r9");
register int r10 asm("r10");
register int r11 asm("r11");
register int r12 asm("r12");
register int r13 asm("r13");

void print_logo() {
  printf("MMMMMWXXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNWMMMMM\n");
  printf("MMMMMO,,kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO;;OMMMMM\n");
  printf("MMMWO,  ,OWMMMMMMMMMMMMMMMMMMMMMMMMMMW0xkKWMMMMMMMMMMMMMMMMMMMMMMMMMMWK:  :KWMMM\n");
  printf("Xdc,.    .,cdXMMMMMMMMMMMMMMMMMMMMMWO:.  .lKWMMMMMMMMMMMMMMMMMMMMMXxl:.    .:lxX\n");
  printf("Ko;.      .;oKMMMMMMMMMMMMMMMMMMMMKl.      .dNMMMMMMMMMMMMMMMMMMMMKc'.      .'cK\n");
  printf("MMWNk'  'kXWMMMMMMMMMW0kXMMMMMMMWk'   ...    :0WMMMMMMMXxOWMMMMMMMMWNKd.  .dKNWM\n");
  printf("MMMMMk..kWMMMMMMMMMMM0'.oNMMMMMNo. .:x0000x;  'kWMMMMMNl '0MMMMMMMMMMMWx..xWMMMM\n");
  printf("MMMMMWKKWMMMMMMMMMMMX:  .kMMMMNl. ,ON0l::l0Xx. .kWMMMMk.  cNMMMMMMMMMMMNOONMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMMMO.   lNMMNo. '0Wx.    .kNx. .OMMMNc   'OMMMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMMMd.   ;XMWx. .dW0::dxxdc:0Nc  ,KMMX;   .xMMMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMMWo    ;XMK;  .kMx':olll:,xWo   lWMX;   .xMMMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMMWo    ;XMx.  .kMx.      .xWo   '0MX;   .xMMMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMMWo    ;XNc   .kMx. ;dd; .xWo   .dWX;   .xMMMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMMWo    :XK;   .OMx..xWMx..xWd    lNX;   .xMMMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMMWo    :XK,  .lXMx. ;dd; .xMK:   cNX;   .xMMMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMMWo    :XK, .dNMMx.   .  .xMMXl. cNX;   .xMMMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMMWo    :XK,'kNXNMx. cOOc .xMXXNd.cNX;   .xMMMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMMWo    :NXx0Nx:OMx..xMMx..xWk:ONOkNX;   .xMMMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMMWo    :NWWKl..kMx..xMMx..xMx..dNWMX;   .xMMMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMMWo   .xWNx'  .kMx..xMMx..xMx.  ;OWNd.  .xMMMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMMWd';dKXk;    .kMx..xMMx..xMx.   .:OX0o,,kMMMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMMMNKXOo'      .kMx..xMMx..xMx.     .,o0XXNMMMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMMNkc'.        .kMx..xWWx..xWx.        .'lONMMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMK:            ;0MO,.'cc'.;0M0;           .cXMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMWk:,,,,,,,,,,;dXX0XXo.  .dXKOKXx;,,,,,,,,,;:OMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMWWNK000XWNX0XWXc.lNX:..cXX: :XWX0XNWX0KKKNWWMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMMMk'...oNK:.lXX; cNWX00XWX; ;XXc.cXXc...'kMMMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMMMO'  .oWK, ;XX: cNNd;;dNN: cNX; ;XNl   'OMMMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMMMWKdoONMK, .xN0xKWx.  .xNKxKNx. ;XMNkodKWMMMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMK,  .lxkxl.    .cdxdc.  ;XMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMWNXNWMMMMMMMMMMXl......................lNMMMMMMMMMMWNXNWMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMWO:'.':OWMMMMMMMMMNXKK00000KKKKKK00000KKKNMMMMMMMMMWO:'.':OWMMMMMMMMMM\n");
  printf("MMMMMMMMMMO.     .OMMMMMMMMMMMMKl,,,lKMMMMKl;;;oXMMMMMMMMMMMMO.     .OMMMMMMMMMM\n");
  printf("MMMMMMNOdl'.'::.  'ld0NMMMMMMMMWklclkNMMMMNklclkWMMMMMMMMNOdl'  .::'.'ldONMMMMMM\n");
  printf("MMMMMKc.  .oXXk;     .cXMMMMMMMMWKOKWMMMMMMWKOKWMMMMMMMMXc.     ;kXXo.  .cXMMMMM\n");
  printf("MMMMNl.   'kO;.,c:;c:..lXNWMMMMMX: :XMMMMMMX: :XMMMMMWNKl..:c;:c,.;Ok.    lNMMMM\n");
  printf("MMM0;      ..  ;k00Ol.  .'cOWMMMK, ,KNOddONK, ,KMMMWOc'.  .o0KKk;  ..      ;0WMM\n");
  printf("MMX;             ..        .cdl:'   ''.  .,'   ':ldl.       ...             :XMM\n");
  printf("MMXdccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccxNMM\n");
  printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n\n");
}

void timeout(unsigned int seconds)
{
    printf("<<< You have %i seconds to auth.\n",seconds);
    alarm(seconds);
}

int three(int a, int b, int r) {
 return ((a + b + r) << 0x3);
}

int two(int b, int c) {
  return ((b / c)^0x2);
}

int one(int c, int d) {
  return ((c - d)+0x1);
}

void get_launch_auth() {
  int i, j, k, l;
  scanf("%x %x %x %x", &i, &j, &k, &l);
  r9 = i;
  r10 = j;
  r11 = k;
  r12 = l;
}

void blast_off() {
  char flag[0x48] = {0};
  FILE *fd = NULL;
  fd = fopen("flag.txt","r");
  fgets(flag, 0x48, fd);
  printf("<<< %s\n", flag);
  exit(1);
}

int main(int argc, char* argv[]) {
  print_logo();
  srand(time(NULL));   
  r13 = rand();
  printf("<<< Welcome to Shuttle Control Terminal.\n");
  timeout(30);      
  printf("----------------------------\n");
  printf("<<< Random nonce = %i\n",r13);

  printf("Enter launch auth code >>> ");
  get_launch_auth();

  if (three(r9,r10,r13) || two(r10,r11) || one(r11,r12)) {
    printf("<<< Authentication Failed.\n");
  } else {
      printf("<<< Authentication Succeeded.\n");
      blast_off();
  }
  return 0;
}
