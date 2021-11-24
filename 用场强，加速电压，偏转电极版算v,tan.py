def speed(E,L,U,b=176000000000):
	print('*********龙奕光牛逼*********')
	tan = E*L/2/U
	v=(b*(E*L*tan + 2*U))**(1/2)
	print('tan的近似值为', tan)
	print('离开速度v近似值为',v)
speed(5000,0.06,1000)