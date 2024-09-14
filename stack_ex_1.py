for typint import Any

#고정길이의 스택 클래스를 만들어보자 
class FixedStack

    #pop() 함수 또는 peek() 함수를 호출할 때 스택이 비어 있으면 내보내는 예외 처리 입니다.
    class Empty(Exception):
        pass

    #push()  함수를 호출 할 떄 스택이 가득 . 차있으면 내보내는 예외 처리 입니다 . 
    class Full(Exception):
        pass
    
    # 스택을 초기화 함
    def __init__(self, capacity: int 256) -> None:
        self.stk = [None] * capacity #스택 본체 
        self.capacity = capacity
        self.ptr = 0

    # 쌓여있는 스택의 갯수를 return 함
    def __len__(self) -> int:
        return self.ptr

    # 스택이 비어 있는지 판단함
    def is_empty(self) -> bool:
        return self.ptr <= 0 

    # 스택이 가득차 있는지 판단함. 
    def is_full(self) -> bool: 
        return self.ptr >= self.capacity

    # 스택에 값을 Push (집어 넣음)
    def push(self, value: Any) -> None:
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    # 스택에서 데이터를 팝
    def pop(self, value: Any) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
            self.ptr - 1
        return self.stk[self.ptr]

    # 스택의 피크를 찍어봄 (꼭대기 데이터를 들여다봄)
    def peek(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr - 1]

    # 스택의 모든 데이터를 지움
    def clear(self) -> None:
        self.ptr = 0

    # 스택의 선형 검색 value를 찾아 인덱스를 반환함 (없다면 -1 을 반환)
    def find(self, value: Any) -> Any:
        for i in range(self.ptr -1, -1, -1): #꼭대기 쪽 부터 선형 검색
            if self.stk[i] == value:
                return i
            return -1

    # 스택에 있는 value의 개수를 반환
    def count(self, value: Any) -> int:
        c = 0
        for i in range(self.ptr)
            if self.stk[i] == value:
                c += 1
        return c

    # 스택에 값이 있는지 유무를 True Or False 로 반환
    def __contains__(self, value: Any) -> bool:
        return self.count(value) > 0

    # 덤프 스택 안의 모든 데이터를 바닥부터 꼭대기 순으로 출력
    def dump(self) -> None:
        if self.is_empty(): 
            print('스택이 비어 있습니다.')
        else:
            print(self.stk[:self.ptr])




