#include "lists.h"

/**
 * check_cycle - A function that detects a cycle in singly linked list
 * @list: A singly linked list
 * Return: (0) if no cycle otherwise (1)
 */


int check_cycle(listint_t *list)
{
	listint_t *current, *fast;

	if (list == NULL)
		return (0);
	current = list;
	fast = list;
	while(fast != NULL && fast->next != NULL)
	{
		current = current->next;
		fast = fast->next->next;
		if(current == fast)
			return(1);
	}
	return (0);
}
