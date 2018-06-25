
#取小数部分
# def fract(input):
#     output=input-int(input)
#     if output>0:
#         return output
#     else:
#         return (1+output)

#把数据限制在0-1
def clamp(input):
    if input<0.:
        #为了覆盖率注释了
        return 0
    elif input<1.:
        return input
    else:
        return 1


