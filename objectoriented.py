#Object Oriented Udemy Homework 
class Line:
	def __init__(self,coor1,coor2):
		self.coor1 = coor1
		self.coor2 = coor2
	def distance(self):
		x1,y1=self.coor1
		x2,y2=self.coor2
		dist=((x2-x1)**2+(y2-y1)**2)**0.5
		return dist
	def slope(self):
		x1,y1=self.coor1
		x2,y2=self.coor2
		slp=(y2-y1)/(x2-x1)
		return slp
coordinate1=(3,2)
coordinate2=(8,10)
li=Line(coordinate1,coordinate2)
dist_li=li.distance()
slp_li=li.slope()
print(slp_li,dist_li)
class Cylinder:
	def __init__(self,height=1,radius=1):
		self.height=height
		self.radius=radius
	def volume(self):
		vlm=self.height*3.14*self.radius**2
		return vlm
	def surface_area(self):
		lateral=2*3.14*self.radius*self.height
		top_bottom=2*3.14*self.radius**2
		surface=lateral+top_bottom
		return surface
c=Cylinder(2,3)
c_volume=c.volume()
c_surface=c.surface_area()
print(c_volume,  c_surface)



