def get_product_type(product_name):
    product_name = product_name.lower()
    product_type = ("", 0)
    if "t-shirt" in product_name or 'tee' in product_name or " shirt" in product_name or "shirts" in product_name:
        product_type = ("tee", 1)
    if "set" in product_name:
        product_type = ("sets", 49)
    if "hat" in product_name:
        product_type = ("hat", 33)
    if "cap" in product_name:
        product_type = ("cap", 875)
    if "wrap" in product_name:
        product_type = ("wrap", 788)
    if "top" in product_name:
        product_type = ("top", 3)
    if "crossbody" in product_name:
        product_type = ("crossbody", 268)
    if "bra" in product_name:
        product_type = ("bra", 966)
    if "belt" in product_name:
        product_type = ("belt", 29)
    if "short" in product_name:
        product_type = ("shorts", 2)
    if "halter" in product_name:
        product_type = ("halter", 30)
    if "capri" in product_name:
        product_type = ("capri", 345)
    if "wig" in product_name:
        product_type = ("wig", 336)
    if "denim" in product_name:
        product_type = ("denim", 51)
    if "jean" in product_name:
        product_type = ("jeans", 18)
    if "cami" in product_name:
        product_type = ("cami", 26)
    if "mask" in product_name:
        product_type = ("mask", 222)
    if "bag" in product_name:
        product_type = ("bag", 57)
    if "long sleeve" in product_name:
        product_type = ("long sleeve", 229)
    if "crew neck" in product_name:
        product_type = ("crew neck", 987)
    if "hair" in product_name:
        product_type = ("hair", 521)
    if "v-neck" in product_name:
        product_type = ("v-neck", 735)
    if "studs" in product_name:
        product_type = ("studs", 48)
    if "vest" in product_name:
        product_type = ("vest", 691)
    if "polo" in product_name:
        product_type = ("polo", 678)
    if "thong" in product_name:
        product_type = ("thong", 65)
    if "slides" in product_name:
        product_type = ("slides", 679)
    if "slipper" in product_name:
        product_type = ("slippers", 680)
    if "sherpa" in product_name:
        product_type = ("sherpa", 570)
    if "chain" in product_name:
        product_type = ("chain", 240)
    if "chinos" in product_name:
        product_type = ("chinos", 690)
    if "chemise" in product_name:
        product_type = ("chemise", 699)
    if "raglan" in product_name:
        product_type = ("raglan", 347)
    if "choker" in product_name:
        product_type = ("choker", 369)
    if "jumper" in product_name:
        product_type = ("jumper", 378)
    if "teddy" in product_name:
        product_type = ("teddy", 261)
    if "babydoll" in product_name:
        product_type = ("babydoll", 262)
    if "dad hat" in product_name:
        product_type = ("dad hat", 330)
    if "heel" in product_name:
        product_type = ("heel", 47)
    if "g-string" in product_name:
        product_type = ("g-string", 655)
    if "stiletto" in product_name:
        product_type = ("stiletto", 470)
    if "shawl" in product_name:
        product_type = ("shawl", 471)
    if "one piece" in product_name or "1 piece" in product_name:
        product_type = ("one piece", 53)
    if "two piece" in product_name or "2 piece" in product_name:
        product_type = ("two piece", 54)
    if "three piece" in product_name or "3 piece" in product_name:
        product_type = ("three piece", 55)
    if "veil" in product_name:
        product_type = ("veil", 472)
    if "boot" in product_name and "booty" not in product_name:
        product_type = ("boot", 63)
    if "booties" in product_name:
        product_type = ("booties", 734)
    if "suit" in product_name:
        product_type = ("suit", 273)
    if "tuxedo" in product_name:
        product_type = ("tuxedo", 274)
    if "booty short" in product_name:
        product_type = ("booty shorts", 4)
    if "booty lift" in product_name:
        product_type = ("booty lift", 444)
    if "boy short" in product_name or "boyshort" in product_name:
        product_type = ("boy shorts", 5)
    if "bottoms" in product_name:
        product_type = ("bottoms", 6)
    if "underwear" in product_name:
        product_type = ("underwear", 457)
    if "sweater" in product_name or "sweatshirt" in product_name:
        product_type = ("sweater", 7)
    if "sweatpant" in product_name:
        product_type = ("sweatpants", 8)
    if "pullover" in product_name or "pull over" in product_name:
        product_type = ("pullover", 999)
    if "hoodie" in product_name:
        product_type = ("hoodie", 9)
    if "cover up" in product_name or "cover-up" in product_name:
        product_type = ("cover up", 10)
    if "swim" in product_name:
        product_type = ("swimsuit", 11)
    if "pillow" in product_name:
        product_type = ("pillow", 493)
    if "bikini" in product_name:
        product_type = ("bikini", 12)
    if "leotard" in product_name:
        product_type = ("leotard", 118)
    if "pants" in product_name or "trousers" in product_name:
        product_type = ("pants", 13)
    if "panties" in product_name or "panty" in product_name:
        product_type = ("panties", 14)
    if "pantyhose" in product_name:
        product_type = ("pantyhose", 114)
    if "legging" in product_name or "yoga pant" in product_name or "7/8" in product_name:
        product_type = ("leggings", 15)
    if "short legging" in product_name or "biker" in product_name:
        product_type = ("short leggings", 299)
    if "tank" in product_name:
        product_type = ("tank", 16)
    if "bustier" in product_name:
        product_type = ("bustier", 161)
    if "glasses" in product_name:
        product_type = ("glasses", 408)
    if "sunglasses" in product_name or "shades" in product_name:
        product_type = ("sunglasses", 409)
    if "romper" in product_name:
        product_type = ("romper", 17)
    if "cardi" in product_name:
        product_type = ("cardigan", 19)
    if "gown" in product_name:
        product_type = ("gown", 190)
    if "nightgown" in product_name:
        product_type = ("nightgown", 191)
    if "blouse" in product_name:
        product_type = ("blouse", 20)
    if "dress" in product_name:
        product_type = ("dress", 21)
    if "brief" in product_name:
        product_type = ("brief", 5387)
    if "mini dress" in product_name:
        product_type = ("mini dress", 22)
    if "maxi" in product_name and "maximum" not in product_name:
        product_type = ("maxi", 23)
    if "midi" in product_name:
        product_type = ("midi", 24)
    if "jumpsuit" in product_name:
        product_type = ("jumpsuit", 25)
    if "tracksuit" in product_name:
        product_type = ("tracksuit", 250)
    if "bodysuit" in product_name:
        product_type = ("bodysuit", 355)
    if "headband" in product_name:
        product_type = ("headband", 27)
    if "garter" in product_name:
        product_type = ("garter", 270)
    if "fishnet" in product_name:
        product_type = ("fishnets", 271)
    if "jogger" in product_name:
        product_type = ("joggers", 28)
    if "platform" in product_name:
        product_type = ("platforms", 280)
    if "clutch" in product_name:
        product_type = ("clutch", 267)
    if "tights" in product_name:
        product_type = ("leggings", 15)
    if "crop" in product_name:
        product_type = ("crop", 31)
    if "crop tee" in product_name:
        product_type = ("crop tee", 32)
    if "crop" in product_name and "hoodie" in product_name:
        product_type = ("crop hoodie", 332)
    if "jacket" in product_name:
        product_type = ("jacket", 34)
    if "breaker" in product_name:
        product_type = ("breaker", 334)
    if "sunsuit" in product_name:
        product_type = ("sunsuit", 340)
    if "playsuit" in product_name:
        product_type = ("playsuit", 35)
    if "costume" in product_name:
        product_type = ("costume", 36)
    if "coat" in product_name:
        product_type = ("coat", 37)
    if "waistcoat" in product_name:
        product_type = ("waistcoat", 370)
    if "skirt" in product_name:
        product_type = ("skirt", 38)
    if "sports bra" in product_name:
        product_type = ("sports bra", 40)
    if "bralet" in product_name:
        product_type = ("bralet", 41)
    if "sock" in product_name:
        product_type = ("socks", 42)
    if "stocking" in product_name:
        product_type = ("stockings", 43)
    if "sandal" in product_name:
        product_type = ("sandal", 44)
    if "flip flop" in product_name or "flip-flop" in product_name:
        product_type = ("flip flops", 440)
    if "shoe" in product_name:
        product_type = ("shoe", 45)
    if "sneakers" in product_name:
        product_type = ("sneakers", 46)
    if "corset" in product_name:
        product_type = ("corset", 50)
    if "glove" in product_name:
        product_type = ("gloves", 400)
    if "flannel" in product_name:
        product_type = ("flannel", 52)
    if "onesie" in product_name:
        product_type = ("onesie", 56)
    if "purse" in product_name:
        product_type = ("purse", 58)
    if "tunic" in product_name:
        product_type = ("tunic", 59)
    if "scarf" in product_name:
        product_type = ("scarf", 60)
    if "overall" in product_name:
        product_type = ("overalls", 61)
    if "lounge" in product_name:
        product_type = ("loungewear", 62)
    if "pumps" in product_name:
        product_type = ("pumps", 64)
    if "garter" in product_name:
        product_type = ("garter", 66)
    if "earring" in product_name:
        product_type = ("earrings", 67)
    if "pendant" in product_name:
        product_type = ("pendant", 676)
    if "bracelets" in product_name:
        product_type = ("bracelet", 68)
    if "anklet" in product_name:
        product_type = ("anklet", 70)
    if "lingerie" in product_name:
        product_type = ("lingerie", 71)
    if "necklace" in product_name:
        product_type = ("necklace", 69)
    if "backpack" in product_name:
        product_type = ("backpack", 73)
    if "jersey" in product_name:
        product_type = ("jersey", 74)
    if "beanie" in product_name:
        product_type = ("beanie", 75)
    if "bandana" in product_name:
        product_type = ("bandana", 76)
    if "blazer" in product_name:
        product_type = ("blazer", 77)
    if "board shorts" in product_name:
        product_type = ("board shorts", 78)
    if "boxers" in product_name:
        product_type = ("boxers", 79)
    if "henley" in product_name:
        product_type = ("henley", 80)
    if "jeggings" in product_name:
        product_type = ("jeggings", 81)
    if "kimono" in product_name:
        product_type = ("kimono", 82)
    if "nightie" in product_name or "nightwear" in product_name:
        product_type = ("nightwear", 83)
    if "pajama" in product_name or "pyjama" in product_name:
        product_type = ("pajamas", 84)
    return product_type