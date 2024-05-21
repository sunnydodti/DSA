#include <iostream>
using namespace std;

void merge(int elements[], int start, int middle, int end)
{
    int leftSize = middle - start + 1;
    int rightSize = end - middle;

    int leftArray[leftSize], rightArray[rightSize];

    for (int i = 0; i < leftSize; i++)
    {
        leftArray[i] = elements[start + i];
    }

    for (int i = 0; i < rightSize; i++)
    {
        rightArray[i] = elements[middle + i + 1];
    }

    int leftI = 0, rightI = 0, mergedI = start;

    while (leftI < leftSize && rightI < rightSize)
    {
        if (leftArray[leftI] < rightArray[rightI])
        {
            elements[mergedI] = leftArray[leftI];
            leftI++;
        }
        else
        {
            elements[mergedI] = rightArray[rightI];
            rightI++;
        }
        mergedI++;
    }

    while (leftI < leftSize)
    {
        elements[mergedI] = leftArray[leftI];
        leftI++;
        mergedI++;
    }

    while (rightI < rightSize)
    {
        elements[mergedI] = rightArray[rightI];
        rightI++;
        mergedI++;
    }
}

void mergeSortRecursive(int elements[], int start, int end)
{
    if (start >= end)
        return;

    int middle = start + (end - start) / 2;
    mergeSortRecursive(elements, start, middle);
    mergeSortRecursive(elements, middle + 1, end);
    merge(elements, start, middle, end);
}

int *mergeSort(int elements[], int length)
{
    mergeSortRecursive(elements, 0, length - 1);
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
    print(mergeSort(input1, size), size, "mergeSort");
}