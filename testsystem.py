import goods
import goodsmanger

warehouse=list()#定义一个仓库
GM = goodsmanger.GoodsManager(warehouse)#定义一个管理员

def addCommodity():
    number = input("请输入商品的编号:")
    name = input("请输入商品的名字:")
    type = input("请输入商品的类型:")
    price = float(input("请输入商品的价格："))
    company=input("请输入商品的生产公司：")
    count = int(input(("请输入商品的数量：")))
    goods1=goods.Goods(number,name,type,price,company,count)
    GM.add(goods1)

def showAll():
    GM.showAll()

def deleteCommodity():
    number=input("请输入要删除的商品的编号：")
    GM.delete(number)


def purchaseCommodity():
    number = input("请输入进货商品的编号：")
    stock = int(input("请输入进货商品的数量："))
    GM.purchase(number,stock)

def queryCommodity():
    name = input("请输入想要查询的商品名称：")
    GM.query(name)

if __name__ == '__main__':
    while True:
        print("1.添加商品   2.显示所有商品   3.删除商品  4.购入商品   5.商品查询  0.退出系统")
        index=int(input("请选择:"))
        if index == 1:
            addCommodity()
        elif index == 2:
            showAll()
        elif index == 3:
            deleteCommodity()
        elif index == 4:
            purchaseCommodity()
        elif index == 5:
            queryCommodity()
        elif index == 0:
            break
        else:
            print("输入有误，重新输入")

