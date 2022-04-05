#include <stdio.h>
#include <time.h>
#include <unistd.h>
#include <stdlib.h>
#include <termios.h>
#include <poll.h>
#include <fcntl.h>
#include <openssl/sha.h>

#define MAX_SIZE 661
#define START_SIZE 1
#define SIZE_X 33
#define SIZE_Y 20

unsigned char hash[SHA256_DIGEST_LENGTH];
SHA256_CTX sha256;
unsigned char magic_bytes[32] = {0xb2,0xea,0xe5,0xbf,0xbb,0x8c,0xc6,0x01,0x38,0x72,0x0b,0x2f,0x0f,0x54,0x9c,0x6e,0x40,0x24,0xea,0x84,0xc7,0xe1,0x7d,0x34,0x58,0xbd,0x2e,0xe2,0xb4,0x12,0x48,0xfe};

// Xor each byte of hash with our magic bytes, then print out flag
void print_flag() {
  for(int i = 0; i < SHA256_DIGEST_LENGTH; i++) {
    hash[i] = hash[i] ^ magic_bytes[i];
  }
  printf("FLAG\n----\n");
  printf("shctf{%.32s}\n", hash);
  return;
}

int main()
{
	int64_t position;
	int x, y, i;
	// Initialize random seed and our hash
	srand(9300);
	SHA256_Init(&sha256);
	// Iterate over all pellets
	for(i = START_SIZE; i < MAX_SIZE; i++) {
		x = rand() % SIZE_X;
  		y = rand() % SIZE_Y;
		position = (x << 4) + y;
    	SHA256_Update(&sha256, &position, 8);
    	SHA256_Final(hash, &sha256);
    	/* UNCOMMENT IF YOU WANT TO SEE ALL HASHES
    	printf("Size %d: ", i+1);
    	for(int j = 0; j < SHA256_DIGEST_LENGTH; j++)
		{
    	printf("%02x", hash[j]);
		}
		printf("\n");
		*/
	}
	printf("FINAL HASH\n----------\n");
	printf("Size %d: ", i);
	for(int j = 0; j < SHA256_DIGEST_LENGTH; j++)
	{
  	printf("%02x", hash[j]);
	}
	printf("\n\n");
	print_flag();
	return 0;
}
