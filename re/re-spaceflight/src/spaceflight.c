/*
 * spaceflight challenge 
 * Author: Sean LaPlante
 */
#include <stdio.h>
#include <stdbool.h>
#include <time.h>
#include <signal.h>
#include <string.h>
#include <stdlib.h>

#define MAX_INPUT 80

static char user_input[MAX_INPUT + 1] = {'\0'};
static const char * launch_password = "b3y0nd!infinity";
static bool timer_cancelled = false;
static int jettisen_sequence[] = { 2, 3, 0, 1 };


static void print_flag() {
    /* you win. Print the flag. */
    char flag[1025] = {'\0'};
    FILE * fh = NULL;
    fh = fopen("flag", "r");
    if (!fh) {
        printf("Real talk: No flag found. This might actually be a bug, tell someone.\n");
        exit(1);
    }
    fread(flag, 1024, 1, fh);
    printf("Flag:\n\n%s\n\n", flag);
}


static void end_travel(){
    /* You lose! Ship explodes. */
    printf("Your space travels have ended without reaching your destination.");
    exit(1);
}


static void read_input() {
    /* Read the user's input */
    char cur_char = '\0';
    int count = 0;
    printf("$ ");
    while((cur_char = getchar()) != '\n' && count < MAX_INPUT) {
        user_input[count] = cur_char;
        count += 1;
    }

    if (count == MAX_INPUT) {
        printf("TOO MUCH INPUT!\n");
        end_travel();
    }
}


static bool check_debugger() {
    /* Check for debugger */
    // NOTE: Could remove this to make easier.
    FILE * fh = NULL;
    int pid = 0;
    char * start = NULL;
    char * end = NULL;
    const char * tracer = "TracerPid:";
    char line[1024] = {'\0'};
    fh = fopen("/proc/self/status", "r");

    if (!fh) {
        printf("WHAT DID YOU DO TO MYSELF?!?!\n");
        end_travel();
    }

    while(fgets(line, 1024, fh)) {
        if ((start = strstr(line, tracer))) {
            end = line + strlen(line);
            for (char *c = start + strlen(tracer); c < end; c++) {
                if ((*c) == ' ') {
                    continue;
                }
                pid = atoi(c);
                if (pid == 0) {
                    return false;
                }
                break;
            }
            return true;
        }
    }

    return false;
}


static void cntrl_c_handler(int signum) {
    /* 'stop' the timer */
    printf("Explode timer suspended. Ship will now take forever seconds to explode.\n");
    timer_cancelled = true;
}


static bool check_jettison(const char * input) {
    int input_nums[4] = {0};
    int new_order[4] = {0};
    int check = sscanf(input, "%d %d %d %d", &input_nums[0], &input_nums[1], &input_nums[2], &input_nums[3]);
    if (check != 4) {
        return false;
    }

    for (int i = 0; i < 4; i++) {
        if (input_nums[i] > 3 || input_nums[i] < 0) {
            return false;
        }
        new_order[i] = jettisen_sequence[input_nums[i]];
    }

    for (int i = 0; i < 3; i++) {
        if (new_order[i] > new_order[i + 1]) {
            return false;
        }
    }

    return true;
}


/*
 * 4 phases must be passed to get the flag
 */

static void phase_launch() {
    /*
     * Input must match the launch password: b3y0nd!infinity
     */
    read_input();

    // NOTE: Could change this to a stack overflow password bypass to make it more challenging
    int check_len = strlen(launch_password);
    if (strnlen(user_input, MAX_INPUT) != check_len) {
        printf("WRONG LENGTH!\n");
        end_travel();
    }
    if (strcmp(user_input, launch_password) != 0) {
        printf("WRONG WRONG!\n");
        end_travel();
    }
}


static void phase_jettison() {
    /*
     * fake 0.1 second timer that has to be 'cancelled' with cntrl+z,
     * then enter valid jettison sequence (order a global array smallest to largest)
     */

    // NOTE: Could remove the check_jettison and just make them figure out cntrl+z to make it easier.
    signal(SIGINT, cntrl_c_handler);
    read_input();

    if (!timer_cancelled) {
        printf("OUT OF TIME!\n");
        end_travel();
    }

    if (!check_jettison(user_input)) {
        printf("OUT OF ORDER!\n");
        end_travel();
    }
}


static void phase_destination() {
    /*
     * Integer overflow, x, y, and z have to be positive and add up to -1
     */
    read_input();
    int x, y, z = 0;

    int check = sscanf(user_input, "%d %d %d", &x, &y, &z);
    if (check != 3) {
        printf("NOT ENOUGH NUMBERS!\n");
        end_travel();
    }

    // Check that we're inside the bounds of positive space
    if (x < 0 || y < 0 || z < 0) {
        printf("NEGATIVE!\n");
        end_travel();
    }

    // They need to learn to warp to negative space (idk....it's an overflow)
    int destination = x + y + z;
    if (destination != -1) {
        printf("NOT NEGATIVE ENOUGH!\n");
        end_travel();
    }
}


static void phase_hyperjump() {
    /*
     * Using gets() here instead. Make sure input is "jump" then overflow
     * one byte into the "check" variable which should be 42 ('*')
     */
    char check = 0;
    char input[4] = {'\0'};

    printf("$ ");
    gets(input);

    // The Answer to the Ultimate Question of Life, the Universe and Everything.
    if (check == 42 && strncmp(input, "jump", 4) == 0) {
        print_flag();
        return;
    }
    end_travel();
}


int main() {
    printf(" /\\/\\/\\                            /  \\\n"
           "| \\  / |                         /      \\\n"
           "|  \\/  |                       /          \\\n"
           "|  /\\  |----------------------|     /\\     |\n"
           "| /  \\ |                      |    /  \\    |\n"
           "|/    \\|                      |   /    \\   |\n"
           "|\\    /|                      |  | (  ) |  |\n"
           "| \\  / |                      |  | (  ) |  |\n"
           "|  \\/  |                 /\\   |  |      |  |   /\\\n"
           "|  /\\  |                /  \\  |  |      |  |  /  \\\n"
           "| /  \\ |               |----| |  |      |  | |----|\n"
           "|/    \\|---------------|    | | /|   .  |\\ | |    |\n"
           "|\\    /|               |    | /  |   .  |  \\ |    |\n"
           "| \\  / |               |    /    |   .  |    \\    |\n"
           "|  \\/  |               |  /      |   .  |      \\  |\n"
           "|  /\\  |---------------|/        |   .  |        \\|\n"
           "| /  \\ |              /          |   .  |          \\\n"
           "|/    \\|              (          |      |           )\n"
           "|/\\/\\/\\|               |    | |--|      |--| |    |\n"
           "------------------------/  \\-----/  \\/  \\-----/  \\--------\n"
           "                        \\\\//     \\\\//\\\\//     \\\\//\n"
           "                        \\/       \\/  \\/       \\/\n"
    );

    if (check_debugger()) {
        end_travel();
    }

    // Phase 1: "b3y0nd!infinity"
    printf("Enter the launch password to blast off:\n");
    phase_launch();
    printf("BLAST OFF!! You're headed to space!\n\n");

    // Phase 2: "2 3 0 1"
    printf("Great job with the blast off! Now let's jettison those empty thrusters. You have 0.1 seconds. Good luck!\n");
    phase_jettison();
    printf("Thrusters safely ejected!\n\n");

    // Phase 3: "2147483647 2147483647 1" (multiple valid answers)
    printf("Next we must set our destination. Here you will learn how to fold space.\n");
    phase_destination();
    printf("Destination locked!\n\n");

    // Phase 4: "jump*"
    printf("The hyperdrive is ready. Enter the jump sequence\n");
    phase_hyperjump();
    printf("You did it! Happy space travels!\n");

    return 0;
}
