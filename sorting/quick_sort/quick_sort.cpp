#include <iostream>
using namespace std;

int partition(int elements[], int start, int end)
{
    int pivot = elements[end];
    int swapIndex = start - 1;
    int temp;
    for (int i = start; i < end; i++)
    {
        if (elements[i] < pivot)
        {
            swapIndex++;

            temp = elements[swapIndex];
            elements[swapIndex] = elements[i];
            elements[i] = temp;
        }
    }

    swapIndex++;

    temp = elements[swapIndex];
    elements[swapIndex] = elements[end];
    elements[end] = temp;

    return swapIndex;
}

int *quickSort(int elements[], int start, int end)
{
    if (start < end)
    {
        int pivot = partition(elements, start, end);
        quickSort(elements, start, pivot - 1);
        quickSort(elements, pivot + 1, end);
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

    print(input1, size, "");
    print(quickSort(input1, 0, size), size, "quickSort");
}