#include "lists.h"

/**
 * check_cycle - A function that detects a cycle in singly linked list
 * @list: A singly linked list
 * Return: (0) if no cycle otherwise (1)
 */


int check_cycle(listint_t *list)
{
	listint_t *current, *next;

	if (list == NULL)
		return (0);
	current = list;
	next = list;
	while(current != NULL && next != NULL && next->next != NULL)
	{
		current = current->next;
		next = next->next->next;
		if(current == next)
			return(1);
	}
	return (0);
}
