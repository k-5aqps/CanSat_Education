# 必要なモジュールをimportする

"""
GPIOの設定をする
"""

def move(duty:int,dir:str) -> None:
    if dir == "f":
        """
        前進
        """
    elif dir == "b":
        """
        後進
        """
    elif dir == "r":
        """
        右折
        """
    elif dir == "l":
        """
        左折
        """
    else:
        """
        while文を抜ける
        """

if __name__ == "__main__":
    duty,dir = input("duty,dir = ").split(",")
    move(duty,dir)