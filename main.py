class A:
    """
    Represents class A.
    """
    def introduce(self) -> str:
        """
        Introduces class A.

        Returns:
        - str: Introduction message for class A.
        """
        return "This is class A"


class B(A):
    """
    Represents class B, a subclass of A.
    """
    def introduce(self) -> str:
        """
        Introduces class B.

        Returns:
        - str: Introduction message for class B.
        """
        return "This is class B"


class C(A):
    """
    Represents class C, a subclass of A.
    """
    # def introduce(self) -> str:
    # """
    # Introduces class C.
    #
    # Returns:
    # - str: Introduction message for class C.
    # """
    #     return "This is class C"
    ...


class D(B, C):
    """
    Represents class D, a subclass of both B and C.
    """
    # def introduce(self) -> str:
    # """
    # Introduces class D.
    #
    # Returns:
    # - str: Introduction message for class D.
    # """
    #     return "This is class D"
    ...


def main() -> None:
    """
    Main function to demonstrate the usage of classes A, B, C, and D.
    """
    a_ins = A()
    b_ins = B()
    c_ins = C()
    d_ins = D()
    print(a_ins.introduce())
    print(b_ins.introduce())
    print(c_ins.introduce())
    print(d_ins.introduce())
    print(D.mro())


if __name__ == "__main__":
    main()
