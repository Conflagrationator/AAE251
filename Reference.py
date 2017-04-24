dragdV = dragLossUpToAltitude(160)
gravdV= gravityLossUpToAltitude(160)
steeringdV= steeringLoss()

dVfor500 = .19540362680297374 * 10**3 + dragdV + gravdV + steeringdV # m/s
dVforGeoTransfer = 2.467596447585046 * 10**3 + dragdV + gravdV + steeringdV # m/s
dVforGeoStatOrbit = 4.4780452652 * 10**3 + dragdV + gravdV + steeringdV # m/s