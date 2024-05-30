void main(List<String> args) {
  List<int> input = [4, 7, 9, 0, 3, 1, 5, 8, 5, 3, 5, 7, 8, 9, 2];
  input.sort();
  int key = 8;
  print("input: $input");
  print("key: $key");

  print("binarySearch: ${binarySearch(input, key)}");

  key = 0;
  print("key: $key");
  print("binarySearch: ${binarySearch(input, key)}");
  key = 5;
  print("key: $key");
  print("binarySearch: ${binarySearch(input, key)}");
  key = 50;
  print("key: $key");
  print("binarySearch: ${binarySearch(input, key)}");
}

int binarySearch(List<int> elements, int key) {
  if (elements.isEmpty) return -1;

  int left = 0;
  int right = elements.length - 1;

  while (left <= right) {
    int mid = (left + (right - left) / 2).floor();

    if (elements[mid] == key) return mid;

    if (key < elements[mid])
      right = mid - 1;
    else
      left = mid + 1;
  }

  return -1;
}
