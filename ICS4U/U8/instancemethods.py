import math

class Circle:
    x = 0.0 #x coordinate of circle
    y = 0.0 #y coordinate of circle 
    r = 0.0 #radius

    def area_circle(self,circle):
        return (math.pi*self.circle.r**2)

def user_input():
    while True:
        try:
            x = float(input("Enter the x coordinate of the circle: "))
            y = float(input("Enter the y coordinate of the circle: "))
            r = float(input("Enter the radius of the circle: "))
            if r > 0:
                return x,y,r
        except:
            print("Enter a proper float value")
def main():
    values = user_input()
    c1 = Circle()
    c1.x = values[0]
    c1.y = values[1]
    c1.r = values[2]
    area_of_circle = c1.area_circle(c1)
    print(area_of_circle)

if __name__ == "__main":
    main()