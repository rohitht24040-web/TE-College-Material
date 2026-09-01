#include<unistd.h>
#include<stdio.h>
#include<stdlib.h>
#include<sys/wait.h>

int main()
{
	pid_t pid;   //unsigned int   sys/types.h
	int status,a[10];
	int i=15;
	pid=fork();
	if(pid==0)
	{
		//sleep(2);
		i=i+10;
		printf("\n Value of i in child process %d",i);
		printf("\n This is child process with id %d",getpid());
		printf("\n Childs parent process with id %d",getppid());
		
	}
	else
	{
		sleep(2);
		system("ps");
		wait(&status);
		system("ps");
		i=i*10;
		printf("\n Value of i in parent process %d",i);
		printf("\n This is parent process with id %d",getpid());
		printf("\n Parents child process with id %d",pid);
		
	}
	
}
