"""
You are given an array of N integers separated by spaces, all in one line.

Display the following:
1. Mean (m): The average of all the integers.
2. Median of this array: In case, the number of integers is odd, the middle element; else, the average of the middle two elements.
3. Mode: The element(s) which occurs most frequently. If multiple elements satisfy this criteria, display the numerically smallest one.
4. Standard Deviation (SD).
SD = (((x1-m)2+(x2-m)2+(x3-m)2+(x4-m)2+...(xN-m)2))/N)0.5
where xi is the ith element of the array
5. Lower and Upper Boundary of the 95% Confidence Interval for the mean, separated by a space. This might be a new term to some.
However, it is an important concept with a simple, formulaic solution. Look it up!

Other than the modal values (which should all be integers) the answers should be in decimal form till one place of decimal (0.0 format).
An error margin of +/- 0.1 will be tolerated for the standard deviation and the confidence interval boundaries.
The mean, mode and median values should match the expected answers exactly.
Assume that these numbers were sampled from a normal distribution; the sample is a reasonable representation of the distribution;
a user can approximate that the population standard deviation =~ standard deviation computed for the given points
with the understanding that assumptions of normality are convenient approximations.
"""


class Data:
    def __init__(self, data: list[int]) -> None:
        self.data = data

    def mean(self) -> float:
        return sum(self.data) / len(self.data)

    def median(self) -> float:
        d = sorted(self.data)
        mid = len(d) // 2
        if len(d) % 2 == 1:
            return d[mid]
        else:
            return (d[mid] + d[mid - 1]) / 2

    def mode(self) -> int:
        max = (0, None)
        for x in set(self.data):
            c = self.data.count(x)
            if c > max[0]:
                max = (c, x)
            elif c == max[0]:
                max = (c, min(max[1], x))
        return max[1]

    def standardDeviation(self) -> float:
        mean = self.mean()
        return (sum([(x - mean) ** 2 for x in self.data]) / len(self.data)) ** 0.5

    def marginError95(self) -> float:
        return 1.96 * (self.standardDeviation() / (len(self.data) ** 0.5))


import sys

sys.stdin = open("Basic Statistics Warmup.txt")  # to delete

data = sys.stdin.buffer.read().splitlines()
N = int(data[0])
data_cls = Data(list(map(int, data[1].split())))
print(round(data_cls.mean(), 1))
print(round(data_cls.median(), 1))
print(round(data_cls.mode(), 1))
print(round(data_cls.standardDeviation(), 1))
me = data_cls.marginError95()
print(round(data_cls.mean() - me, 1), round(data_cls.mean() + me, 1))
