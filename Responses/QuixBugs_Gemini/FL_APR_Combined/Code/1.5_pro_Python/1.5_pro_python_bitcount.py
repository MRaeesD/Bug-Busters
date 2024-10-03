def bitcount(n):
        """
        Bitcount

        Args:
            n: a nonnegative int

        Returns:
            The number of 1-bits in the binary encoding of n

        Examples:
            >>> bitcount(127)
            7
            >>> bitcount(128)
            1
        """
        count = 0
        while n:
            n ^= n - 1
            count += 1
        return count
