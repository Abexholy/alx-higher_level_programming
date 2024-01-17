#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
#include <unistd.h>
/**
 * insert_node - this is a number to a sorted list
 *
 * @head: a linked list of the code
 *
 * @number: number to be inserted to the code
 *
 * Return: Apointer to the head
 *
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *rageing = *head;
	listint_t *onew = NULL;
	listint_t *tonew = NULL;

	if (!head)
		return (NULL);

	onew = malloc(sizeof(listint_t));
	if (!onew)
		return (NULL);
	onew->n = number;
	onew->next = NULL;

	if (!*head || (*head)->n > number)
	{
		onew->next = *head;
		return (*head = onew);
	}
	else
	{
		while (rageing && rageing->n < number)
		{
			tonew = rageing;
			rageing = rageing->next;
		}

		tonew->next = onew;
		onew->next = rageing;
	}
	return (onew);
}
