#include <wiringPi.h>
#include <stdio.h>

#define GPIO25 25

int main( void ) {
  printf("Hello world!\n");

  int i;
  // Initialize WiringPi
  if(wiringPiSetupGpio() == -1) return 1;

    // Set GPIO18 pin to output mode
    pinMode(GPIO25, OUTPUT);

    // Repeat LED blinking 10 times
    for(i=0; i<10; i++){
    digitalWrite(GPIO25, 0);
    delay(950);
    digitalWrite(GPIO25, 1);
    delay(50);
  }

  // Turn off LED
  digitalWrite(GPIO25, 0);
  
  return 0;
}

