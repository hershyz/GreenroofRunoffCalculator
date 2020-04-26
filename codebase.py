def calculate(rawArea, rawN, rawInches):

    print("-------------------------------------------")
    
    maxSaved = .6
    minSaved = .5

    area = int(rawArea)
    n = int(rawN)
    inches = int(rawInches)
    
    tempArea = area / 100
    gallons = tempArea * 62
    yearlyGallons = gallons * inches

    print("yearly stormwater runoff from one structure (traditional roof): " + str(yearlyGallons))
    print("yearly stormwater runoff from one structure (green roof): " + str(yearlyGallons - (maxSaved * yearlyGallons))  + " to " + str(yearlyGallons - (minSaved * yearlyGallons)))

    nGallons = yearlyGallons * n

    print("yearly stormwater runoff from neighborhood (traditional roof): " + str(nGallons))
    print("yearly stormwater runoff from neighborhood structure (green roof): " + str(nGallons - (maxSaved * nGallons)) + " to " + str(nGallons - (minSaved * nGallons)))