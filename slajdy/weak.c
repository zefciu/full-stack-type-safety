#include <stdio.h>
short int fun(int* x) {
	short int y = *(short int*)x;
	return y + 1;
}

int main(int argc, char** argv) {
	int a = -10;
	int b = 777777;
	printf("%d\n", fun(&b)); // prints: -8654
	printf("%u\n", a);       // prints: 4294967286
}
