/*
    [MEDIUM]
    155. Min Stack

    Concepts:
    - stack
    - design

    Stats:
        Runtime | 2 ms      [Beats 69.04%]
        Memory  | 23.18 MB  [Beats 91.09%]
*/

class MinStack {
public:
    std::vector<std::array<int, 2>> stck = {};

    MinStack() {}
    
    void push(int val) {
        if (this->stck.empty())
            this->stck.push_back({val, val});
        else {
            this->stck.push_back({
                val,
                (
                    (this->stck.back()[1] < val) ?
                    (this->stck.back()[1]) :
                    (val)
                )
            });
        }
    }
    
    void pop() {
        this->stck.pop_back();
    }
    
    int top() {
        return this->stck.back()[0];
    }
    
    int getMin() {
        return this->stck.back()[1];
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */