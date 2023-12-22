#include <iostream>
#include <vector>

using namespace std;

int findLMISLength(const vector<int>& arr) {
    int n = arr.size();
    vector<int> dp(n, 1); // dp[i] stores the length of LMIS ending at index i

    for (int i = 1; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (arr[i] > arr[j] && dp[i] < dp[j] + 1) {
                dp[i] = dp[j] + 1;
            }
        }
    }

    int maxLength = 0;
    for (int i = 0; i < n; ++i) {
        if (dp[i] > maxLength) {
            maxLength = dp[i];
        }
    }

    return maxLength;
}

int main() {
    vector<int> arr = {4, 1, 13, 7, 0, 2, 8, 11, 3};
    
    int result = findLMISLength(arr);

    cout << "Length of Longest Monotonically Increasing Subsequence: " << result << endl;

    return 0;
}