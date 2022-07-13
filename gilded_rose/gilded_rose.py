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
        if item.name == self.brie and item.quality < 50:
            item.quality = item.quality + 1
        elif item.name == self.backstage_pass and item.quality < 50:
            item.quality = item.quality + 1
            if item.sell_in < 11 and item.quality < 50:
                item.quality = item.quality + 1
            if item.sell_in < 6 and item.quality < 50:
                item.quality = item.quality + 1
        elif item.name != self.ragnaros and item.quality > 0:
            item.quality = item.quality - 1

    def handle_passed_sell_by_date(self, item):
        if item.name == self.brie and item.quality < 50:
            item.quality = item.quality + 1
        elif item.name == self.backstage_pass:
            item.quality = 0
        elif item.name != self.ragnaros and item.quality > 0:
            item.quality = item.quality - 1

    def decrease_sell_in(self, item):
        if item.name != self.ragnaros:
            item.sell_in = item.sell_in - 1
