#!/usr/bin/env python3
# # -*- coding: utf-8 -*-


class CommonAttributes(object):
    """
    Description: All common attributes for both conditional and non-conditional products
    """
    max_quality_index = 50

    def __init__(self, item):
        self.item = item

    def appreciate_quality(self):
        # The Quality of an item is never more than 50. Increase only when it's below 50
        if self.item.quality < self.max_quality_index:
            self.item.quality = self.item.quality + 1

    def degrade_quality(self):
        # The Quality of an item is never negative, i.e. it will keep reducing until it reaches zero, depending on
        # product type
        if self.item.quality > 0:
            self.item.quality = self.item.quality - 1

    def decrease_sell_in(self):
        self.item.sell_in = self.item.sell_in - 1


class NonConditionalItems(CommonAttributes):

    def update_item_quality(self):
        self.decrease_sell_in()
        # Quality degrade when approach sell by date
        self.degrade_quality()

        # Once the sell by date has passed, Quality degrades twice as fast
        if self.item.sell_in < 0:
            self.degrade_quality()


class AgedBrie(CommonAttributes):
    def update_item_quality(self):
        self.decrease_sell_in()
        # "Aged Brie" actually increases in Quality the older it gets
        self.appreciate_quality()

        # Quality increase twice, reverse to default product
        if self.item.sell_in < 0:
            self.appreciate_quality()


class Sulfuras(CommonAttributes):
    # "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
    def update_item_quality(self):
        pass


class BackstagePasses(CommonAttributes):
    max_days = 10
    min_days = 5

    def update_item_quality(self):
        # Increases in Quality as its SellIn value approaches same like "Aged Brie";
        self.appreciate_quality()
        # Quality increases by 2 when there are 10 days or less, already appreciated once
        if self.item.sell_in <= self.max_days:
            self.appreciate_quality()
        # Quality increases by 3 when there are 5 days or less, already appreciated twice
        if self.item.sell_in <= self.min_days:
            self.appreciate_quality()
        self.decrease_sell_in()
        if self.item.sell_in < 0:
            # Quality drops to 0 when after the concert
            self.item.quality = 0


class Conjured(CommonAttributes):
    def update_item_quality(self):
        self.decrease_sell_in()
        # "Conjured" items degrade in Quality twice as fast as normal items
        self.degrade_quality()
        self.degrade_quality()

        if self.item.sell_in < 0:
            # Since non-conditional item's quality drop by twice when sell-in date passed, so it would drop twice faster
            self.degrade_quality()
            self.degrade_quality()


class UpdateItem(CommonAttributes):
    # Assigning product category to corresponding class
    item_name_cls_mapping_dict = {
        "Aged Brie": AgedBrie,
        "Sulfuras, Hand of Ragnaros": Sulfuras,
        "Backstage passes to a TAFKAL80ETC concert": BackstagePasses,
        "Conjured Mana Cake": Conjured
    }

    @classmethod
    def get_quality(cls, item):
        if item.name in cls.item_name_cls_mapping_dict:
            # Return each corresponding class
            return cls.item_name_cls_mapping_dict[item.name](item)
        # Otherwise return non-conditional product class
        return NonConditionalItems(item)


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item_updater = UpdateItem.get_quality(item)
            item_updater.update_item_quality()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
