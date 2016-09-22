def whileLoop_notRecursion (num_beers):
    while num_beers != 0:
        print(str(num_beers) + " bottles of beer on the wall")
        print(str(num_beers) + " bottles of beer,")
        print("if one of those bottles should happen to fall")
        num_beers -= 1
        if num_beers == 0:
            print("No more bottles of beer on the wall")
            return 
        print(str(num_beers) + " bottles of beer left on the wall\n")

whileLoop_notRecursion(10)
