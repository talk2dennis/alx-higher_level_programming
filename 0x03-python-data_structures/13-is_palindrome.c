#include "lists.h"

/**
 * is_palindrome - A function that checks if a list is a palindrome
 * @head: pointer to the list
 * Return: (0) if false otherwise (1)
 */


int is_palindrome(listint_t **head)
{
	listint_t *current;
	int start = 0, end = 0, *buffer = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	current = *head;
	while (current != NULL)
	{
		current = current->next;
		end++;
	}
	buffer = malloc(sizeof(int) *end);
	if (buffer == NULL)
		return (0);
	end = 0;
	current = *head;
	while (current != NULL)
	{
		buffer[end] = current->n;
		current = current->next;
	}
	while (start < (end / 2))
	{
		if (buffer[start] != buffer[end - 1])
		{
			free(buffer);
			return (0);
		}
		start++;
		end--;
	}
	free(buffer);
	return (1);
}
