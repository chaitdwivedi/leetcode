'''
Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length.  Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id


Example 1:

Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation:
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5


Constraints:

1 <= length <= 50000
At most 50000 calls will be made to set, snap, and get.
0 <= index < length
0 <= snap_id < (the total number of times we call snap())
0 <= val <= 10^9
'''
class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0 
        self.snap_shot = {}
        self.array = [0] * length
        for i in range(length):
            self.set(i, 0)     

    def set(self, index: int, val: int) -> None:
        self.array[index] = val
        if index in self.snap_shot:
            self.snap_shot[index][self.snap_id] = val
        else:
            self.snap_shot[index] = {self.snap_id: val}

    def snap(self) -> int:       
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        def lin_get_id(index, snap_id):
            ids = self.snap_shot[index].keys()
            #print(ids)
            max_id = max(ids)
            if snap_id > max_id:
                #return self.snap_shot[index][max_id]
                return max_id
            for id_ in sorted(ids, reverse=True):
                if id_ < snap_id:
                    #return self.snap_shot[index][id_]
                    return id_
                
        def get_id(index, snap_id):
            ids = sorted(self.snap_shot[index].keys())
            start, end = 0, len(ids) - 1 
            
            if snap_id > ids[end]:
                return ids[end]
            
            ans = -1 
            while start <= end:
                mid = start + (end - start)//2
                if ids[mid] > snap_id:
                    end = mid - 1
                else:
                    ans = mid
                    start = mid + 1 
            
            return ids[ans]
                
        if index not in self.snap_shot:
            return self.array[index]
        
        if snap_id in self.snap_shot[index]:
            return self.snap_shot[index][snap_id]

        # find largest existing snap_id that is smaller than `snap_id`
        return self.snap_shot[index][get_id(index, snap_id)]
            
       
        
        # return self.array[index]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

