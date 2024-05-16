#include <iostream>
using namespace std;

int *insertionSort(int elements[], int length)
{
    int current;
    int j;
    for (int i = 1; i < length; i++)
    {
        current = elements[i];
        j = i - 1;
        while (j >= 0 && current < elements[j])
        {
            elements[j + 1] = elements[j];
            j--;
        }
        elements[j + 1] = current;
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
    print(insertionSort(input1, size), size, "insertionSort");
}