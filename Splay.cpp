#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long splay_t;
class Splay{
public:
    struct Node{
        splay_t key;
        int size;
        Node *left, *right, *parent;
        Node(splay_t _key):key(_key),size(1),left(NULL),right(NULL),parent(NULL){}
    };
    Node *root;
    void insert(splay_t key){
        //cout<<"insert "<<key<<endl;
        
        if(!root) {
            root = new Node(key);
            splay(root);
            return;
        }
        Node *t =root;
        while(true){
       //     cout<<"try "<<t->key<<endl;
            
            if(key<t->key){
                if(t->left) t = t->left;
                else break;
            }else{
                if(t->right) t = t->right;
                else break;
            }
        }
        //cout<<"under "<<t->key<<endl;
        if(key<t->key) t->left = new Node(key), t->left->parent = t, t = t->left;
        else t->right = new Node(key), t->right->parent=t, t = t->right;
        splay(t);
        
    }
    int size(Node *x){
        if(!x) return 0;
        else return x->size;
    }
    void update(Node *x){
        x->size = 1+size(x->left) + size(x->right);
    }
    void rotate(Node *x,bool left){
        Node *y = x->parent;
        
        x->parent = y->parent;
        if(!x->parent) root = x;
        else if(x->parent->left == y) x->parent->left = x;
        else x->parent->right = x;
        
        y->parent = x;
        Node *t = NULL;
        if(left) t = x->right, x->right = y, y->left = t;
        else t = x->left, x->left = y, y->right = t;
        if(t) t->parent = y;
        update(y);
    }
    void splay(Node *x){
        while(x->parent){
            if(x->parent->parent==NULL){
                rotate(x,x->parent->left==x);
            }else if((x->parent->left==x)^(x->parent->parent->left == x->parent)){
                rotate(x,x->parent->left==x);
                rotate(x,x->parent->left==x);
            }
            else{
                rotate(x->parent,x->parent->parent->left==x->parent);
                rotate(x,x->parent->left==x);
            }
        }
        update(x);
    }
    
    splay_t select(int k){
        Node *t = root;
        if(k<=0 || size(root)< k) {
            cerr<<"error selecting"<<endl;
            exit(1);
        }
        while(true){
            if(1+size(t->left)==k) break;
            else if(1+size(t->left)>k) t = t->left;
            else k -= 1+ size(t->left), t = t->right;
        }
        splay(t);
//cout<<"selected "<<t->key<<endl;
        return root->key;
    }
    void erase(splay_t key){
      //  cout<<"erasing "<<key<<endl;
      //  cout<<"root is "<<root->key<<endl;
        
        Node *t = root;
        if(!root){
            cerr<<"didn't find a key"<<endl;
            return;
        }
        while(true){
            if(key==t->key) break;
            else if(key<t->key) t = t->left;
            else t = t->right;
        }
        //found key in Node t
        //try to find the next higher key
        Node *x,*y;
        if(!t->left || !t->right){ //delete directly
            y = t->parent;
            
        }else{
            x = t->right;
            while(x->left) x = x->left;
            y = x->parent;
            t->key = x->key;
            t = x;
        }
        if(!y){
            if(t->left) t->left->parent = y, root = t->left;
            else if(t->right) t->right->parent = y, root = t->right;
            else root = NULL;
        }
        else if(y->left == t) {
            if(t->left) t->left->parent = y, y->left = t->left;
            else if(t->right) t->right->parent = y, y->left = t->right;
            else y->left = NULL;
        }
        else {
            if(t->left) t->left->parent = y, y->right = t->left;
            else if(t->right) t->right->parent = y, y->right = t->right;
            else y->right = NULL;
        }
        delete t;
        if(y)splay(y);

        
    }
    Splay():root(NULL){}
};
