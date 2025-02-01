#include "interact.h"

void flushBusher(){
     fflush(NULL);
}

void readFromFile(){
    FILE *reader = fopen(FILENAME, "r");
     if(reader == NULL){
          return;
     }

    char input[200];

    while (fgets(input, sizeof(input), reader) != NULL) {
          int space_index = 1;
          if (input[2] == '\0')
          {
              space_index = 2;
          }

          char *message = input + space_index+1;
          message[strlen(message) - 1] = '\0';

          addNode(atoi(input), message);
    }
     flushBusher();
     fclose(reader);
}

void writeToFile(){
     FILE *appender = fopen(FILENAME, "w");
     if(appender == NULL){
          return;
     }

     for (int i = 0; i < last_day; i++)
     {
          Node *current = day_messages[i];
          while(current != NULL){
               fprintf(appender, "%d %s\n",(i+1),current->message);
               current = current->next;
          }
     }
     flushBusher();
     fclose(appender);
}


