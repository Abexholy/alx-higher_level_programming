#include "lists.h"

/**
 * check_cycle : Function in charge of checking lishg
 * @list : The list on the linked list to be written
 * Return 1: if theres sample or return 0;
 *
 */
int check_cycle(listint_t *list)
{
	listint_t *move, *stop;

		if (!list || !list->next)
			return(0);
	move = list;
	stop = list;

	while (stop != NULL && move != NULL && move->next != NULL)
	{
		stop = stop->next;
		move = move->next->next;
		if (stop == move)
		{
			return (1);
		}
	}
	return (0);
}
