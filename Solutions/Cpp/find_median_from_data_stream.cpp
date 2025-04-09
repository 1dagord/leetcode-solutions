/*
    [HARD]
    295. Find Median from Data Stream

    Concepts:
    - design
    - heap/priority queue
    - data stream

    Stats:
        Runtime | 95 ms     [Beats 13.26%]
        Memory  | 126.91 MB [Beats 9.87%]
*/

class MedianFinder {
public:
    // smaller half
    std::priority_queue<int> max_heap;
    // larger half
    std::priority_queue<int, std::vector<int>, std::greater<int>> min_heap;
    
    MedianFinder() {}
    
    void addNum(int num) {
        // if even...
        if (min_heap.size() == max_heap.size()) {
            // pop old value off of smaller half
            // push new value to smaller half
            // push old value to larger half
            max_heap.push(num);
            min_heap.push(max_heap.top());
            max_heap.pop();
        }

        // pop old value off of larger half
        // push new value to larger half
        // push old value to smaller half
        min_heap.push(num);
        max_heap.push(min_heap.top());
        min_heap.pop();
    }
    
    double findMedian() {
        // if even...
        if (min_heap.size() == max_heap.size()) {
            // average values at top of both heaps
            return ((min_heap.top() + max_heap.top()) / 2.0);
        }
        // if odd, return value at top of min_heap (larger half)
        return min_heap.top();
    }
};

/**
    * Your MedianFinder object will be instantiated and called as such:
    * MedianFinder* obj = new MedianFinder();
    * obj->addNum(num);
    * double param_2 = obj->findMedian();
    */