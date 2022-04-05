#include <stdio.h>
#include <time.h>
#include <unistd.h>
#include <stdlib.h>
#include <termios.h>
#include <poll.h>
#include <fcntl.h>
#include <openssl/sha.h>

#define SIZE_X 33
#define SIZE_Y 20
#define MAX_WORM 661

#define clear_screen() printf("\033[H\033[J")
#define reset_cursor() printf("\x1b[1;1H")
#define ngetc(c) read(0, c, 1)

// SHA-256 variables
SHA256_CTX buf; // context
unsigned char buf2[SHA256_DIGEST_LENGTH]; // hash
// For size == 600
//unsigned char magic_bytes[32] = {0xe9,0xb7,0xfe,0xe0,0xa5,0x09,0xd4,0xa0,0x3b,0x85,0x4b,0xb4,0x73,0x3d,0xd8,0x4d,0xb4,0x91,0x7f,0x9d,0xdf,0x55,0x2c,0x72,0xdf,0xda,0xb6,0x0f,0x71,0xf9,0xd9,0x1c};
// For size == 661
unsigned char magic_bytes[32] = {0xb2,0xea,0xe5,0xbf,0xbb,0x8c,0xc6,0x01,0x38,0x72,0x0b,0x2f,0x0f,0x54,0x9c,0x6e,0x40,0x24,0xea,0x84,0xc7,0xe1,0x7d,0x34,0x58,0xbd,0x2e,0xe2,0xb4,0x12,0x48,0xfe};

// Global variables to track user input (horizontal & vertical)
int h = 0;
int v = 0;

// Game map
int arrakis[SIZE_X][SIZE_Y];

// Ticks tracker (used for collision detection)
int tracker = 1;


// Defining our worm struct
typedef struct Shai_Hulud Shai_Hulud;

struct Shai_Hulud {
  int size;
  int direction;
  int x, y;
} worm;

// Clear the field of any values
void clear()
{
  for (int i = 0; i < SIZE_X; i++)
    for (int j = 0; j < SIZE_Y; j++)
      arrakis[i][j] = -1;
}

// generate new food
void vibration()
{
  int tx = rand() % SIZE_X;
  int ty = rand() % SIZE_Y;

  // place the food
  arrakis[tx][ty] = -2;
}

// Do changes for this frame
int frame()
{
  Shai_Hulud* sh = &worm;

  // Based on direction, change the (x,y) value of our worm
  switch(sh->direction)
  {
  case 0:
    sh->x++;
    break;
  case 1:
    sh->y++;
    break;
  case 2:
    sh->x--;
    break;
  case 3:
    sh->y--;
    break;
  }

  // Keep track of how many rounds there have been
  tracker++;

  // Wraparound 
  if (sh->x < 0)
    sh->x = SIZE_X - 1;
  if (sh->x >= SIZE_X)
    sh->x = 0;
  if (sh->y < 0)
    sh->y = SIZE_Y - 1;
  if (sh->y >= SIZE_Y)
    sh->y = 0;

  // Fail conditions - Checks for collision
  if (arrakis[sh->x][sh->y] > 0 && arrakis[sh->x][sh->y] >= tracker - sh->size)
    return 0;

  // If the worm lands on food, update our Proof of Work, place new food, and increase the worm size
  if (arrakis[sh->x][sh->y] == -2)
  {
    int64_t position = (sh->x << 4) + sh->y;
    SHA256_Update(&buf, &position, 8);
    SHA256_Final(buf2, &buf);
    vibration();
    worm.size++;
  }

  arrakis[sh->x][sh->y] = tracker;

  return 1;
}

// Output the screen
void draw()
{
  reset_cursor();
  for (int i = -1; i <= SIZE_Y; i++)
  {
    for (int j = -1; j <= SIZE_X; j++)
    {
      if (i < 0 || i >= SIZE_Y || j < 0 || j >= SIZE_X)
        printf("#");
      else if (arrakis[j][i] == -2)
        printf("*");
      else if (arrakis[j][i] <= tracker - worm.size)
        printf(" ");
      else
        printf("@");
    }
    if (i == 0) {
      printf("  Inspired by USCC Cyber Quest");
    }
    if (i == 1) {
      printf("  Use wasd to move your worm, press q to terminate");
    }
    else if (i == 2) {
      printf("  Size: %d", worm.size);
    }
    else if (i == 3) {
      printf("  POW: ");
      for(int i = 0; i < SHA256_DIGEST_LENGTH; i++)
      {
        printf("%02x", buf2[i]);
      }
    }
    
    printf("\n");
  }
  
}

// Movement
void wriggle()
{
  int direction = worm.direction;

  // Based on inputs, change directions
  if (h == 1 && direction != 2)
    direction = 0;
  else if (h == -1 && direction != 0)
    direction = 2;
  else if (v == 1 && direction != 1)
    direction = 3;
  else if (v == -1 && direction != 3)
    direction = 1;

  // Store back into our worm
  worm.direction = direction;
}

void input_thread()
{
  fcntl(0, F_SETFL, O_NONBLOCK);
  char c = 0;
  struct termios oldt, newt;
  tcgetattr(STDIN_FILENO, &oldt);
  newt = oldt;
  newt.c_iflag &= ~(ICANON | ECHO);
  tcsetattr(STDIN_FILENO, TCSANOW, &newt);
  ngetc (&c);
  system("/bin/stty raw");
  tcsetattr(STDIN_FILENO, TCSANOW, &oldt);

  switch (c)
    {
    // Up
    case 'w':
    case 'W':
      h = 0;
      v = 1;
      break;
    // Down
    case 's':
    case 'S':
      h = 0;
      v = -1;
      break;
    // Right
    case 'd':
    case 'D':
      h = 1;
      v = 0;
      break;
    // Left
    case 'a':
    case 'A':
      h = -1;
      v = 0;
      break;
    // Quit
    case 'q':
    case 'Q':
      clear();
      printf("DEBUG INFO (don't forget to delete me!)\nX:%d Y:%d Size:%d Dir:%d\n", worm.x, worm.y, worm.size, worm.direction);
      exit(0);
    }
  printf("%c", c);
  c = 0;
}

void wormsign() {
  worm.x = SIZE_X/2;
  worm.y = SIZE_Y/2;
  worm.size = 1;
  worm.direction = 0;
  return;
}

void print_flag() {
  printf("shctf{");
  for(int i = 0; i < SHA256_DIGEST_LENGTH; i++) {
    buf2[i] = buf2[i] ^ magic_bytes[i];
  }
  printf("%.32s}\n", buf2);
  return;
}


// Main
int main()
{
  srand(9300);
  SHA256_Init(&buf);
  clear();
  
  wormsign();
  vibration();

  // Main loop
  while (1)
  {
    if(worm.size == MAX_WORM) {
      print_flag();
      break;
    }
    input_thread();
    wriggle();
    if (!frame())
      break;
    clear_screen();
    draw();
    usleep(100*1000);
  }
  return 0;
}
