#include <iostream>
using namespace std;
#include<iomanip>

int main()
{
    cout<<fixed<<setprecision(5);
    float A;
    float B;
    
    cin >> A;
    cin >> B;
    
    float media = (A*3.5 + B*7.5) / 11;
    
    cout <<"MEDIA = "<< media << endl;
}