#include <iostream>
#include <stdlib.h>


using namespace std;


int main()
{

int pipsel{3};

while(1 == 1)
{

cout << "\npip or pip3 ? (1 or 3) : ";
cin >> pipsel ;


if (pipsel == 1)
{
system("pip install pytube");
break;
}


else if (pipsel == 3)
{
system("pip3 install pytube");
break;
}


else
{
cout <<"\ngive a valid input.\n";
}


}//while end


cout << "\npackage installed successfully : pytube";
return 0;
}
