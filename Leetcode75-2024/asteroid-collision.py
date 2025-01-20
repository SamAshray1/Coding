class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        # Solution by Yangshun Tay
        outputList = []
        for asteroid in asteroids:
            # We only need to resolve collisions under the following conditions:
            # - stack is non-empty
            # - current asteroid is -ve
            # - top of the stack is +ve
            while len(outputList) and asteroid < 0 and outputList[-1] > 0:
                # Both asteroids are equal, destroy both.
                if outputList[-1] == -asteroid:
                    outputList.pop()
                    break
                # Stack top is smaller, remove the +ve asteroid 
                # from the stack and continue the comparison.
                elif outputList[-1] < -asteroid:
                    outputList.pop()
                    continue
                # Stack top is larger, -ve asteroid is destroyed.
                elif outputList[-1] > -asteroid:
                    break
            else:
                # -ve asteroid made it all the way to the 
                # bottom of the stack and destroyed all asteroids.
                outputList.append(asteroid)
        return outputList


