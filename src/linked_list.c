#include "linked_list.h"

Node* day_messages[] = {
     NULL,
     NULL,
     NULL,
     NULL,
     NULL,
     NULL,
     NULL,
     NULL,
     NULL,
     NULL,
     NULL,
     NULL,
     NULL,
     NULL,
     NULL,
     NULL,
     NULL,
     NULL,
     NULL,
     NULL,
     NULL,
     NULL,
     NULL,
     NULL,
     NULL,
     NULL,
     NULL,
     NULL,
     NULL,
     NULL,
     NULL
};

void addNode(int day, char* message)
{
     Node *newNode = malloc(sizeof(Node));
     newNode->day = day;
     newNode->message = malloc(strlen(message) + 1);
	newNode->next = NULL;
     strncpy(newNode->message, message, strlen(message) + 1);
     
     Node *p = day_messages[day -1];
     if(p == NULL){
	     day_messages[day-1] = newNode;
     }else{
	while(p->next != NULL){
		p=p->next;
	}
	p->next = newNode;
     }     
}

void freeAll(){
     for (int i = 0; i < last_day; i++)
     {
          Node *current = day_messages[i];
          while(current != NULL){
               free(current->message);
               free(current);
               current = current->next;
          }
     }
}

void printList(){
     for (int i = 0; i < last_day; i++)
     {
          Node *current = day_messages[i];
          if(current != NULL){
               printf("---%s (%d)---\n", day_to_string(i+1), i+1);
               int j = 1;
               while (current != NULL)
               {
                    printf("(%d): %s", j, current->message);
                    printf("\n");
                    current = current->next;
                    j++;
               }
          }
     }
}

void removeReminder(int day, int index){
     day = day -1;
	Node *current = day_messages[day];
     Node *prev = NULL;
     for(int i = 1; i < index && current != NULL; i++){
	prev = current;
	current = current->next;
     }

     if(current == NULL){
          printf("Message Not Found\n");
          return;
     }
     if(prev == NULL){
          day_messages[day] = current->next;
     }
     else
     {
          prev->next = current->next;
     }
     free(current->message);
     free(current);
}

void printToday(int day){
     Node *current = day_messages[day-1];
     if(current != NULL){
          printf("Today---%s (%d)---\n", day_to_string(day), day);
          int j = 1;
          while (current != NULL)
          {
               printf("(%d): %s", j, current->message);
               printf("\n");
               current = current->next;
               j++;
          }
     }else{
          printf("---%s (%d)---\nNo Reminders\n\n", day_to_string(day), day);
     }
}
