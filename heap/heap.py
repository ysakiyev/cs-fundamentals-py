class Heap:
    def __init__(self):
        self.data = [0]  # add dummy to 0 index

    def get(self, idx: int) -> int:
        return self.data[idx]

    def get_left(self, idx: int) -> int:
        return self.data[2 * idx]

    def get_right(self, idx: int) -> int:
        return self.data[2 * idx + 1]

    def get_parent(self, idx: int) -> int:
        return self.data[idx // 2]

    def get_parent_idx(self, idx: int) -> int:
        return idx // 2

    def get_left_idx(self, idx: int) -> int:
        return 2 * idx

    def get_right_idx(self, idx: int) -> int:
        return 2 * idx + 1

    def has_left(self, idx:int) -> bool:
        return 2 * idx < len(self.data)

    def has_right(self, idx: int) -> bool:
        return 2 * idx + 1 < len(self.data)

    def has_parent(self, idx: int) -> bool:
        return idx // 2 >= 0

    def push(self, val:int):
        self.data.append(val)
        idx_cur = len(self.data) - 1

        # heapify up
        while self.has_parent(idx_cur) and self.get(idx_cur) < self.get_parent(idx_cur):
            self.data[self.get_parent_idx(idx_cur)], self.data[idx_cur] = self.data[idx_cur], self.data[self.get_parent_idx(idx_cur)]
            idx_cur = self.get_parent_idx(idx_cur)

    def pop(self):
        if self.size() == 1:
            return None

        if self.size() == 2:
            return self.data.pop()

        res = self.data[1]
        self.data[1] = self.data.pop()

        i = 1
        # heapify down
        while self.has_left(i):
            # if right < cur and right < left
            if self.has_right(i) and self.get_right(i) < self.get_left(i) and self.get_right(i) < self.get(i):
                # swap cur with right
                self.data[i], self.data[self.get_right_idx(i)] = self.data[self.get_right_idx(i)], self.data[i]
                i = self.get_right_idx(i)
            # if cur < left
            elif self.get_left(i) < self.get(i):
                # swap cur with left
                self.data[i], self.data[self.get_left_idx(i)] = self.data[self.get_left_idx(i)], self.data[i]
                self.get_left_idx(i)
            else:
                break

        return res

    def peek(self) -> int:
        return self.data[1]

    def size(self) -> int:
        return len(self.data)





