class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [] # pair: car, time

        cars = sorted(zip(position, speed), reverse=True)
        print(cars)
        for car in cars:
            time = (target - car[0]) / car[1]
            if not stack or stack[-1][1] < time:
                stack.append((car, time))
        
        print(stack)
        return len(stack)