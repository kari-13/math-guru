#include <iostream>
#include "json.hpp"
#include <fstream>
#include <string>

using json = nlohmann::json;

int main() {
    //to load the json file 
    std::ifstream file ("math.json");
    if(!file.is_open()){
        std::cerr << "failed to open the json file , please check that you have the math.json file in the same directory as your app is, if you are on a mac run "
    }
}


