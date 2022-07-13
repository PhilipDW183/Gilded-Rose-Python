class GildedRose(object):

    def __init__(self, items):
        self.items = items

    backstage_pass = "Backstage passes to a TAFKAL80ETC concert"
    ragnaros = "Sulfuras, Hand of Ragnaros"
    brie = "Aged Brie"


    def update_quality(self):
        for item in self.items:
            if item.name != self.brie and item.name != self.backstage_pass:
                if item.quality > 0:
                    if item.name != self.ragnaros:
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == self.backstage_pass:
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != self.ragnaros:
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != self.brie:
                    if item.name != self.backstage_pass:
                        if item.quality > 0:
                            if item.name != self.ragnaros:
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1
