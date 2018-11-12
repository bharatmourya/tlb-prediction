#define _GNU_SOURCE

#include<stdio.h>
#include<string.h>
#include<pthread.h>
#include<stdlib.h>
#include<unistd.h>
#include <sys/syscall.h>
#include <sched.h>

#define AFFINITY 1
#define THREADS 8

pthread_t tid[THREADS];
unsigned long long value_array[THREADS], result=0;
int flag=0;


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


void* doSomeThing(void *arg)
{
    unsigned long i = 0, j=0;
    int index = (int*) arg;
    pid_t tid = syscall(SYS_gettid);

    while(value_array[index]<0xFFFFFFFFFFFFFFFF)
    {
       //for(i=0; i<(0xFFFFFFFF);i++)
       //for(j=0; j<(0xFFFFFFFF);j++);

       value_array[index]++;

       if(flag)
         pthread_cancel(pthread_self());
    }
    return NULL;
}


void create_thread(int cpu)
{
    int i = 0;
    int err;  
    while(i < THREADS)
    {
        value_array[i]=0;
        err = pthread_create(&(tid[i]), NULL, &doSomeThing, (void *)i);
        i++;
    }
    
    if(AFFINITY)
      set_affinity(cpu);
}

unsigned long long print_result()
{
    int i=0;
    unsigned long long result =0;
    while(i<THREADS)
    {
       result+= value_array[i++];
    }
    
    return result;
}


int main(int argc, char* argv[])
{
    create_thread(atoi(argv[1]));
    sleep(180);
    flag=1;

    printf("\nValue : %lld\n", print_result());
    return 0;
}
