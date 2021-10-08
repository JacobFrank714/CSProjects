#include <iostream>
#include <vector>
#include "omp.h"
#define size 4
using namespace std;

int Dot_Product_Reg(vector <int> vect_a, vector <int> vect_b) {
    int prod;
    prod = 0;
    for (int i = 0; i < size; i++) {
        prod += vect_a[i] * vect_b[i];
    }
    return prod;
}

int Dot_Product_Par(vector <int> vect_a, vector<int> vect_b) {
    int product = 0;

    #pragma omp parallel num_threads(3) for
        for (int i = 0; i < size; i++)
        {
            product += vect_a[i] * vect_b[i];
        }
    return product;
}



int main() {
    vector <int> vector_a = {5, 8, 4, 3};
    vector <int> vector_b = {6, 3, 1, 2};
    cout << "Dot product regular:" << endl;
    cout << Dot_Product_Reg(vector_a, vector_b) << endl;
    cout << "Dot product with openMP" << endl;
    cout << Dot_Product_Par(vector_a, vector_b) << endl;
    return 0;
}