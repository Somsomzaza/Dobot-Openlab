import math

#width = 54mm
#thickness = 85.55 mm
#length = 0.82mm

dType.SetPTPJointParams(api,200,200,200,200,200,200,200,200,0)
dType.SetPTPCoordinateParams(api,200,200,200,200,0)
dType.SetPTPJumpParams(api, 10, 200,0)
dType.SetPTPCommonParams(api, 100, 100,0)

pos = dType.GetPose(api)
rHead = pos[3]

width = 54
thickness = 0.8
length = 85.55

card_num = 1
card_pile = 0

home_x = 188.5147;home_y = 6.8836 ;home_z = -64.0975 + 50.0 #+ thickness * 6 + 10  # initial home postion
move_x = width * 1.4 # (difference between start and end)
move_y = length * 1.2  # (difference between start and end)
z_final = -64.1392

#fixed position pile 1
x1 = home_x + move_x
y1 = home_y + move_y

#fixed position pile 2
x2 = home_x + move_x
y2 = home_y

#fixed position pile 3
x3 = home_x + move_x
y3 = home_y - move_y
print(x1)
print(x2)
print(x3)
print(y1)
print(y2)
print(y3)



for i in range(2):
   #Home postion at current Z at each card
   dType.SetPTPCmd(api, 2, home_x, home_y, home_z , rHead, 1)
   dType.SetPTPCmd(api, 2, home_x, home_y, home_z - 50.0 - (thickness * (card_num - 1)) , rHead, 1)
   dType.SetEndEffectorSuctionCup(api, 1,1,1)
   dType.SetPTPCmd(api, 2, home_x, home_y, home_z , rHead, 1)
   dType.SetPTPCmd(api, 2, x1, y1, home_z , rHead, 1)
   dType.SetPTPCmd(api, 2, x1, y1, home_z , rHead, 1)
   dType.SetPTPCmd(api, 2, x1, y1, z_final + card_pile * thickness , rHead, 1)
   dType.SetEndEffectorSuctionCup(api, 1,0,1)
   card_pile += 1
   dType.SetPTPCmd(api, 2, x1, y1, home_z , rHead, 1)
   dType.SetPTPCmd(api, 2, home_x, home_y, home_z , rHead, 1)
   card_num += 1

   dType.SetPTPCmd(api, 2, home_x, home_y, home_z , rHead, 1)
   dType.SetPTPCmd(api, 2, home_x, home_y, home_z - 50.0 - (thickness * (card_num - 1)) , rHead, 1)
   dType.SetEndEffectorSuctionCup(api, 1,1,1)
   dType.SetPTPCmd(api, 2, home_x, home_y, home_z , rHead, 1)
   dType.SetPTPCmd(api, 2, x2, y2, home_z , rHead, 1)
   dType.SetPTPCmd(api, 2, x2, y2, home_z , rHead, 1)
   dType.SetPTPCmd(api, 2, x2, y2, z_final + card_pile * thickness , rHead, 1)
   dType.SetEndEffectorSuctionCup(api, 1,0,1)
   card_pile += 1
   dType.SetPTPCmd(api, 2, x2, y2, home_z , rHead, 1)
   dType.SetPTPCmd(api, 2, home_x, home_y, home_z , rHead, 1)
   card_num += 1


   dType.SetPTPCmd(api, 2, home_x, home_y, home_z , rHead, 1)
   dType.SetPTPCmd(api, 2, home_x, home_y, home_z - 50.0 - (thickness * (card_num - 1)) , rHead, 1)
   dType.SetEndEffectorSuctionCup(api, 1,1,1)
   dType.SetPTPCmd(api, 2, home_x, home_y, home_z , rHead, 1)
   dType.SetPTPCmd(api, 2, x3, y3, home_z , rHead, 1)
   dType.SetPTPCmd(api, 2, x3, y3, home_z , rHead, 1)
   dType.SetPTPCmd(api, 2, x3, y3, z_final + card_pile * thickness , rHead, 1)
   dType.SetEndEffectorSuctionCup(api, 1,0,1)
   card_pile += 1
   dType.SetPTPCmd(api, 2, x3, y3, home_z , rHead, 1)
   dType.SetPTPCmd(api, 2, home_x, home_y, home_z , rHead, 1)
   card_num += 1
