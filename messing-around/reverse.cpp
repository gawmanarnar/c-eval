#include <algorithm>
#include <string>
#include <stdio.h>

std::string reverse(std::string str) {
    std::reverse(str.begin(),str.end());
    return str;
}

int main(int argc, const char* argv[]) {
    printf("%s\n",reverse("cake").c_str());
}
