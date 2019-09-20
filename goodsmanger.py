class GoodsManager: #GoodsManager为管理员
    def __init__(self,warehouse): #属性warehouse为仓库
        self.warehouse = warehouse

    def add(self,goods): #为仓库内增加新的商品

        flag = False
        if len(self.warehouse) > 0 :
            for b in self.warehouse:
                    if b.number==goods.number:
                        flag=True

        if not flag :
            self.warehouse.append(goods)
            print("编号为",goods.number,"的商品已入库")
        else:
            print("这个商品已经存在,无法重复添加！")

    def showAll(self):  #显示所有的商品信息
        if len(self.warehouse) > 0 :
            print("商品编号   商品名称    商品类型    商品价格    生产公司    库存")
            for goods in self.warehouse:
                print(goods.number,"   ",goods.name,"  ",goods.type,"     ",goods.price,"     ",goods.company,"     ",goods.count)
        else:
            print("仓库中没有商品！")

    def delete(self,number): #删除商品信息
        if len(self.warehouse) > 0 :
            flag = False#标识商品是否删除
            for goods in self.warehouse:
                if goods.number == number :
                    self.warehouse.remove(goods)
                    flag = True
                    break
            if flag:
                print(number,"已经从仓库上移除！")
            else:
                print("仓库中没有",number,"的商品，无法移除！")
        else:
            print("目前仓库中没有此商品！")

    def purchase(self,number,stock):  #购买商品进货

        if len(self.warehouse) > 0 :
            isExist = False#商品存在状态
            for goods in self.warehouse:
                if goods.number == number :
                    isExist = True#商品存在
                    goods.count = goods.count+stock#更新库存
                    print("库存已经更新")
                    break
            if not isExist:
                print(number,"这个商品仓库中还没有，请添加商品信息!")
        else:
            print("仓库还空空如也，你要干什么？")

    def query(self,name): #商品查询

        if len(self.warehouse) > 0:
            print("商品编号   商品名称    商品类型    商品价格    生产公司    库存")
            for goods in self.warehouse:
                if goods.name==name:
                    print(goods.number,"   ",goods.name,"  ",goods.type,"     ",goods.price,"     ",goods.company,"     ",goods.count)
                else:
                    print("没有找到这个名称的商品")
                    return  #return的两个作用：①为方法返回一个值  ②方法结束
        else:
            print("仓库中没有商品！")
            return





