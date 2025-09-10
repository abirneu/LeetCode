def max_skill():
    R,B = map(int, input().split())
    green = min(R, B)
    remaining_red = R - green
    remaining_blue = B - green
    
    skill = remaining_red * 1 + remaining_blue * 2 + green * 5
    print(skill)
