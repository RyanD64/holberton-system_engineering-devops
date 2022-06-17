#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - make a function repeat indefinitely
 * Return: nothing
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - create 5 zombie functions
 * Return: 0
 */

int main(void)
{
	int a = 0;
	pid_t ZOMBIE;

	for (a = 0; a < 5; a++)
	{
		ZOMBIE = fork();
		if (ZOMBIE == 0)
			exit(0);
		printf("Zombie process created, PID: %d\n", ZOMBIE);
		sleep(1);
	}
	infinite_while();
	return (0);
}
