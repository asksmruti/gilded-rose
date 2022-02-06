# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-


import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    #####################################
    # Non conditional products i.e. dpg #
    #####################################
    # Quality degrade when approach sell by date
    def test_dpg_quality_degrade(self):
        items = [Item(name="dpg", sell_in=10, quality=4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(["dpg", 9, 3], [items[0].name, items[0].sell_in, items[0].quality])

    # Once the sell by date has passed, Quality degrades twice as fast
    def test_dpg_quality_degrade_after_sale_date(self):
        items = [Item(name="dpg", sell_in=0, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(["dpg", -1, 8], [items[0].name, items[0].sell_in, items[0].quality])

    # The Quality of an item is never negative
    def test_dpg_quality_never_negative(self):
        items = [Item(name="dpg", sell_in=0, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(["dpg", -1, 0], [items[0].name, items[0].sell_in, items[0].quality])

    #############
    # Aged Brie #
    #############
    # Increases in Quality the older it gets
    def test_aged_brie_quality_appreciation(self):
        items = [Item(name="Aged Brie", sell_in=1, quality=1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(["Aged Brie", 0, 2], [items[0].name, items[0].sell_in, items[0].quality])

    # Double when sell date pass (Opposite to normal product)
    def test_aged_brie_quality_appreciation_after_sell_date(self):
        items = [Item(name="Aged Brie", sell_in=0, quality=1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(["Aged Brie", -1, 3], [items[0].name, items[0].sell_in, items[0].quality])

    # The Quality of an item is never go above 50
    def test_aged_brie_quality_never_above_50(self):
        items = [Item(name="Aged Brie", sell_in=10, quality=50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(["Aged Brie", 9, 50], [items[0].name, items[0].sell_in, items[0].quality])

    #############
    # Sulfuras  #
    #############
    def test_sulfuras_never_change(self):
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=10, quality=80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(["Sulfuras, Hand of Ragnaros", 10, 80], [items[0].name, items[0].sell_in, items[0].quality])

    #####################
    # Backstage passes  #
    #####################
    # Increases in Quality as its SellIn value approaches same like "Aged Brie";
    def test_backstage_passes_quality_appreciation(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=12, quality=4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(["Backstage passes to a TAFKAL80ETC concert", 11, 5], [items[0].name, items[0].sell_in,
                                                                                items[0].quality])

    # Quality increases by 2 when there are 10 days or less
    def test_backstage_passes_quality_appreciation_10(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=7)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(["Backstage passes to a TAFKAL80ETC concert", 9, 9], [items[0].name, items[0].sell_in,
                                                                               items[0].quality])

    # Quality increases by 3 when there are 5 days or less
    def test_backstage_passes_quality_appreciation_5(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=4, quality=7)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(["Backstage passes to a TAFKAL80ETC concert", 3, 10], [items[0].name, items[0].sell_in,
                                                                                items[0].quality])

    # Quality drops to 0 when after the concert
    def test_backstage_passes_drop_quality_0(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=7)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(["Backstage passes to a TAFKAL80ETC concert", -1, 0], [items[0].name, items[0].sell_in,
                                                                                items[0].quality])

    ############
    # Conjured #
    ###########
    # Once the sell by date has passed, Quality degrades twice as fast
    def test_conjured_quality_degrade(self):
        items = [Item(name="Conjured Mana Cake", sell_in=8, quality=4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(["Conjured Mana Cake", 7, 2], [items[0].name, items[0].sell_in, items[0].quality])

    # When sell date go off quality degrades twice of normal items
    def test_conjured_quality_degrade_after_sell_date(self):
        items = [Item(name="Conjured Mana Cake", sell_in=0, quality=8)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(["Conjured Mana Cake", -1, 4], [items[0].name, items[0].sell_in, items[0].quality])


if __name__ == '__main__':
    unittest.main()
