class MyCircularQueue {
vector<int>arr;
    int front=0,rear=-1,a;
    public:
    MyCircularQueue(int k) {
        arr.resize(k);
        a = k;
    }
    
    bool enQueue(int value) {
        if(isFull())return false;
        
        rear = (rear+1)% a;
        arr[rear] = value;
        return true;
    }
    
    bool deQueue() {
        if(isEmpty()) return false;
        if (front==rear){
            front =0,rear=-1;
        }else{
            front=(front+1)%a;
        }
        return true;
        
    }
    
    int Front() {
        return isEmpty()? -1:arr[front];
        
    }
    
    int Rear() {
        return isEmpty()? -1:arr[rear];
    }
    
    bool isEmpty() {
        return rear == -1;
    }
    
    bool isFull() {
        return !isEmpty() and (rear +1)%a ==front;
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */