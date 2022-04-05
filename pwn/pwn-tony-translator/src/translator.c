#include <ctype.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include <sys/types.h>

int counter = 0;

struct fp {
    int (*fp)();
};

int slightly_more_useless_func(){
    char tony;
}

int useless_func(){
    printf("Tony has successfuly translated your gibberish!\n");
}

int main(int argc, char **argv){

    // 70NY 574rck'5 C41cu1470r
    counter += 1;
    if (counter == 2) {
        printf("\n84ck 50 500n?\n");
        FILE *fin = fopen("flag.txt", "r");
        char *flag = NULL;
        int len, read;
        read = getline(&flag, &len, fin);
        printf("%s\n", &flag[0]);
        return 0;
    } else {
        printf("W31c0m3 70 70ny'5 7r4n51470r.\n");
    }

    struct fp *f;
    char *translate;
    translate = (char *)malloc(sizeof(char)*56);
    char *tony = (char *)malloc(sizeof(char)*8);
    strcpy(tony, "1337");
    f = malloc(sizeof(struct fp));
    f->fp = useless_func;
    
    char user_input[60];
    scanf("%[^\n]s", &user_input[0]);

    if (strlen(user_input) > 60) {
        printf("Tony is busy translating, don't overwhelm him.\n");
        return 1;
    }
    
    int len = strlen(user_input);
    strcpy(translate, user_input);
    printf("Translating the string %s to 70NY 5P34K...\n", &translate[0]);
    for (int i = 0; i < len; i++) {
        char cur = tolower(translate[i]);
        switch (cur) {
            case 'a':
                for (int j = strlen(translate); j >= i; j--) {
                    translate[j+1] = translate[j];
                }
                translate[i] = '/';
                translate[i+1] = '\\';
                break;
            case 'e':
                translate[i] = '3';
                break;
            case 'i':
                translate[i] = '1';
                break;
            case 'o':
                translate[i] = '0';
                break;
            case 'l':
                translate[i] = '1';
                break;
            case 't':
                translate[i] = '7';
                break;
            break;
        }  
        if (cur != tolower(translate[i])) {   
            printf("Swapped %c -> %c\n", cur, translate[i]);
        }
    }
    printf(tony);
    printf(" Translation: %s\n", &translate[0]);
    if (f->fp) {
        f->fp();
    }
}