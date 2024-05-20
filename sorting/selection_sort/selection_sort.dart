List<int> selectionSort(List<int> elements) {
  int length = elements.length;
  late int temp;
  for (var i = 0; i < length - 1; i++) {
    int minElementIndex = i;
    for (var j = i; j < length; j++) {
      if (elements[j] < elements[minElementIndex]) {
        minElementIndex = j;
      }
    }

    temp = elements[i];
    elements[i] = elements[minElementIndex];
    elements[minElementIndex] = temp;
  }
  return elements;
}

void main() {
  List<int> input = [3, 19, 8, 2, 5, 1,0];
  print(input);
  print("selectionSort ${selectionSort(List<int>.from(input))}");
}
