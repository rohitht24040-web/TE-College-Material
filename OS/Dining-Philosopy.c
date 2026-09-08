#include<semaphore.h>
#include<pthread.h>
#include<unistd.h>
#include<stdio.h>

sem_t room ;
sem_t ch[5];

void *philosopher(void *arg)
{
	int i = *(int *)arg;
	
	sem_wait(&room);
	printf("\nPhilosopher %d entered in the room\n",i);
		sem_wait(&ch[i]); //Left Chopstick
		printf("Philosopher %d Picked the left ChopStick\n",i);
			sem_wait(&ch[(i+1)% 5]);
			printf("Philosopher %d Picked the right ChopStick\n",i);
				printf("Philosopher %d is eating\n",i);
			sem_post(&ch[(i+1)%5]);
			printf("Philosopher %d Release the left ChopStick\n",i);
		sem_post(&ch[i]);
		printf("Philosopher %d Release the left ChopStick\n",i);
	sem_post(&room);
	printf("Philosopher %d Leave the Room\n",i);	
}

int main()
{
	pthread_t p[5];
	int id[5];
	
	sem_init(&room,0,4);	//initialization of room
	
	for(int i = 0 ; i < 5 ; i++)	//initialization of ch[i]=1
	{
		sem_init(&ch[i],0,1);
	}
	
	for(int i = 0 ; i < 5 ;i++)
	{
		id[i] = i ;
		pthread_create(&p[i],NULL,philosopher,(void *)&id[i]);
	}
	
	for(int i=0 ; i<5 ; i++)
	{
		pthread_join(p[i],NULL);
	}
return 0;
}
