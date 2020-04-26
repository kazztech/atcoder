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
    int th, ta, mh, ma;
    cin >> th >> ta >> mh >> ma;
    while (true) {
        mh -= ta;
        if (mh <= 0) {
            cout << "Yes" << endl;
            return 0;
        }

        th -= ma;
        if (th <= 0) {
            cout << "No" << endl;
            return 0;
        }
    }

    return 0;
}