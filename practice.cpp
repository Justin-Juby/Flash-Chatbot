#include <iostream>
using namespace std;
class example{
  static int a;
  public:
     void add(){
      for (int i=0;i<10;i++){
        a+=i;
        
      }
      cout<<a<<endl;
     }
  };

int example::a = 0;
int main(){
  example e;
  e.add();
  e.add();
  e.add();
  return 0;
  
}