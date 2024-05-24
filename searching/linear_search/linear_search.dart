void main(List<String> args) {
  List<int> input = [4, 7, 9, 0, 3, 1, 5, 8, 5, 3, 5, 7, 8, 9, 2];
  int key = 4;
  print("input: $input");
  print("key: $key");

  print("linear_search: ${linear_search(input, key)}");
  print("linear_search_v2: ${linear_search_v2(input, key)}");
}

linear_search(List<int> input, int key) {
  for (var i = 0; i < input.length; i++) {
    if (input[i] == key) return i;
  }
  return -1;
}

linear_search_v2(List<int> input, int key) {
  int count = 0;
  for (int number in input) {
    if (number == key) return count;
    count++;
  }
  return -1;
}
