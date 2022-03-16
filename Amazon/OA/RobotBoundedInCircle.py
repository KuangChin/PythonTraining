class RobotBoundedInCircle:
    def sol(self, input):
        d_R = {}
        d_L = {}

        d_R[(0, 1)] = (1, 0)
        d_R[(1, 0)] = (0, -1)
        d_R[(0, -1)] = (-1, 0)
        d_R[(-1, 0)] = (0, 1)

        d_L[(0, 1)] = (-1, 0)
        d_L[(-1, 0)] = (0, -1)
        d_L[(0, -1)] = (1, 0)
        d_L[(1, 0)] = (0, 1)

        x = 0
        y = 0

        d = (0, 1)

        for i in input:
            if i == 'G':
                x += d[0]
                y += d[1]
            elif i == 'L':
                d = d_L[d]
            elif i == 'R':
                d = d_R[d]
        if x==0 and y==0:
            return True
        elif d == (0, 1):
            return False
        else:
            return True

test = RobotBoundedInCircle()
print(test.sol("GGLLLLGG"))