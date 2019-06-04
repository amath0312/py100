
import matplotlib
import matplotlib.pyplot as plt
from copy import deepcopy


class Asset():

    def __init__(self):
        self.device_cnt = 0
        self.balance = 0
        self.buy_product = 0
        self.remain_product = 0
        self.invest = 0
        self.income = 0
        self.cost = 0

    def __str__(self):
        s = '[assets]:\n'
        s += '    device: %d\n' % self.device_cnt
        s += '    invest: %d\n' % self.invest
        s += '    buy_product: %d\n' % self.buy_product
        s += '    remain_product: %d\n' % self.remain_product
        s += '    income: %d\n' % self.income
        s += '    cost: %d\n' % self.cost
        s += '    balance: %d\n' % self.balance
        return s

    def __repr__(self):
        return str(self)


class Partner():

    def __init__(self):
        self.day_sell = 500
        self.min_product = 10000
        self.day_ad = 10
        self.profit_percent = 0.4
        self.ad_percent = 0.3
        self.service_fee = 0.1
        self.band = 0
        self.space = 5000
        self.device = 7999
        self.asset = Asset()

    def monthly_asset(self, device_cnt, year=3):
        self._invest(device_cnt)
        device_cnt = self.asset.device_cnt
        self.asset.cost = self.asset.cost
        print(self.asset)
        yield deepcopy(self.asset)

        months = year * 12
        for month in range(1, months + 1):
            ad_income = self._sell_ad()
            product_income = self._sell_product()

            cost = self.service_fee * product_income + self.space / 12 * device_cnt
            cost += self._buy_product()
            self.asset.cost += cost

            self.asset.balance += product_income + ad_income - cost
            print(self.asset)
            yield deepcopy(self.asset)

    def _sell_product(self):
        revenue = self.day_sell * 30 * self.asset.device_cnt
        self.asset.remain_product -= revenue * (1 - self.profit_percent)
        self.asset.income += revenue
        return revenue

    def _sell_ad(self):
        ad = self.day_ad * 30 * self.ad_percent * self.asset.device_cnt
        self.asset.income += ad
        return ad

    def _invest(self, device_cnt):
        self.asset = Asset()
        self.asset.device_cnt = device_cnt
        self.asset.invest = self.device * device_cnt + self.band + self._buy_product()
        self.asset.balance = -self.asset.invest

    def _buy_product(self):
        device_cnt = self.asset.device_cnt
        need_product = self.day_sell * \
            (1 - self.profit_percent) * 30 * device_cnt
        if self.asset.remain_product >= need_product:
            self.asset.buy_product = 0
            return 0
        buy_product = need_product - self.asset.remain_product
        if buy_product < self.min_product:
            buy_product = self.min_product
        self.asset.remain_product += buy_product
        self.asset.buy_product = buy_product
        return buy_product

    def cost(self, device_cnt, year):
        '''总成本'''
        all_sells = self._product_revenue(device_cnt, year)
        service_fee = all_sells * self.service_fee
        band = self.band
        product_fee = all_sells * (1 - self.profit_percent)
        device_cost = self.device * device_cnt
        space = self.space * year * device_cnt
        return service_fee + band + product_fee + device_cost + space

    def revenue(self, device_cnt, year):
        '''总收入'''
        return self._product_revenue(device_cnt, year) \
            + self._ad_revenue(device_cnt, year)

    def profit(self, device_cnt, year):
        '''总利润'''
        return self.revenue(device_cnt, year) - self.cost(device_cnt, year)

    def roi(self, device_cnt, year):
        return 1.0 * self.profit(device_cnt, year) / self.cost(device_cnt, year)

    def _product_revenue(self, device_cnt, year):
        '''产品销售总额'''
        all_sells = self.day_sell * 360 * year * device_cnt
        return all_sells

    def _ad_revenue(self, device_cnt, year):
        '''广告分成总额'''
        ad_sells = self.day_ad * 360 * year * device_cnt * self.ad_percent
        return ad_sells


def figure_by_count(year):
    p = Partner()
    X1 = range(1, 50)
    # Y1 = [p.profit(cnt, year) for cnt in X1]
    Y2 = [p.roi(cnt, year) for cnt in X1]

    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['font.family'] = 'sans-serif'

    # plt.plot(X1, Y1, 'r')
    plt.plot(X1, Y2, 'g')
    plt.xlabel('加盟设备')
    plt.ylabel('投资回报率')
    plt.show()


def figure_by_year(count):
    p = Partner()
    X1 = range(1, 50)
    # Y1 = [p.profit(count, year) for cnt in X1]
    Y2 = [p.roi(count, year) for year in X1]

    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['font.family'] = 'sans-serif'
    # plt.plot(X1, Y1, 'r')
    plt.plot(X1, Y2, 'g')
    plt.xlabel('合作期限（年）')
    plt.ylabel('投资回报率')
    plt.show()


def figure_assets(device_cnt, year):
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['font.family'] = 'sans-serif'
    p = Partner()
    X1 = range(year * 12 + 1)
    Y1 = [asset.balance for asset in p.monthly_asset(device_cnt, year)]

    X2 = range(1 * 12 + 1)
    Y2 = [asset.balance for asset in p.monthly_asset(device_cnt, 1)]

    X3 = range(year * 12 + 1)
    Y3 = [asset.balance for asset in p.monthly_asset(1, year)]
    print(Y3 == Y1)
    plt.style.use('ggplot')
    A, = plt.plot(X1, Y1, 'r', label='%d台设备经营%d年' % (device_cnt, year))
    plt.annotate(
        '%.2f' % Y1[-1],
        xy=(year * 12, int(Y1[-1])),
        xytext=(year * 12, int(Y1[-1]) * 1.05),
    )

    B, = plt.plot(X2, Y2, 'g', label='%d台设备经营%d年' % (device_cnt, 1))
    plt.annotate(
        '%.2f' % Y2[-1],
        xy=(1 * 12, int(Y2[-1])),
        xytext=(1 * 12, int(Y2[-1]) * 1.05),
    )

    C, = plt.plot(X3, Y3, 'b', label='%d台设备经营%d年' % (1, year))
    plt.annotate(
            '%.2f' % Y3[-1],
            xy=(year * 12, int(Y3[-1])), 
            xytext=(year * 12, int(Y3[-1])*1.05)
        )

    plt.xlabel('日期（月）')
    plt.ylabel('净利润')
    plt.xticks(X1)
    plt.legend(handles=[A, B, C])

    plt.show()


def main():
    p = Partner()
    print(p.cost(1, 3))
    print(p.revenue(1, 3))
    print(p.profit(1, 3))
    # figure()
    # figure_by_count(3)
    # figure_by_year(10)
    figure_assets(5, 3)


if __name__ == '__main__':
    main()
