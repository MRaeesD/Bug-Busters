def hanoi(height, start=1, end=3):
                steps = []
                if height > 0:
                    helper = 6 - start - end  # 6 is the sum of pegs 1, 2, 3
                    steps.extend(hanoi(height - 1, start, helper))
                    steps.append((start, end))
                    steps.extend(hanoi(height - 1, helper, end))

                return steps