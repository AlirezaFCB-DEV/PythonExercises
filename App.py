def http_error(status):
    match(status):
        case 400:
            return "Bad Request"
        case 401 | 402 | 403:
            return "Not Allowed "
        case 404:
            return "Not Found"
        case 418:
            return "I'm A Teapot"
        case _:
            return "Something's wrong with the internet"


print(http_error(401))


point = (0, 0)
point = (5, 0)
point = (0, 6)
point = (5, 6)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x} , Y={y}")
    case _:
        raise ValueError("Not A Point!!")


class Point1:
    __match_args__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

    #     Point(1, var)
    # Point(1, y=var)
    # Point(x=1, y=var)
    # Point(y=var, x=1)

    # def where_is(point):
    #     match point:
    #         case Point1(x = 0 , y =0) :
    #             print("Origin")
    #         case Point1(x = 0 , y = y):
    #             print(f"Y={y}")
    #         case Point1(x = x , y = 0) :
    #             print(f"X={x}")
    #         case Point1() :
    #             print("Somewhere Else")
    #         case _ :
    #             print("Not A Point")


points = [Point1(0, 0)] 
points = [Point1(5, 6)] 
# points = [Point1(0, 2), Point1(0, 3)]  
points = [Point1(12, 16), Point1(126, 18)]
# points = []


match points:
    case []:
        print("No Points")
    case [Point1(0, 0)]:
        print("The Origin")
    case [Point1(x, y)]:
        print(f"Single Point {x} , {y}")
    case [Point1(0, y1), Point1(0, y2)]:
        print(f"Two on the Y axis at {y1} , {y2}")
    case [Point1(x1, y1), Point1(x2, y2)]:
        print(f"Second Point x = [{x1, x2}] , y=[{y1, y2}]")
    case _:
        print("Something else")

point2 = Point1( 12 , 16)
point2 = Point1( 12 , 12)

match point2 :
    case Point1(x , y) if x == y :
        print(f"Y=X at {x}")
    case Point1(x ,y) :
        print(f"Not on the diagonal")