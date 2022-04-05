#include <stdio.h>
#include <time.h>
#include <stdlib.h>


__attribute__((constructor)) void ignore_me() {
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);
	setbuf(stderr, NULL);
}

void display_flag(char* fname) {
   FILE *fp;
   char buff[255];
   fp = fopen(fname, "r");
   fscanf(fp, "%s", buff);
   printf("<<< Congratulations: %s\n", buff );
}


int auth(int code1,int code2, int code3) {
  int res= ((code1+code2+code3) << (code1 % code2)) / (code3 * (3 ^ 2 << code1));
  return res;
}

int main()
{
    ignore_me();
    time_t T = time(NULL);
    struct tm tm = *localtime(&T);

    printf("<<< Space Travel require precision.\n");
    printf("<<< Current Time Is: %02d:%02d:%02d\n", tm.tm_hour, tm.tm_min, tm.tm_sec);


    printf("Enter authorization sequence >>> ");
    int code1, code2,code3;
    scanf("%x %x %x", &code1, &code2, &code3);

    if (auth(code1,code2,code3)!=10798448) {
       printf("<<< Authorization sequence not valid.");
       exit(0);
    }

    if ((tm.tm_min >= 17) && (tm.tm_min < 18)) {
       display_flag("flag.txt");
       return 0;
    }
    else {
      printf("<<< You failed. Try Another Time.\n");
    }
    return 0;
}
