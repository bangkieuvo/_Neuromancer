class IpV4():
	def __init__(self,value = []):
		self.value = value
	def setIpByBinary(self):
		returns
	def setIpByDecimal(self,str):
		newValue = [] 
		l = str.split(".")
		for char in l:
			num = int(char)
			if (num<0 or num>255):
				print(f"[❌ Wrong input! ({num} is not validate)]")
				return
			newValue.append(num)
		self.value = newValue.copy()
	def show(self,choice = 0):
		if choice == 0:
			print(self.value)
ip = IpV4()
ip.setIpByDecimal("125.25.-7.1")
print(ip.value)