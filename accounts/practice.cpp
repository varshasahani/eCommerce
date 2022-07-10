#include <iostream>

using namespace std;

int search(int arr[],int n,int e){
   for(int pos=0; pos<n;++pos){
      if(arr[pos]==e){
         return pos;

      }
   }
   return -1;
}

int main(){
  int n,e ,arr[]={2,4,5,1,8,4,23,13,24};
  cin>>n>>e
  cout<<search(arr,n,e);
  return 0;
}