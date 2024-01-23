#include "lists.h"
#include <stdio.h>

void reversal(listint_t **head);
int comp_list(listint_t *head, listint_t *middle, int len);

/**
 * is_palindrome - it checks for slingly linked in palidrome
 *
 * @head: point into thr pointer of first node in the list passed
 *
 * Return: 0 if palidrome is not detected and 1 if palidrome is
 */

int is_palindrome(listint_t **head)
{
	int lan, j;
	listint_t *tmp;
	listint_t *middle;

	if (head == NULL || *head == NULL)
		return (1);
	tmp = *head;
	middle = *head;

	for (lan = 0; tmp != NULL; lan++)
		tmp =tmp->next;

	lan = lan / 2;

	for (j = 1; j < lan; j++)
		middle = middle->next;
	if (lan % 2 != 0 && lan != 1)
	{
	 	middle = middle->next;
		lan = lan - 1;
	}
	reversal(&middle);
	j = comp_list(*head, middle, lan);

	return (j);
}

/**
 * @middle: pointer to middle3 node
 * @lan: lenght of the list
 * comp_list - compare two lists
 * @head: pointer to head node
 * Return: return 1 if it is the sum return 0 if not sum
 *
 */
int comp_list(listint_t *head, listint_t *middle, int lan)
{
	int j;

	if  (head == NULL || middle == NULL)
		return (1);
	for (j = 0; j < lan; j++)
	{
		if (head->n != middle->n)
			return (0);
		head = head->next;
		middle = middle->next;
	}
	return (1);
}

/**
 * reversal - reverse a list
 * @head: it is a pointer to the head been reversed
 */
void reversal(listint_t **head)
{
	listint_t *current;
	listint_t *next;
	listint_t *prev;

	if (head == NULL || *head == NULL)
		return;

	prev = NULL;
	current = *head;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}
