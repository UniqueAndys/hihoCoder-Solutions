#include <iostream>
#include <string>
#include <list>
#include <algorithm>

using namespace std;

int eliminateNum(list<char> &strList) {
  // eliminate adj chars
	int cnt = 0;
	int tmp = -1;
	list<char>::iterator it1, it2;
	int len;
	while (cnt > tmp && !strList.empty()) {
		tmp = cnt; // save last state
		it1 = it2 = strList.begin();
		++it2;
		len = 1;
		while (it2 != strList.end()) {
			if (*it2 != *it1) {
				if (len > 1) {
          // eliminate len chars
					cnt += len;
					while (len) {
						it1 = strList.erase(it1);
						--len;
					}
					++it2, ++len;
				}
				else {
					++it1, ++it2;
				}
			}
			else {
				++it2, ++len;
			}
		}
		if (len > 1) {
			cnt += len;
			while (len) {
				it1 = strList.erase(it1);
				--len;
			}
		}
	}
	return cnt;
}

int main()
{
	char character[3] = { 'A', 'B', 'C' };
	int T;
	cin >> T;
	string s;
	for (int t = 0; t < T; ++t) {
		cin >> s;
		list<char> strList;
    // convert a string to list
		for (int i = 0; i < s.size(); ++i)
			strList.push_back(s[i]);
		list<char>::iterator it;
		int maxCnt = 0, cnt;
		for (it = strList.begin(); it != strList.end(); ++it) {
			for (int i = 0; i < 3; ++i) {
        // insert a char to each position
				strList.insert(it, character[i]);
				--it;
				list<char> newList = strList;
				cnt = eliminateNum(newList);
				maxCnt = max(cnt, maxCnt);
				it = strList.erase(it);
			}
		}
		cout << maxCnt << endl;
	}
	return 0;
}
