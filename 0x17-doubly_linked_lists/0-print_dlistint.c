#include <stdio.h>
#include <stddef.h>

typedef struct dlistint_s {
    int n;
    struct dlistint_s *prev;
    struct dlistint_s *next;
} dlistint_t;

size_t print_dlistint(const dlistint_t *h) {
    size_t node_count = 0;

    while (h != NULL) {
        printf("%d\n", h->n);
        h = h->next;
        node_count++;
    }

    return node_count;
}


