#ifndef REMINDER
#define REMINDER


#include <stdio.h>
#include <signal.h>
#include <time.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include "linked_list.h"
#include "interact.h"

#define FILENAME "./storage.txt"

extern int last_day;

void printCalendar(char* month);

void insertToCalendar();

char *day_to_string(int month_day);

#endif
