class GildedRose(object):

    def __init__(self, items):
        self.items = items

    backstage_pass = "Backstage passes to a TAFKAL80ETC concert"
    ragnaros = "Sulfuras, Hand of Ragnaros"
    brie = "Aged Brie"

    def update_quality(self):
        for item in self.items:
            self.change_item_quality(item)

            self.decrease_sell_in(item)

            if item.sell_in < 0:
                self.handle_passed_sell_by_date(item)

    def change_item_quality(self, item):
        if item.name == self.brie:
            self.increase_quality_by_one(item)
        elif item.name == self.backstage_pass:
            self.increase_quality_by_one(item)
            if item.sell_in <= 10:
                self.increase_quality_by_one(item)
            if item.sell_in <= 5:
                self.increase_quality_by_one(item)
        else:
            self.decrease_quality_by_one(item)

    def handle_passed_sell_by_date(self, item):
        if item.name == self.brie:
            self.increase_quality_by_one(item)
        elif item.name == self.backstage_pass:
            item.quality = 0
        else:
            self.decrease_quality_by_one(item)

    def decrease_sell_in(self, item):
        if item.name != self.ragnaros:
            item.sell_in = item.sell_in - 1

    def increase_quality_by_one(self, item):
        if item.quality < 50:
            item.quality += 1

    def decrease_quality_by_one(self, item):
        if item.name != self.ragnaros and item.quality > 0:
            item.quality -= 1
