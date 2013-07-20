#include <stdlib.h>
#include <fstream>

void ReadInputFile(const char*);
int fib(int n);

void ReadInputFile(const char* file_path) {
  std::ifstream input_file(file_path);
  for(std::string line; getline(input_file, line);) {
    if(line.empty()) { continue; }
    int nth_fib = atoi(line.c_str());
    printf("%d\n",fib(nth_fib));
  }
  input_file.close();
}

int fib(int n) {
  int fib_numbers[n];
  fib_numbers[0] = 0;
  fib_numbers[1] = 1;
  
  for(int i=2; i <= n; i++) {
    fib_numbers[i] = fib_numbers[i-2] + fib_numbers[i-1];
  }

  return fib_numbers[n];
} 

int main(int argc, const char* argv[]) {
  ReadInputFile(argv[1]);
  return 0;
}
