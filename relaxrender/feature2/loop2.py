def loop2(ox, oy, d, circles, blockers):
    max_circle = center_circle = (ox, oy, max_circle_one_point(ox, oy, circles, blockers))
    for i in range(1, 16):
        #x0 = d*math.cos((i/9) * math.pi / 4)
        #y0 = d*math.sin((i/9) * math.pi / 4)
        if i == 1 or i == 2 or i == 3:
            x0 = ox + d
        if i == 5 or i == 6 or i == 7:
            x0 = ox - d
        if i == 4 or i == 8:
            x0 = ox
        if i == 3 or i == 4 or i == 5:
            y0 = oy + d
        if i == 7 or i == 8 or i == 1:
            y0 = oy - d
        if i == 2 or i == 6:
            y0 = oy
        if i == 10:
            x0 = ox - d/2
             y0 = oy + d/2
        if i == 11:
            x0 = ox - d / 2
            y0 = oy - d / 2
        if i == 12:
            x0 = ox + d / 2
            y0 = oy - d / 2
        if i == 13:
            x0 = ox + d / 2
            y0 = oy + d / 2
        this_circle = (x0, y0, max_circle_one_point(x0, y0, circles, blockers))
        if this_circle[2] >= max_circle[2]:
            center_circle2 = second_circle = max_circle
          max_circle = this_circle
    if max_circle[2] - center_circle[2] < 0.00000001 :
        return max_circle
        #if second_circle[2] - center_circle2 <0.0000001:
            #if max_circle[2] > second_circle[2]:
                #return max_circle
        # else:
        #return second_circle
        #else:
              #return max_in_nine_points(second_circle[0], second_circle[1], d/2, circles, blockers)
    else:
        return max_in_nine_points(max_circle[0], max_circle[1], d/3 , circles, blockers)
        def max_circle_one_point(ox, oy, circles, blockers):
    if (not (ox <= 1 and ox >= -1)) \
            or (not (oy <= 1 and oy >= -1)):
        return 0
    minb = min(ox+1, 1-ox, oy+1, 1+oy)
        minc = 2
    for circle in circles:
        if math.sqrt((ox - circle[0])**2 + (oy - circle[1])**2) - circle[2] < minc:
            minc = math.sqrt((ox - circle[0])**2 + (oy - circle[1])**2) - circle[2]
    mind = 2
    for blocker in blockers:
        if math.sqrt((ox - blocker[0])**2 + (oy - blocker[1])**2) < mind:
            mind = math.sqrt((ox - blocker[0])**2 + (oy - blocker[1])**2)
    if min(minb, minc, mind) >= 0:
        r = min(minb, minc, mind)
    else:
         r = 0
    return r
