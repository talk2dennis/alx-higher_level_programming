#include "lists.h"

/**
 * is_palindrome - A function that checks if a list is a palindrome
 * @head: pointer to the list
 * Return: (0) if false otherwise (1)
 */


int is_palindrome(listint_t **head)
{
	listint_t *current;
	int start = 0, end = 0, buffer[1024];

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	current = *head;
	while (current != NULL)
	{
		buffer[end] = current->n;
		current = current->next;
		end++;
	}
	while (start < end)
	{
		if (buffer[start] != buffer[end - 1])
			return (0);
		start++;
		end--;
	}
	return (1);
}
