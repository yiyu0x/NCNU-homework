#include <iostream>
#include <iomanip>
#include <string>
#include <vector>

using namespace std;

void eraseSpace (string &s) {
	const char ch = ' ';
    s.erase(s.find_last_not_of(" ") + 1);
    s.erase(0, s.find_first_not_of(" "));
}

int isComment(string &s) {
	const char ch = '.';
	return ( s[0] == ch ) ? 1 : 0;
}

void split(string s, vector<string> &box) {

	int current = 0;
	//not have space, likes "RSUB" (only one column)
	int next = s.find_first_of(" ", current);
	if (next == string::npos) {
		box.push_back(s);
		return;
	}
	
	int timer = 3;
	while (timer--) {
		next = s.find_first_of(" ", current);
		string tmp = s.substr(current, next-current);
		box.push_back(tmp);
		if (next == string::npos) break;
		s = s.substr(next, s.length());
		eraseSpace(s);
	}
}

void upperCase(string &s) {
	int flag = 0;
	for ( int i=0;i<s.length();i++ ) {
		
		if ( ( s[i]=='c' || s[i]=='C' ) && 
			   s[i+1] == '\'' ) {

			flag = 1;
			s[i] = 'C';
		}

		if (flag) continue;
		if ( s[i] >=97 && s[i]<=122 )
			s[i] -= 32;
	}
}

void printFormat(vector<string> stdout_data) {
	cout.flags(ios::left);

	if ( stdout_data.size()==3 ) {
		cout << setw(9) << stdout_data[0]
		     << setw(8) << stdout_data[1]
		     << stdout_data[2];
	} else if ( stdout_data.size()==2 ) {
		// endrd exception
		if ( stdout_data[0] == "ENDRD" ) {
			cout << setw(9) << stdout_data[0]
		     	 << stdout_data[1];
		} else {
			cout << setw(9) << " "
			     << setw(8) << stdout_data[0]
			     << stdout_data[1];
		}
	} else if ( stdout_data.size()==1 ) {
		cout << setw(9) << " "
		     << stdout_data[0];
	}

	cout<<endl;
}
int main() {
	string stdin_data;

	while (getline(cin, stdin_data)) {
		vector<string> stdout_data;
		// getline(cin, stdin_data);

		//ignore comment
		stdin_data = stdin_data.substr(0,35);
		//erase space from head and tail.
		eraseSpace(stdin_data);
		//if string's head has '.' , jump to next one.
		if ( isComment(stdin_data) ) {
			continue;
		}

		upperCase(stdin_data);
		split(stdin_data, stdout_data);
		printFormat(stdout_data);
	}
}