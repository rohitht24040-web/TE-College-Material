#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<string.h>
#include<fcntl.h>

int main()
{
	int decp1[2] ,decp2[2] , fd;


	char filename[10]={'\0'};
	char buffer[200]={'\0'};

	pid_t  pid;

	pipe(decp1);
	pipe(decp2);

	pid = fork();

	if(pid>0) //Parent Process because after fork  it returns child ID
	{
	close(decp1[0]);
	close(decp2[1]);

	write(decp1[1] , "abcd.txt",8);
	close(decp1[1]);


	read(decp2[0],buffer,sizeof(buffer));
	
	printf("%s",buffer);

	close(decp2[0]);
	}
	else
	{

	close(decp1[1]);
	close(decp2[0]);

	read(decp1[0],filename,sizeof(filename));
	close(decp1[0]);


	fd = open(filename,O_RDONLY);
	read(fd,buffer,sizeof(buffer));
	close(fd);

	write(decp2[1],buffer,sizeof(buffer));
	close(decp2[1]);
	}

return 0;
}
