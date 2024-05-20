#include <iostream>
using namespace std;

int *selectionSort(int elements[], int length)
{
    int i, j, temp, min_element_index;
    for (i = 0; i < length - 1; i++)
    {
        min_element_index = i;
        for (j = i + 1; j < length; j++)
        {
            if (elements[j] < elements[min_element_index])
            {
                min_element_index = j;
            }
        }
        temp = elements[i];
        elements[i] = elements[min_element_index];
        elements[min_element_index] = temp;
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
    print(selectionSort(input1, size), size, "selectionSort");
}