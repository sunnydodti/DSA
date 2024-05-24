#include <iostream>
using namespace std;

int linearSearch(int input[], int key, int size)
{
    for (int i = 0; i < size; i++)
    {
        if (input[i] == key)
        {
            return i;
        }
    }
    return -1;
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
    int input[] = {4, 0, 9, 0, 3, 2, 5, 8, 5, 3, 5, 7, 8, 1, 2};
    int key = 20;
    int size = sizeof(input) / sizeof(input[0]);

    print(input, size, "input:");
    cout << "key: " << key << "\n";
    cout << "linearSearch: " << linearSearch(input, key, size);
}
