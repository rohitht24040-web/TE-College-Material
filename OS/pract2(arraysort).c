#include<unistd.h>
#include<stdio.h>
#include<stdlib.h>
#include<sys/wait.h>

int main()
{
	pid_t pid;   //unsigned int   sys/types.h
	int status,arr[10];
	printf("\n Enter the 5 numbers for sorting\n");
	for(int i=0 ; i < 5 ; i++)
	{
		scanf("%d",&arr[i]);
	}
	pid=fork();
	if(pid==0)
	{
		//sleep(2);
		printf("\n Value of array in child process");
		printf("\nSortig in the asscending orfer\n");
		for(int i=0; i<5 ;i++)
                {
	                for(int j = 0 ; j < 5-i-1 ; j++)
	                    {
		                  if(arr[j] > arr[j+1])
		                 {
		    	              int temp = arr[j];
		 	              arr[j] = arr[j+1];
		 	              arr[j+1] = temp;	
		                  }
	                    }
                }
                for(int i=0 ; i<5 ; i++)
		{
			printf("%d\n", arr[i]);
		}					
		
		printf("\n This is child process with id %d",getpid());
		printf("\n Childs parent process with id %d",getppid());
		
	}
	else
	{
		sleep(2);
		system("ps");
		wait(&status);
		system("ps");
		
		printf("\n Value of array in parent process");
		printf("\nSortig in the descending order \n");
		for(int i=0; i<5 ;i++)
                {
	                for(int j = 0 ; j < 5-i-1 ; j++)
	                    {
		                  if(arr[j] < arr[j+1])
		                 {
		    	              int temp = arr[j];
		 	              arr[j] = arr[j+1];
		 	              arr[j+1] = temp;	
		                  }
	                    }
                }
                for(int i=0 ; i<5 ; i++)
		{
			printf("%d\n", arr[i]);
		}

		printf("\n This is parent process with id %d",getpid());
		printf("\n Parents child process with id %d",pid);
		
	}
	
}
