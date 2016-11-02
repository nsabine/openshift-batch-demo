// file ex8.c
#include "unif01.h"
#include "ulcg.h"
#include "ulec.h"
#include "my16807.h"
#include <stdio.h>

int main (void) 
{
   unif01_Gen *gen;
   gen = CreateMy16807 (12345);
   bbattery_SmallCrush (gen);
   DeleteMy16807 (gen);
   return 0;
}

