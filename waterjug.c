#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Struct to represent a state of the jugs
typedef struct {
    int jug1, jug2;
} State;

// Queue implementation for BFS
typedef struct {
    State states[1000];
    int front, rear;
} Queue;

// Initialize queue
void initQueue(Queue *q) {
    q->front = q->rear = -1;
}

// Check if queue is empty
bool isEmpty(Queue *q) {
    return q->front == -1;
}

// Enqueue operation
void enqueue(Queue *q, State s) {
    if (q->rear == 999) {
        printf("Queue overflow\n");
        exit(1);
    }
    if (q->front == -1) q->front = 0;
    q->states[++q->rear] = s;
}

// Dequeue operation
State dequeue(Queue *q) {
    if (isEmpty(q)) {
        printf("Queue underflow\n");
        exit(1);
    }
    State s = q->states[q->front];
    if (q->front == q->rear) q->front = q->rear = -1;
    else q->front++;
    return s;
}

// Function to check if a state is the goal state
bool isGoalState(State s, int goal) {
    return s.jug1 == goal || s.jug2 == goal;
}

// Function to pour water between jugs
State pour(State s, int fromJugCapacity, int toJugCapacity, bool fromJug1ToJug2) {
    int transfer = 0;
    if (fromJug1ToJug2) {
        transfer = s.jug1 < (toJugCapacity - s.jug2) ? s.jug1 : (toJugCapacity - s.jug2);
        s.jug1 -= transfer;
        s.jug2 += transfer;
    } else {
        transfer = s.jug2 < (fromJugCapacity - s.jug1) ? s.jug2 : (fromJugCapacity - s.jug1);
        s.jug2 -= transfer;
        s.jug1 += transfer;
    }
    return s;
}

// BFS algorithm
void bfs(int jug1Capacity, int jug2Capacity, int goal) {
    Queue queue;
    initQueue(&queue);
    bool visited[1000][1000] = {false};  // Keeps track of visited states

    // Starting state: Jug1 full, Jug2 empty
    State startState = {jug1Capacity, 0};
    enqueue(&queue, startState);
    visited[startState.jug1][startState.jug2] = true;

    printf("Exploring states:\n");

    while (!isEmpty(&queue)) {
        State currentState = dequeue(&queue);
        printf("Current state: Jug1 = %d, Jug2 = %d\n", currentState.jug1, currentState.jug2);

        if (isGoalState(currentState, goal)) {
            printf("\nGoal reached: Jug1 = %d, Jug2 = %d\n", currentState.jug1, currentState.jug2);
            return;
        }

        // Generate next possible states
        State nextStates[6] = {
            {jug1Capacity, currentState.jug2},         // Fill Jug1
            {currentState.jug1, jug2Capacity},         // Fill Jug2
            {0, currentState.jug2},                    // Empty Jug1
            {currentState.jug1, 0},                    // Empty Jug2
            pour(currentState, jug1Capacity, jug2Capacity, true),  // Pour Jug1 to Jug2
            pour(currentState, jug1Capacity, jug2Capacity, false)  // Pour Jug2 to Jug1
        };

        // Process each next state
        for (int i = 0; i < 6; i++) {
            State nextState = nextStates[i];
            if (!visited[nextState.jug1][nextState.jug2]) {
                visited[nextState.jug1][nextState.jug2] = true;
                enqueue(&queue, nextState);
            }
        }
    }

    printf("No solution found.\n");
}

// Main function
int main() {
    int jug1Capacity, jug2Capacity, goal;

    printf("Enter the capacity of Jug 1: ");
    scanf("%d", &jug1Capacity);
    printf("Enter the capacity of Jug 2: ");
    scanf("%d", &jug2Capacity);
    printf("Enter the desired final state (goal): ");
    scanf("%d", &goal);

    if (goal > jug1Capacity && goal > jug2Capacity) {
        printf("Goal state cannot be greater than the capacity of either jug.\n");
        return 1;
    }

    bfs(jug1Capacity, jug2Capacity, goal);

    return 0;
}