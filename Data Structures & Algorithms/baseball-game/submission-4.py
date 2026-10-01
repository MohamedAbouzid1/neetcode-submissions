class Solution:
    def calPoints(self, operations: List[str]) -> int:

        ops = []

        for i in range(len(operations)):
            if operations[i] == "+":
                sum_prev_two = ops[-1] + ops[-2] 
                ops.append(sum_prev_two)
            elif operations[i] == "D":
                double_prev_two = ops[-1] * 2
                ops.append(double_prev_two)
            elif operations[i] == "C":
                ops.pop()
            else:
                ops.append(int(operations[i]))

        return sum(ops)