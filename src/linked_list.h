#ifndef LIST
#define LIST

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "reminder.h"



typedef struct Node{
     int day;
     char *message;
     struct Node *next;
} Node;

extern Node* day_messages[];

void addNode(int day, char *message);

void freeAll();

void printList();

void removeReminder(int day, int index);

void printToday(int day);

#endif
