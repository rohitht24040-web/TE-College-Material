#include<semaphore.h>
#include<pthread.h>
#include<unistd.h>
#include<stdio.h>

int rdcount = 0;

sem_t r,w;

void *write( void *arg)
{
	int i = *(int *)arg;
	sem_wait(&w);
		printf("Writer %d is Writing",i);
	sem_post(&w);
}

void *read(void *arg)
{
	int i = *(int *)arg;
	
	sem_wait(&r);
	rdcount++;
	
	if(rdcount == 1)
	{
		sem_wait(&w);
	}
	
	sem_post(&r);
		printf("Reader %d is reading",i);
	sem_wait(&r);
		printf("Reader %d has done reading",i);
	rdcount--;
	
	if(rdcount == 0)
	{
		sem_post(&w);
	}
	sem_post(&r);
}
int main()
{
	pthread_thread p[8],writ;
	int id[5];
	
	sem_init(&r,0,5);
	sem_init(&w,0,3);
	
	for(int i = 0 ; i < 5  ; i++)
	{
		id[i]=i;
		pthread_create(&p[i] , NULL ,read , (void *)&id[i]);
	}
	for(int i = 0 ; i < 3  ; i++)
	{
		id[i]=i;
		pthread_create(&p[i] , NULL ,write , (void *)&id[i]);
	}
	
	
	
	for(int i = 0 ; i < 5  ; i++)
	{
		pthread_join(&p[i] , NULL);
	}
	
	
return 0;
}
























