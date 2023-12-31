#include "lists.h"

/**
 * insert_node - adds number in a sorted singly linked list.
 * @number: number to insert
 * @head: head of linked list
 *
 * Return: if function fails - NULL
 * Otherwise - pointer to new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;
	
	new->next = node->next;
	node->next = new;

	return (new);
}
