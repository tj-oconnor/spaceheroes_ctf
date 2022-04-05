#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

void print_logo() {
  printf("MMMMMMMMMMMWX0xoc;'.....:KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMWXkl;...';cloddx0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMN0l,..,cdO0K0Okxdx0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMWOc'.'cxKKOdc,'.....:KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
  printf("MMMXo'.'l0XOo,...;coxkkOKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXO0NMMMMMMMMMMM\n");
  printf("MW0:..:OXOc...:x0XNNK0OOKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXx;..cOWMMMMMMMMM\n");
  printf("WO;..lKXd'..lONN0dc,'...:KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXx;.....'cONMMMMMMM\n");
  printf("K:..lXKl..;kNNOc...,codx0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXx;..........cONMMMMM\n");
  printf("o..:KXl..;0WXo..'lOXWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXx;..............cOWMMM\n");
  printf(",..xNk'.'kWXo..;kNWXkl:;:lkXWMMMMMMMMMMMMMMMMMMMMMMMMMMXx;.................'cONM\n");
  printf("..;0Nl..cXWk'.'kWW0:.......:0WMMMMMMMMMMMMMMMMMMMMMMMXx;......................cO\n");
  printf("..cKXc..dWWd..:KMNo.........oNMMMMMMN0O0KNWMMMMMMMWXk;.........................c\n");
  printf("dd0WW0dxKWWKxd0WMWx.........;OWMMWXx;...';xXWMMMMXx;.........................XX;\n");
  printf("MMMMMMMMMMMMMMMMMMNx;........'l0Kx;........;xXWMNd'........................;xNMM\n");
  printf("MMMMMMMMMMMMMMMMMMMWN0kkxl'.....'............;xXWXx;.....................;xXMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMMMMMMMMW0l'..................;xXWXx;.................;xXMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMMMMMMMMWKo'....................;XXXo...............;xXMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMMMMMMWKd,........................,,...;;.........;xXWMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMMMMMMO;..............................oXXk;.....;xXMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMMMMMWx'..............................;xXWXx:';xXMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMMMMMMNk;...............................;xXWNKNMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMMMMMMMMXk;...............................;xNMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMXx;...............................;xXMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMMMMMMMMMNNWXx:...............................;kNMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMMMMMMMXx::xXWXx;...............................lXMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMMMMMNk;....;kXW0:..............................cXMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMMMXx;........;l:...'.........................,dKWMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMXx;..............,x0x;.....................,oKWMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMXk:................;xXWXKx;................,oKWMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMXx;....................:kXWWXx:............,oKWMMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMWXx;........................cxKMMXx;........,oKWMMMMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMWXx;.........................;x0NMMMMXk:....,oKWMMMMMMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMWO:.........................;xXMMMMMMMMMNOddkKWMMMMMMMMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMW0c.......................;xXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMNOc...................;xXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMNOc...............;kXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMNOc...........:xXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMNOc.......;xXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMNOl...;xXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
  printf("MMMMMMMMMMMMMMMMMMMMNx;lKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
  printf("\nWelcome to our SATellite Terminal\n");
}

void print_flag() {
  char flag[64] = {0};
  FILE *fd = NULL;
  fd = fopen("flag.txt", "r"); 
  fgets(flag, 64, fd);
  printf("\n\n<<< Flag: %s\n", flag);
}

long long auth_func(long long a, long long b, int r) {
 return ((a<<b)^r);
}

void sat_access(int nonce) {
  long long secure_id;
  char resp[16];
  long long secure_seed;
  printf("\n<<< Here is a random token %i\n",nonce);
  printf("What is your response >>> ");
  scanf("%s", resp);
  if (auth_func(secure_id,secure_seed,nonce)!=31337) {
     exit(0);
  }
}

int main(int argc, char* argv[]) {

  print_logo();
  srand(time(NULL));   
  int nonce = rand();
  sat_access(nonce);

  printf("Thank You.\n");
  return 0;
}
