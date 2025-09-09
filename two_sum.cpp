#include <bits/stdc++.h>
using namespace std;

int main()
{
    vector<int> number = {2, 7, 11, 15}; // use vector for dynamic array
    int target = 9;

    for(int i = 0; i < number.size(); i++)
    {
        for(int j = i + 1; j < number.size(); j++)
        {
            if(number[i] + number[j] == target)
            {
                cout << "Found at indices: " << i << " and " << j << endl;
            }
        }
    }

    return 0;
}
