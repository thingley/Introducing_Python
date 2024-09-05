boolValue = bool(1)
print(boolValue)

intValue = int(14.0)
print(intValue)

floatValue = float('14.1')
print(floatValue)

combinedvalue = int(boolValue) + intValue + floatValue
combinedValueType = type(combinedvalue)
print(combinedvalue)
print(combinedValueType)
