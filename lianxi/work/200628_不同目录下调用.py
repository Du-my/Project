#不同包跟目录下调用
from apple import iphone6
iphone6.askPrice()
from apple import iphone7
iphone7.askPrice()

from python.samsung.note import galaxy_note8
galaxy_note8.askPrice()

from python.samsung.s import galaxy_s7
galaxy_s7.askPrice()
