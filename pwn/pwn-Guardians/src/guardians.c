// format string

#include <stdio.h>
#include <stdlib.h>

void buffer_init() {
	setbuf(stdout, NULL);
	setbuf(stdin, NULL);
	setbuf(stderr, NULL);
}

int main() {
	char name[32];
	char flag[32];
	char *flag_ptr = flag;

	buffer_init();
	FILE *file = fopen("./flag.txt", "r");
	if (file == NULL) {
		printf("Error, please message admins with 'infinity_error'.\n");
		exit(0);
	}

	fgets(flag,sizeof(flag),file);

	while(1) {
		printf("Does Quill manage to win the dance battle?\n");
		fgets(name,sizeof(name),stdin);
		printf("\nOh no, Ronano has seen through the distraction!\n");
		printf(name);
		printf("\n");
	}
	return 0;
}