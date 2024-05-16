List<int> insertionSort(List<int> elements) {
  for (var i = 1; i < elements.length; i++) {
    int current = elements[i];
    int j = i - 1;

    while (j >= 0 && current < elements[j]) {
      elements[j + 1] = elements[j];
      j--;
    }

    elements[j + 1] = current;
  }
  return elements;
}

void main() {
  List<int> input = [3, 19, 8, 2, 5, 1];
  print(input);
  print("insertionSort ${insertionSort(List<int>.from(input))}");
}
