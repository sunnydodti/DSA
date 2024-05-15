#include <iostream>
using namespace std;

int *bubbleSort(int elements[], int length)
{
    for (int i = 0; i < length; i++)
    {
        for (int j = 0; j < length; j++)
            if (elements[j] > elements[j + 1])
            {
                int temp = elements[j];
                elements[j] = elements[j + 1];
                elements[j + 1] = temp;
            }
    }
    return elements;
}

int *bubbleSortOptimized(int elements[], int length)
{
    for (int i = 0; i < length - 1; i++)
    {
        for (int j = 0; j < length - 1 - i; j++)
            if (elements[j] > elements[j + 1])
            {
                int temp = elements[j];
                elements[j] = elements[j + 1];
                elements[j + 1] = temp;
            }
    }
    return elements;
}

void print(int array[], int size, const string message)
{
    if (!message.empty())
        cout << message << " ";

    for (int i = 0; i < size; i++)
    {
        std::cout << array[i] << " ";
    }
    cout << std::endl;
}

int main()
{
    int size = 6;

    int input1[size] = {7, 0, 3, 5, 9, 1};
    int input2[size] = {7, 0, 3, 5, 9, 1};

    print(input1, size, "");
    print(bubbleSort(input1, size), size, "bubbleSort");
    print(bubbleSortOptimized(input2, size), size, "bubbleSortOptimized");
}