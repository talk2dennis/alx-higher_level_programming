#include "lists.h"

/**
 * insert_node - A functin that inserts a node in a sorted list
 * @head: pointer to the sorted list
 * @number: int to insert
 * Return: pointer to the inserted node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = malloc(sizeof(listint_t));
	listint_t *tmp = *head;

	if (node == NULL)
		return (NULL);
	node->n = number;
	if (*head == NULL || (*head)->n > number)
	{
		node->next = *head;
		*head = node;
		return (node);
	}

	while (tmp->next != NULL)
	{
		if (tmp->next->n >= number)
		{
			node->next = tmp->next;
			tmp->next = node;
			return (node);
		}
		tmp = tmp->next;
	}
	node->next = NULL;
	tmp->next = node;
	return (node);

}
