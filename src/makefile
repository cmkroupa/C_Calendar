gcal: linked_list.o interact.o reminder.o
	gcc -o gcal linked_list.o interact.o reminder.o

linked_list.o: linked_list.c linked_list.h reminder.h
	gcc -c linked_list.c

interact.o: interact.c interact.h linked_list.h reminder.h
	gcc -c interact.c

reminder.o: reminder.c reminder.h linked_list.h interact.h
	gcc -c reminder.c
