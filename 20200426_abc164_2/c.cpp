#include <algorithm>
#include <bitset>
#include <cmath>
#include <ctime>
#include <iostream>
#include <list>
#include <map>
#include <math.h>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <stdio.h>
#include <string>
#include <tuple>
#include <vector>

using namespace std;

int main() {
    int n;
    std::set<string> st;
    cin >> n;
    for (int i = 0; i < n; i++) {
        string ipt;
        cin >> ipt;
        st.insert(ipt);
    }
    cout << st.size() << endl;
    return 0;
}