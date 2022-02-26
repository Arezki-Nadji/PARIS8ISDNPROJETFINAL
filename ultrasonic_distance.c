// gcc -Wall -pthread -o ultrasonic_distance ultrasonic_distance.c -lpigpio

#include <stdio.h>
#include <pigpio.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define TRIGGER 23
#define ECHO  24

int main(int argc, char *argv[]) {
    double start, stop, measure;

    if (gpioInitialise() < 0) {
        fprintf(stderr, "pigpio initialisation failed\n");
        return 1;
    }

    /* Set GPIO modes */
    gpioSetMode(TRIGGER , PI_OUTPUT);  // trigger
    gpioSetMode(ECHO , PI_INPUT);  // echo
    fprintf(stdout, "Set GPIO modes\n");
int compteur = 0;
while(compteur < 10){
    compteur ++;
    gpioWrite(TRIGGER, 1);
    gpioSleep(PI_TIME_RELATIVE, 0, 10); // sleep for 0.00001 seconds
    gpioWrite(TRIGGER, 0);

    while (gpioRead(ECHO) == 0)
	start = time_time();
    while (gpioRead(ECHO) == 1)
        stop = time_time();

    measure = (stop-start) *17150.0; // vitesse du son 340 m/s
    
    fprintf(stdout, "Measure: %lf cm\n", measure); 
    if(measure <12.0){
        system("python picture.py");
     }
}   
    /* Stop DMA, release resources */
    gpioTerminate();
    return 0;
}
