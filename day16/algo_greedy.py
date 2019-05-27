
def thief():
    """
    贪婪法：在对问题求解时，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解。
    输入：
    最大承受重量 20
    电脑 200 20
    收音机 20 4
    钟 175 10
    花瓶 50 2
    书 10 1
    油画 90 9
    """
    class Thing(object):
        def __init__(self, name, price, weight):
            self.name = name
            self.price = price
            self.weight = weight

        @property
        def value(self):
            """价格重量比"""
            return self.price / self.weight
        def __str__(self):
                return '{}:${}/{}'.format(self.name,self.price,self.weight)
        def __repr__(self):
                return self.__str__()

    max_weight = 20
    max_count = 6
    lines = [x.strip() for x in """
            电脑 200 20
            收音机 20 4
            钟 175 10
            花瓶 50 2
            书 10 1
            油画 90 9
        """.split('\n') if (x is not None) and x.strip() != '']
    things = []
    for line in lines:
        name,price,weight=line.split()
        things.append(Thing(name,int(price),int(weight)))
    things.sort(key=lambda t:t.value, reverse=True)
    print(things)
    total_weight=0
    total_price=0
    steal=[]
    for t in things:
        if total_weight+t.weight<=max_weight:
            total_price+=t.price
            total_weight+=t.weight
            steal.append(t)
            
    print('weight:',total_weight,' | price',total_price )
    print(steal)



if __name__ == '__main__':
    thief()
    
