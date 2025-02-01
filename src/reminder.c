//gcc -o program linked_list.c interact.c reminder.c
#include "reminder.h"

int start_day = 0;
int current_day = 1;
int last_day = 31;

char* initMonth(){
    time_t now = time(NULL);
    struct tm *local = localtime(&now);
    int int_month = local->tm_mon + 1;
    current_day = local->tm_mday;

    local->tm_mday = 1;
    mktime(local);
    start_day = local->tm_wday;

    char *month = malloc(10);
    switch (int_month)
    {
    case 1:
        strncpy(month, "January", 10);
        break;
    case 2:
        strncpy(month, "February", 10);
        last_day = 28;
        break;
    case 3:
        strncpy(month, "March", 10);
        break;
    case 4:
        strncpy(month, "April", 10);
        last_day = 30;
        break;
    case 5:
        strncpy(month, "May", 10);
        break;
    case 6:
        strncpy(month, "June", 10);
        last_day = 30;
        break;
    case 7:
        strncpy(month, "July", 10);
        break;
    case 8:
        strncpy(month, "August", 10);
        break;
    case 9:
        strncpy(month, "September", 10);
        last_day = 30;
        break;
    case 10:
        strncpy(month, "October", 10);
        break;
    case 11:
        strncpy(month, "November", 10);
        last_day = 30;
        break;
    case 12:
        strncpy(month, "December", 10);
        break;
    }
    month[strlen(month)] = '\0';
    return month;
}

void printCalendar(char* month){
    printf("\n%s:\n",month);
    printf("-------------\n");
    printf("\tSun  Mon  Tue  Wed  Thu  Fri  Sat\n");
    printf("\t");

    for (int i = 0; i < start_day; i++)
    {
        printf("     ");
    }

    for (int i = 0; i < last_day; i++)
    {
        if (day_messages[i] != NULL)
        {
            if(i + 1 < 10){
                printf("( %d)  ", i+1);
            }else{
                printf("(%d)  ", i+1);
            }
        }
        else
        {
            if(i + 1 < 10){
                printf(" %d   ", i+1);
            }else{
                printf("%d   ", i+1);
            }
        }

        if((i+start_day + 1) % 7 == 0){
            printf("\n\t");
        }
    }
    printf("\n");
    printList();
}

char * day_to_string(int month_day){
    char *message = malloc(4);
    

    time_t now = time(NULL);
    struct tm *local = localtime(&now);
    
    local->tm_mday = month_day-1;
    mktime(local);

    int work_day = local->tm_wday; //0 - 6
    switch(work_day){
        case 0:
            strncpy(message, "Mon", 4);
            break;
        case 1:
            strncpy(message, "Tue", 4);
            break;
        case 2:
            strncpy(message, "Wed", 4);
            break;
        case 3:
            strncpy(message, "Thu", 4);
            break;
        case 4:
            strncpy(message, "Fri", 4);
            break;
        case 5:
            strncpy(message, "Sat", 4);
            break;
        case 6:
            strncpy(message, "Sun", 4);
            break;
    }
    message[3] = '\0';
    return message;
}

void handle(int SIGNAL){
    writeToFile();
    freeAll();
    printf("\n");
    if (SIGNAL == SIGINT)
    {
        printf("SIGINT Caught and Handled.");
    }
    else if (SIGNAL == SIGTERM)
    {
        printf("SIGTERM Caught and Handled.");
    }
    else
    {
        printf("SIGSEGV Caught and Handled.");
    }
    exit(0);
}

int main(int argc, char *argv[]){
   int function = 0;
   switch(*(argv[1])){
	   case 'a':
		  function = 1;
		  break;
	case 'r':
		  function = 2;
		  break;
	case 'v':
		  function = 3;
		  break;
	case 't':
		  function = 4;
		  break;
   }
    signal(SIGINT, handle);
    signal(SIGTERM, handle);
    signal(SIGSEGV, handle);
    char *month = initMonth();
    readFromFile();
    int day = 1;
    switch (function)
    {
    case 1:
	day = atoi(argv[2]);
	char *msg = malloc(200);
	char *current = msg;
	for(int i = 0; i < argc-3;i++){	
		*current = ' ';
		current = current + 1;
		for(int j = 0; j < strlen(argv[i + 3]);j++){
			*current = *(argv[i+3] + j);
			current += 1;
		}
		*current = '\0';
	}
        addNode(day, msg);
	printCalendar(month);
        break;
    case 2:
        day = atoi(argv[2]);
	int index = atoi(argv[3]);
	removeReminder(day,index);
        printCalendar(month);
	break;
    case 3:
        printCalendar(month);
	break;
    case 4:
        printToday(current_day);
        break;
    default:
        printf("Message Error");
     }
     writeToFile();
     free(month);
     freeAll();
}
