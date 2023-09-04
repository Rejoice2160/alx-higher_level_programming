#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if the singly-linked list contain a cycle.
 * @list: A singly-linked list to check
 *
 * Return: If linked list has no cycle - 0.
 *         If it has a cycle - 1.
 */
int check_cycle(listint_t *list)
{
        listint_t *snail, *chicken;

        if (list == NULL || list->next == NULL)
                return (0);

        snail = list->next;
        chicken = list->next->next;

        while (snail && chicken && chicken->next)
        {
                if (snail == chicken)
                        return (1);

                snail = snail->next;
                chicken = chicken->next->next;
        }

        return (0);
