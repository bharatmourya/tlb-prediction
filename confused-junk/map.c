#define _GNU_SOURCE

#include<stdio.h>
#include<string.h>
#include <stdlib.h>
#include<pthread.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/syscall.h>
#include<sched.h>
#include<time.h>
#include <semaphore.h> 
#include <sys/mman.h>

#define AFFINITY 1
#define THREADS 8
#define MAPPER 4
#define UNMAPPER 4

struct map{
    char* addr;
    sem_t mutex;
};

struct map map_data[MAPPER];

pthread_t tid[THREADS];
int flag=0;

void init_mapper_mutex()
{
  int i=0;
  while(i<MAPPER)
  {
    sem_init(&(map_data[i].mutex), 0, 1);
    i++;
  }

}


void set_affinity(int cpu)
{
  cpu_set_t my_set;
  CPU_ZERO(&my_set);
  CPU_SET(cpu, &my_set);

  int i=0;
  while(i<THREADS)
  {	  
     pthread_setaffinity_np(tid[i], sizeof(cpu_set_t), &my_set);
     i++;
  }   
}


void* domap(void *arg)
{
    int index=(int*)arg;
    int pagesize = getpagesize();

    FILE *fp;
    fp=fopen("sample.txt","r");

    while(1)
    {
       sem_wait(&map_data[index].mutex);
       if(!map_data[index].addr)
       {
         map_data[index].addr = mmap(NULL, pagesize, PROT_READ | PROT_WRITE, MAP_ANON | MAP_PRIVATE, fp, 0);
         strcpy(map_data[index].addr, "Hello");
       }
       sem_post(&map_data[index].mutex);      
      
       if(flag)
         pthread_cancel(pthread_self());
    }
    return NULL;
}


void* dounmap(void *arg)
{
    int index;
    int pagesize = getpagesize();

    while(1)
    {
       srand(time(0));
       index=rand()%MAPPER;

       sem_wait(&map_data[index].mutex);
       if(map_data[index].addr)
       {
         munmap(map_data[index].addr, pagesize);
         map_data[index].addr = NULL;
       }
       sem_post(&map_data[index].mutex);      
      
       if(flag)
         pthread_cancel(pthread_self());
    }
    return NULL;
}


void create_thread(int cpu)
{
    int i = 0;
    int err;  
    while(i < MAPPER)
    {
        err = pthread_create(&(tid[i]), NULL, &domap, (void *)i);
        i++;
    }



    i=0;
    while(i < UNMAPPER)
    {
        err = pthread_create(&(tid[i+MAPPER]), NULL, &dounmap, (void *)i+MAPPER);
        i++;
    }
    
    if(AFFINITY)
      set_affinity(cpu);
}

unsigned long long print_result()
{
  return 0;
}


int main(int argc, char* argv[])
{
    init_mapper_mutex();
    create_thread(atoi(argv[1]));
    sleep(100);
    flag=1;

    printf("\nValue : %lld\n", print_result());
    return 0;
}
