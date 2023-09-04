#ifndef LISTS_H
#define LISTS_H

#include <stddef.h>

/**
 * struct ListNode - singly linked list
 * @value: integer value stored in the node
 * @next: pointer to the next node
 */
typedef struct ListNode
{
    int value;
    struct ListNode *next;
} ListNode;

/**
 * print_listint - Print all elements of a singly linked list.
 * @h: A pointer to the head of the list.
 * Return: The number of nodes in the list.
 */
size_t print_listint(const ListNode *h);

/**
 * add_nodeint - Add a new node at the beginning of a singly linked list.
 * @head: A pointer to the pointer to the head of the list.
 * @n: The integer value to store in the new node.
 * Return: A pointer to the new node, or NULL if it fails.
 */
ListNode *add_nodeint(ListNode **head, const int n);

/**
 * free_listint - Free memory used by a singly linked list.
 * @head: A pointer to the head of the list.
 */
void free_listint(ListNode *head);

/**
 * check_cycle - Check if a cycle exists in a linked list.
 * @list: A pointer to the head of the list.
 * Return: 1 if a cycle exists, 0 otherwise.
 */
int check_cycle(ListNode *list);

#endif /* LISTS_H */
